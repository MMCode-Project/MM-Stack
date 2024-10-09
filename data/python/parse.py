import ast
import os
from datasets import load_dataset
import re
import urllib.parse

# Keywords and libraries from README.md for multimodal data
multimodal_keywords = {
    'plot': [
        'matplotlib', 'seaborn', 'plotly', 'bokeh', 'altair', 'ggplot', 'pygal', 'holoviews',
        'hvplot', 'vispy', 'chartify', 'cufflinks', 'folium'
    ],
    'table': [
        'pandas', 'csv', 'openpyxl', 'xlrd', 'xlwt', 'xlutils', 'pyexcel', 'sqlite3', 'sqlalchemy', 
        'petl', 'tablib', 'feather', 'pyarrow', 'fastparquet', 'pyhive', 'pyspark', 'dask', 'vaex', 
        'polars', 'csvkit', 'numpy', 'modin', 'datatable', 'koalas', 'ibis', 'pandasql', 
        'great_expectations', 'beautifultable', 'prettytable', 'tabulate', 'xlsxwriter', 'pyxlsb'
    ],
    'diagram': [
        'graphviz', 'networkx', 'pydot', 'pygraphviz', 'diagrams', 'pyvis', 'igraph',
        'plotly', 'dash', 'mermaid'
    ],
    'gui': [
        'tkinter', 'PyQt5', 'kivy', 'pygame', 'wx', 'PySimpleGUI', 'PySide2', 'PyGObject',
        'wxPython', 'Flexx', 'DearPyGui', 'PyGTK', 'Toga', 'Eel', 'PyQt6'
    ],
    'web': [
        'django', 'flask', 'pyramid', 'fastapi', 'tornado', 'bottle', 'cherrypy', 'aiohttp',
        'sanic', 'dash', 'streamlit', 'gradio', 'starlette', 'falcon', 'quart', 'responder'
    ],
    'image': [
        'PIL', 'cv2', 'skimage', 'imageio', 'mahotas', 'simpleitk', 'pyvips',
        'wand', 'pgmagick', 'pydicom', 'pypng', 'qrcode', 'exif', 'geopandas', 'shapely', 'fiona', 
        'pyproj', 'rasterio', 'cartopy', 'geopy', 'osmnx', 'folium', 'pycrs', 'pysal', 'geoviews', 
        'xarray', 'salem', 'pyvista', 'vtk', 'trimesh', 'open3d', 'pyrender', 'pyglet', 'moderngl', 
        'pyrr', 'pywavefront', 'meshio', 'vedo', 'pyav'
    ],
    'audio': [
        'librosa', 'pydub', 'pyaudio', 'soundfile', 'scipy', 'mutagen', 'aubio',
        'essentia', 'madmom', 'mido', 'pretty_midi', 'pyo', 'pydsm'
    ],
    'video': [
        'moviepy', 'opencv-python', 'ffmpeg', 'vidgear', 'skvideo', 'PyAV', 'imageio',
        'gizeh', 'vapory', 'scikit-video'
    ],
}


def get_multimodal_category(code):
    categories = []
    for category, libs in multimodal_keywords.items():
        if any(lib in code for lib in libs):
            categories.append(category)
    return categories

def extract_file_paths_and_links(code):
    file_paths_and_links = []

    # Define patterns for file paths and URLs, including placeholders
    file_path_pattern = r'(?:\'|")([^\'"\s]+\.(?:csv|txt|json|xlsx?|tsv|parquet|hdf5?|sav|dta|sas7bdat|mat|pkl|feather|h5|nc))(?:\'|")'
    url_pattern = r'(https?://\S+)'
    
    # Extract file paths
    file_paths = re.findall(file_path_pattern, code)
    for path in file_paths:
        if '*' not in path and '?' not in path:
            file_paths_and_links.append(path)

    # Extract URLs
    urls = re.findall(url_pattern, code)
    for url in urls:
        parsed_url = urllib.parse.urlparse(url)
        if parsed_url.path.lower().endswith(('.csv', '.txt', '.json', '.xlsx', '.xls', '.tsv', '.parquet', '.hdf', '.hdf5', '.sav', '.dta', '.sas7bdat', '.mat', '.pkl', '.feather', '.h5', '.nc')):
            file_paths_and_links.append(url)

    return file_paths_and_links

def process_py(example):
    
    example['visual_output'] = [
        'category': get_multimodal_category(example['content']),
        'file_paths_and_links': extract_file_paths_and_links(example['content'])
    ]
    return example

def main():
    ds = load_dataset("bigcode/the-stack", data_dir="data/python", split="train", cache_dir='./cache')
    # for i, example in enumerate(ds):
    #     # check if the example is a multimodal data script
    #     categories = get_multimodal_category(example['content'])
    #     files = extract_file_paths_and_links(example['content'])
    #     if "if __name__" not in example['content']: continue
    #     if categories:
    #         print(f"Category: {categories}")
    #     if files:
    #         print(files)
    #     if categories or files:
    #         print("-"*100)
    processed_ds = ds.map(process_py).filter(lambda x: x['visual_output']['category'])
    while True:
        try:
            processed_ds.push_to_hub("bigcode/mm-stack", "python", private=True)
        except Exception as e:
            logging.error(f"Error pushing to hub: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()