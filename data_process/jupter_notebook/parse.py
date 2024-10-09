import json
import time
import html
import pandas as pd
from io import StringIO
from datasets import load_dataset, Dataset
import os
from tqdm import tqdm
import re
import urllib.parse
from bs4 import BeautifulSoup  # For HTML parsing
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_markdown_outputs(cells):
    outputs = []
    for idx, cell in enumerate(cells):
        if cell.get('cell_type') == 'markdown':
            source = "".join(cell.get('source', []))
            if isinstance(source, str):
                if any(keyword in source for keyword in ['$$', '\\begin{', '\\end{', '|', '---']):
                    outputs.append({'cell_index': idx, 'type': 'markdown_output', 'content': source})
                # Extract code blocks from markdown cells
                code_block_pattern = r'```[\s\S]*?```'
                code_blocks = re.findall(code_block_pattern, source)
                for block in code_blocks:
                    outputs.append({'cell_index': idx, 'type': 'markdown_code_block', 'content': block})
                # Extract embedded HTML/CSS and JavaScript
                if '<style>' in source or '<div>' in source or '<script>' in source:
                    outputs.append({'cell_index': idx, 'type': 'embedded_html', 'content': source})
                # Extract images and multimedia from markdown
                image_pattern = r'!\[.*?\]\((.*?)\)'
                images = re.findall(image_pattern, source)
                for image in images:
                    outputs.append({'cell_index': idx, 'type': 'markdown_image', 'content': image})
            else:
                logging.error(f"Unexpected type for markdown source: {type(source)}")
    return outputs

def extract_images(cells):
    images = []
    for idx, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            for output in cell.get('outputs', []):
                if output.get('output_type') == 'display_data':
                    for image_type in output.get('data', {}):
                        if image_type.startswith('image/'):
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
                        # Join list into a single string if necessary
                        if isinstance(text_data, list):
                            text_data = ''.join(text_data)
                        if isinstance(text_data, str):
                            # Check for various table formats
                            if re.search(r'^\s*\w+\s+\w+.*\n[-\s]+\n', text_data, re.MULTILINE) or \
                               re.search(r'^\s*\|.*\|.*\n\s*\|[-:]+\|', text_data, re.MULTILINE) or \
                               'DataFrame' in text_data:
                                tables.append({'cell_index': idx, 'type': 'code_table', 'content': text_data})
                        else:
                            logging.error(f"Unexpected type for text data: {type(text_data)}")
                    if 'text/html' in output.get('data', {}):
                        html_data = output['data']['text/html']
                        # Join list into a single string if necessary
                        if isinstance(html_data, list):
                            html_data = ''.join(html_data)
                        if isinstance(html_data, str):
                            soup = BeautifulSoup(html_data, 'html.parser')
                            for table in soup.find_all('table'):
                                tables.append({'cell_index': idx, 'type': 'html_table', 'content': str(table)})
                        else:
                            logging.error(f"Unexpected type for HTML data: {type(html_data)}")
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
                        if isinstance(json_data, (str, dict)):
                            outputs.append({'cell_index': idx, 'type': 'json', 'content': json_data})
                        else:
                            logging.error(f"Unexpected type for JSON data: {type(json_data)}")
                    
                    if 'text/html' in data:
                        html_data = data['text/html']
                        # Join list into a single string if necessary
                        if isinstance(html_data, list):
                            html_data = ''.join(html_data)
                        if isinstance(html_data, str):
                            html_data = html.unescape(html_data)
                            if html_data:
                                outputs.append({'cell_index': idx, 'type': 'html', 'content': html_data})
                        else:
                            logging.error(f"Unexpected type for HTML data: {type(html_data)}")
    
    return outputs

def extract_file_paths_and_links(cells):
    file_paths_and_links = []
    
    file_path_pattern = r'(?:\'|")([^\'"\s]+\.(?:csv|txt|json|xlsx?|tsv|parquet|hdf5?|sav|dta|sas7bdat|mat|pkl|feather|h5|nc))(?:\'|")'
    url_pattern = r'(https?://\S+)'
    
    for idx, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            source = "".join(cell.get('source', []))
            if isinstance(source, str):
                # Extract file paths
                file_paths = re.findall(file_path_pattern, source)
                for path in file_paths:
                    if '*' not in path and '?' not in path:
                        file_paths_and_links.append({
                            'cell_index': idx,
                            'type': 'data_source',
                            'content': path
                        })
                
                # Extract URLs
                urls = re.findall(url_pattern, source)
                for url in urls:
                    parsed_url = urllib.parse.urlparse(url)
                    if parsed_url.path.lower().endswith(('.csv', '.txt', '.json', '.xlsx', '.xls', '.tsv', '.parquet', '.hdf', '.hdf5', '.sav', '.dta', '.sas7bdat', '.mat', '.pkl', '.feather', '.h5', '.nc')):
                        file_paths_and_links.append({
                            'cell_index': idx,
                            'type': 'data_source',
                            'content': url
                        })
            else:
                logging.error(f"Unexpected type for code source: {type(source)}")
    
    return file_paths_and_links

def extract_multimedia_outputs(cells):
    multimedia = []
    for idx, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            for output in cell.get('outputs', []):
                if output.get('output_type') == 'display_data':
                    for media_type in output.get('data', {}):
                        if media_type.startswith('audio/') or media_type.startswith('video/'):
                            multimedia.append({'cell_index': idx, 'type': media_type, 'content': output['data'][media_type]})
    return multimedia

