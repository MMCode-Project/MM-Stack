import re
import urllib.parse

def get_multimodal_category(code, keywords):
    categories = dict()
    for category, libs in keywords.items():
        categories[category] = None
        if any(lib in code for lib in libs):
            categories[category] = {lib for lib in libs if lib in code}
    return categories

def extract_file_paths_and_links(code, file_extensions):
    file_paths_and_links = []

    # Define patterns for file paths and URLs, including placeholders
    file_path_pattern = r'(?:\'|")([^\'"\s]+\.(?:' + '|'.join(ext[1:] for ext in file_extensions) + r'))(?:\'|")'
    url_pattern = r'(https?://\S+)'
    
    # Extract file paths
    file_paths = re.findall(file_path_pattern, code)
    for path in file_paths:
        if '*' not in path and '?' not in path:
            file_paths_and_links.append(path)

    # Extract URLs
    urls = re.findall(url_pattern, code)
    for url in urls:
        try:
            parsed_url = urllib.parse.urlsplit(url)
            if parsed_url.path.lower().endswith(tuple(file_extensions)):
                file_paths_and_links.append(url)
        except Exception as e:
            pass

    return file_paths_and_links

def process_code(example, keywords, file_extensions):
    example['visual_output'] = {
        'category': get_multimodal_category(example['content'], keywords),
        'file_paths_and_links': extract_file_paths_and_links(example['content'], file_extensions)
    }
    return example