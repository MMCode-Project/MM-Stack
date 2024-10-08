import json
import html
import pandas as pd
from io import StringIO
from datasets import load_dataset, Dataset
import os
from tqdm import tqdm

def extract_markdown_outputs(cells):
    outputs = []
    for idx, cell in enumerate(cells):
        if cell.get('cell_type') == 'markdown':
            source = "".join(cell.get('source', []))
            if any(keyword in source for keyword in ['$$', '\\begin{', '\\end{', '|', '---']):
                outputs.append({'cell_index': idx, 'type': 'markdown_output', 'content': source})
    return outputs

def extract_images(cells):
    images = []
    for idx, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            for output in cell.get('outputs', []):
                if output.get('output_type') == 'display_data':
                    for image_type in ['image/png', 'image/jpeg', 'image/svg+xml', 'image/gif']:
                        if image_type in output.get('data', {}):
                            image_data = output['data'][image_type]
                            images.append({'cell_index': idx, 'type': 'image', 'content': image_data})
    return images

def extract_code_output_tables(cells):
    tables = []
    for idx, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            for output in cell.get('outputs', []):
                if output.get('output_type') in {'display_data', 'execute_result'}:
                    if 'text/plain' in output.get('data', {}):
                        text_data = output['data']['text/plain']
                        if "   " in text_data and "\n" in text_data:
                            try:
                                df = pd.read_csv(StringIO(text_data), sep=r'\s+')
                                tables.append({'cell_index': idx, 'type': 'code_output_table', 'content': df.to_dict()})
                            except Exception:
                                continue
    return tables

def extract_json_html_outputs(cells):
    outputs = []
    for idx, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            for output in cell.get('outputs', []):
                if output.get('output_type') in ['display_data', 'execute_result']:
                    data = output.get('data', {})
                    
                    if 'application/json' in data:
                        json_data = data['application/json']
                        outputs.append({'cell_index': idx, 'type': 'json', 'content': json_data})
                    
                    if 'text/html' in data:
                        html_data = data['text/html']
                        if isinstance(html_data, list):
                            html_data = ''.join(html_data)
                        outputs.append({'cell_index': idx, 'type': 'html', 'content': html.unescape(html_data)})
    
    return outputs

def create_notebook_json(cells):
    notebook_data = []

    notebook_data.extend(extract_markdown_outputs(cells))
    notebook_data.extend(extract_images(cells))
    notebook_data.extend(extract_code_output_tables(cells))
    notebook_data.extend(extract_json_html_outputs(cells))

    return notebook_data

def process_notebook(example):
    try:
        cells = json.loads(example['content'])['cells']
        outputs = create_notebook_json(cells)
        example['visual_output'] = json.dumps(outputs)
    except Exception as e:
        example['visual_output'] = None
    return example

def main():
    # Load the dataset
    ds = load_dataset("bigcode/the-stack", data_dir="data/jupyter-notebook", split="train", download_mode='force_redownload', cache_dir='./cache')

    # Set batch size and output directory
    batch_size = 1000
    output_dir = "processed_notebooks"
    os.makedirs(output_dir, exist_ok=True)

    # Find the last processed batch
    processed_files = [f for f in os.listdir(output_dir) if f.startswith("batch_") and f.endswith(".jsonl")]
    last_batch = max([int(f.split("_")[1].split(".")[0]) for f in processed_files]) if processed_files else 0

    # Process batches
    batch_num = last_batch + 1
    for start_idx in tqdm(range(0, len(ds), batch_size), desc="Processing batches"):
        if batch_num <= last_batch:
            batch_num += 1
            continue

        batch = ds.select(range(start_idx, min(start_idx + batch_size, len(ds))))
        processed_batch = batch.map(process_notebook)

        # Filter out examples with empty visual_output
        filtered_batch = [example for example in processed_batch if example['visual_output']]

        # Write to JSONL file
        output_file = os.path.join(output_dir, f"batch_{batch_num}.jsonl")
        with open(output_file, 'w') as f:
            for example in filtered_batch:
                f.write(json.dumps(example) + '\n')

        batch_num += 1

    # After processing all batches, combine JSONL files and push to Hub
    combined_dataset = Dataset.from_json(f"{output_dir}/batch_*.jsonl")
    combined_dataset.push_to_hub("bigcode/the-stack-ipynb-p2c", private=True)

if __name__ == "__main__":
    main()