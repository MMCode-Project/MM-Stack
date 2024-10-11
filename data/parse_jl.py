from datasets import load_dataset, Dataset
import logging
import time
from utils import JL_KEYWORDS, FILE_EXTENSIONS, process_code

def main():
    ds = load_dataset("bigcode/the-stack", data_dir="data/julia", split="train", cache_dir='./cache', streaming=True).take(1000)
    processed_ds = Dataset.from_generator(ds.__iter__).map(lambda x: process_code(x, JL_KEYWORDS, FILE_EXTENSIONS)).filter(lambda x: any(x['visual_output']['category'].values()))
    while True:
        try:
            processed_ds.push_to_hub("bigcode/mm-stack", "jl", private=True)
            break
        except Exception as e:
            logging.error(f"Error pushing to hub: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()