def extract_interactive_plots(cells):
    plots = []
    for idx, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            for output in cell.get('outputs', []):
                if output.get('output_type') in ['display_data', 'execute_result']:
                    data = output.get('data', {})
                    if any(key for key in data if key.startswith('application/')):
                        for key in data:
                            if key.startswith('application/'):
                                plots.append({'cell_index': idx, 'type': key, 'content': data[key]})
    return plots

def extract_text_visualizations(cells):
    visualizations = []
    for idx, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            for output in cell.get('outputs', []):
                if output.get('output_type') in ['execute_result', 'display_data']:
                    if 'text/plain' in output.get('data', {}):
                        text = output['data']['text/plain']
                        # Check if text is a list and join it into a single string
                        if isinstance(text, list):
                            text = ''.join(text)
                        if isinstance(text, str):
                            if re.search(r'[│├──└]', text):  # Simple check for tree-like structures
                                visualizations.append({'cell_index': idx, 'type': 'text_tree', 'content': text})
                            elif re.search(r'[╔╗╚╝║═]', text):  # Simple check for box drawings
                                visualizations.append({'cell_index': idx, 'type': 'ascii_art', 'content': text})
                        else:
                            logging.error(f"Unexpected type for text visualization: {type(text)}")
    return visualizations

def create_notebook_json(cells):
    notebook_data = dict()

    notebook_data.update({"markdown_outputs": extract_markdown_outputs(cells)})
    notebook_data.update({"images": extract_images(cells)})
    notebook_data.update({"code_output_tables": extract_code_output_tables(cells)})
    notebook_data.update({"json_html_outputs": extract_json_html_outputs(cells)})
    notebook_data.update({"file_paths_and_links": extract_file_paths_and_links(cells)})
    notebook_data.update({"multimedia_outputs": extract_multimedia_outputs(cells)})
    notebook_data.update({"interactive_plots": extract_interactive_plots(cells)})
    notebook_data.update({"text_visualizations": extract_text_visualizations(cells)})
    return notebook_data

def process_notebook(example):
    try:
        # Load the notebook content
        notebook_content = json.loads(example['content'])
        if int(notebook_content['nbformat']) != 4:
            if 'worksheets' not in notebook_content:
                logging.error("Notebook does not contain 'worksheets' key")
                print(str(notebook_content)[:200])
                example['visual_output'] = []
                return example
            worksheets = notebook_content['worksheets']
            worksheet_outputs = []
            for worksheet in worksheets:
                cells = worksheet['cells']
                outputs = create_notebook_json(cells)
                worksheet_outputs.append(json.dumps(outputs))
            example['visual_output'] = worksheet_outputs
            return example
        else:
            # Check if 'cells' key exists
            if 'cells' not in notebook_content:
                logging.error("Notebook does not contain 'cells' key")
                print(str(notebook_content)[:200])
                example['visual_output'] = []
                return example
            if 'cells' in notebook_content:
                outputs = create_notebook_json(notebook_content['cells'])
                example['visual_output'] = [json.dumps(outputs)]
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {e}")
        example['visual_output'] = []
    except Exception as e:
        logging.error(f"Error processing notebook: {e}")
        example['visual_output'] = []
    return example

def main():
    # Load the dataset
    ds = load_dataset("bigcode/the-stack", data_dir="data/jupyter-notebook", split="train", cache_dir='./cache').select(range(200))

    processed_ds = ds.map(process_notebook).filter(lambda x: any(any(v != [] for v in json.loads(y).values()) for y in x['visual_output']))
    while True:
        try:
            processed_ds.push_to_hub("bigcode/mm-stack", "jupyter.notebook", private=True)
        except Exception as e:
            logging.error(f"Error pushing to hub: {e}")
            time.sleep(10)
    # # Set batch size and output directory
    # batch_size = 5000
    # output_dir = "processed_notebooks"
    # os.makedirs(output_dir, exist_ok=True)

    # # Find the last processed batch
    # processed_files = [f for f in os.listdir(output_dir) if f.startswith("batch_") and f.endswith(".jsonl")]
    # last_batch = max([int(f.split("_")[1].split(".")[0]) for f in processed_files]) if processed_files else 0

    # # Process batches
    # batch_num = last_batch + 1
    # for start_idx in tqdm(range(0, len(ds), batch_size), desc="Processing batches"):
    #     if batch_num <= last_batch:
    #         batch_num += 1
    #         continue

    #     batch = ds.select(range(start_idx, min(start_idx + batch_size, len(ds))))
    #     processed_batch = batch.map(process_notebook)

    #     # Filter out examples with empty visual_output
    #     filtered_batch = [example for example in processed_batch if example['visual_output']]

    #     # Write to JSONL file
    #     output_file = os.path.join(output_dir, f"batch_{batch_num}.jsonl")
    #     with open(output_file, 'w') as f:
    #         for example in filtered_batch:
    #             f.write(json.dumps(example) + '\n')

    #     batch_num += 1

    # # After processing all batches, combine JSONL files and push to Hub
    # combined_dataset = Dataset.from_json(f"{output_dir}/batch_*.jsonl")
    # combined_dataset.push_to_hub("bigcode/the-stack-ipynb-p2c", private=True)

if __name__ == "__main__":
    main()