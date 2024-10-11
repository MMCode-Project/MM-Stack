# R-specific keywords
R_KEYWORDS = {
    'plot': [
        'ggplot2', 'plotly', 'lattice', 'ggvis', 'rbokeh', 'highcharter', 'leaflet',
        'rgl', 'rayshader', 'scatterplot3d', 'plotrix', 'rCharts', 'googleVis'
    ],
    'table': [
        'data.table', 'dplyr', 'tidyr', 'readr', 'readxl', 'openxlsx', 'rio', 'RSQLite',
        'DBI', 'RMySQL', 'RPostgreSQL', 'feather', 'arrow', 'fst', 'sparklyr', 'dtplyr',
        'tibble', 'knitr', 'kableExtra', 'gt', 'flextable', 'formattable', 'reactable'
    ],
    'diagram': [
        'DiagrammeR', 'networkD3', 'visNetwork', 'igraph', 'ggraph', 'graphlayouts',
        'ggnetwork', 'tidygraph'
    ],
    'gui': [
        'shiny', 'shinydashboard', 'flexdashboard', 'htmlwidgets', 'RGtk2', 'gWidgets',
        'tcltk', 'RInno'
    ],
    'web': [
        'shiny', 'plumber', 'httr', 'rvest', 'xml2', 'jsonlite', 'webshot', 'RSelenium',
        'seleniumPipes'
    ],
    'image': [
        'imager', 'magick', 'EBImage', 'OpenImageR', 'raster', 'rgdal', 'sf', 'sp',
        'leaflet', 'tmap', 'ggmap', 'rayshader', 'rgl', 'plotly'
    ],
    'audio': [
        'tuneR', 'seewave', 'audio', 'warbleR', 'soundecology', 'phonTools', 'specan',
        'sonify'
    ],
    'video': [
        'av', 'animation', 'gganimate', 'transformr', 'gifski', 'magick'
    ],
}

# Python-specific keywords
PY_KEYWORDS = {
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

JL_KEYWORDS = {
    'plot': [
        'Plots', 'Gadfly', 'VegaLite', 'Makie', 'PyPlot', 'UnicodePlots', 'PlotlyJS',
        'GR', 'PGFPlotsX', 'Winston', 'GLMakie', 'CairoMakie', 'WGLMakie'
    ],
    'table': [
        'DataFrames', 'CSV', 'XLSX', 'JuliaDB', 'Tables', 'Query', 'DataFramesMeta',
        'TypedTables', 'SQLite', 'MySQL', 'PostgreSQL', 'ODBC', 'Arrow', 'Feather',
        'JLD', 'JLD2', 'HDF5', 'MAT', 'RData', 'JSON', 'YAML', 'DataStructures'
    ],
    'diagram': [
        'GraphPlot', 'NetworkX', 'LightGraphs', 'GraphRecipes', 'TikzGraphs',
        'GraphMakie', 'GraphViz'
    ],
    'gui': [
        'Gtk', 'QML', 'Blink', 'Electron', 'Escher', 'Interact', 'WebIO', 'Dash'
    ],
    'web': [
        'HTTP', 'Genie', 'Mux', 'Bukdu', 'Joseki', 'Franklin', 'JuliaWebAPI',
        'WebSockets', 'Requests', 'URIs', 'JSON3', 'XMLDict', 'EzXML'
    ],
    'image': [
        'Images', 'ImageView', 'ImageMagick', 'TestImages', 'ImageTransformations',
        'ImageFiltering', 'ImageSegmentation', 'ImageMorphology', 'ImageQualityIndexes',
        'ImageContrastAdjustment', 'ImageEdgeDetection', 'ImageFeatures', 'ImageMetadata',
        'CoordinateTransformations', 'GDAL', 'GeoArrays', 'GeoStats', 'Proj4'
    ],
    'audio': [
        'PortAudio', 'LibSndFile', 'WAV', 'FFTW', 'DSP', 'SampledSignals', 'MusicProcessing',
        'MIDI', 'AudioSchedules', 'Sonification'
    ],
    'video': [
        'VideoIO', 'FFMPEG', 'AVSPStreamFormat', 'OpenCV'
    ],
}

JS_KEYWORDS = {
    'plot': [
        'd3', 'chart.js', 'plotly', 'highcharts', 'echarts', 'c3', 'recharts', 'victory',
        'vega', 'vega-lite', 'three.js', 'vis.js', 'chartist', 'sigma.js', 'leaflet'
    ],
    'table': [
        'ag-grid', 'datatables', 'tabulator', 'handsontable', 'react-table', 'griddle',
        'vue-tables-2', 'ngx-datatable', 'papa-parse', 'xlsx', 'jspdf', 'pdfmake'
    ],
    'diagram': [
        'mermaid', 'jsplumb', 'gojs', 'jointjs', 'raphael', 'cytoscape', 'dagre',
        'vis-network', 'd3-hierarchy', 'react-flow'
    ],
    'gui': [
        'react', 'vue', 'angular', 'svelte', 'electron', 'nw.js', 'proton-native',
        'quasar', 'ionic', 'react-native', 'nativescript'
    ],
    'web': [
        'express', 'koa', 'hapi', 'fastify', 'nest', 'sails', 'meteor', 'next.js',
        'nuxt.js', 'gatsby', 'axios', 'fetch', 'socket.io', 'websocket'
    ],
    'image': [
        'jimp', 'sharp', 'canvas', 'fabric.js', 'konva', 'p5.js', 'two.js', 'paper.js',
        'pixijs', 'opencv.js', 'tesseract.js', 'face-api.js', 'tracking.js'
    ],
    'audio': [
        'howler.js', 'tone.js', 'wavesurfer.js', 'web-audio-api', 'pizzicato',
        'soundjs', 'audiojs', 'jsmediatags', 'audio-recorder-polyfill'
    ],
    'video': [
        'video.js', 'plyr', 'mediaelement', 'shaka-player', 'hls.js', 'dash.js',
        'flv.js', 'jplayer', 'videojs-contrib-hls', 'ffmpeg.js'
    ],
}

CPP_KEYWORDS = {
    'plot': [
        'gnuplot-iostream', 'matplotlib-cpp', 'plotcpp', 'sciplot', 'matplotlibcpp',
        'qcustomplot', 'plplot', 'root', 'vtk', 'qwt'
    ],
    'table': [
        'rapidcsv', 'fast-cpp-csv-parser', 'csv-parser', 'sqlite3', 'libpqxx', 'soci',
        'odb', 'sqlpp11', 'xlnt', 'libxls', 'libxlsxwriter', 'tabulate'
    ],
    'diagram': [
        'graphviz', 'ogdf', 'lemon', 'boost::graph', 'igraph', 'networkx', 'graph-tool',
        'cgal'
    ],
    'gui': [
        'qt', 'wxwidgets', 'gtkmm', 'fltk', 'imgui', 'juce', 'nana', 'sfml', 'sdl',
        'allegro', 'cegui'
    ],
    'web': [
        'cpprestsdk', 'crow', 'pistache', 'oatpp', 'drogon', 'civetweb', 'cpp-httplib',
        'beast', 'proxygen', 'wt', 'curlpp', 'libcurl'
    ],
    'image': [
        'opencv', 'cimg', 'magick++', 'vigra', 'vips', 'devil', 'freeimage', 'stb_image',
        'libjpeg', 'libpng', 'exiv2', 'tesseract'
    ],
    'audio': [
        'portaudio', 'rtaudio', 'libsndfile', 'openal', 'fmod', 'sdl_mixer', 'miniaudio',
        'libsamplerate', 'aubio', 'soundtouch'
    ],
    'video': [
        'ffmpeg', 'gstreamer', 'vlc', 'opencv', 'directshow', 'mediafoundation', 'libav',
        'mlt++', 'moviepy'
    ],
}


HTML_KEYWORDS = {
    'plot': [
        'd3.js', 'd3.min.js', 'chart.js', 'plotly.js', 'plotly-latest.min.js',
        'highcharts.js', 'echarts.min.js', 'c3.min.js', 'recharts.min.js',
        'vega.min.js', 'vega-lite.min.js', 'three.min.js', 'vis.min.js', 'chartist.min.js',
        'sigma.min.js', 'leaflet.js', 'google-charts.js'
    ],
    'table': [
        'datatables.js', 'datatables.min.js', 'tabulator.min.js', 'ag-grid.min.js',
        'handsontable.full.min.js', 'grid.min.js', 'jexcel.js', 'jspreadsheet.js',
        'slickgrid.min.js', 'papaparse.min.js', 'xlsx.full.min.js', 'jspdf.min.js', 
        'pdfmake.min.js'
    ],
    'diagram': [
        'mermaid.min.js', 'jsplumb.min.js', 'go.js', 'joint.min.js', 'raphael.min.js',
        'cytoscape.min.js', 'vis-network.min.js', 'dagre.min.js', 'flowchart.min.js'
    ],
    'gui': [
        'react.js', 'react.min.js', 'vue.js', 'vue.min.js', 'angular.js', 'angular.min.js',
        'svelte.min.js', 'jquery.min.js', 'bootstrap.min.js', 'materialize.min.js',
        'foundation.min.js'
    ],
    'image': [
        'fabric.min.js', 'konva.min.js', 'p5.min.js', 'two.min.js', 'paper.min.js',
        'pixi.min.js', 'opencv.js', 'tesseract.min.js', 'face-api.min.js',
        'tracking-min.js', 'cropper.min.js'
    ],
    'audio': [
        'howler.min.js', 'tone.min.js', 'wavesurfer.min.js', 'pizzicato.min.js',
        'sound.min.js', 'audio.min.js', 'jsmediatags.min.js', 'web-audio-api.min.js'
    ],
    'video': [
        'video.min.js', 'plyr.min.js', 'mediaelement.min.js', 'shaka-player.compiled.js',
        'hls.min.js', 'dash.all.min.js', 'flv.min.js', 'jquery.jplayer.min.js',
        'videojs-contrib-hls.min.js', 'jwplayer.js'
    ],
}



TS_KEYWORDS = {
    'plot': [
        'd3', 'chart.js', 'plotly', 'highcharts', 'echarts', 'c3', 'recharts', 'victory',
        'vega', 'vega-lite', 'three.js', 'vis.js', 'chartist', 'sigma.js', 'leaflet'
    ],
    'table': [
        'ag-grid', 'datatables', 'tabulator', 'handsontable', 'react-table', 'griddle',
        'vue-tables-2', 'ngx-datatable', 'papa-parse', 'xlsx', 'jspdf', 'pdfmake'
    ],
    'diagram': [
        'mermaid', 'jsplumb', 'gojs', 'jointjs', 'raphael', 'cytoscape', 'dagre',
        'vis-network', 'd3-hierarchy', 'react-flow'
    ],
    'gui': [
        'react', 'vue', 'angular', 'svelte', 'electron', 'nw.js', 'proton-native',
        'quasar', 'ionic', 'react-native', 'nativescript'
    ],
    'web': [
        'express', 'koa', 'hapi', 'fastify', 'nest', 'sails', 'meteor', 'next.js',
        'nuxt.js', 'gatsby', 'axios', 'fetch', 'socket.io', 'websocket'
    ],
    'image': [
        'jimp', 'sharp', 'canvas', 'fabric.js', 'konva', 'p5.js', 'two.js', 'paper.js',
        'pixijs', 'opencv.js', 'tesseract.js', 'face-api.js', 'tracking.js'
    ],
    'audio': [
        'howler.js', 'tone.js', 'wavesurfer.js', 'web-audio-api', 'pizzicato',
        'soundjs', 'audiojs', 'jsmediatags', 'audio-recorder-polyfill'
    ],
    'video': [
        'video.js', 'plyr', 'mediaelement', 'shaka-player', 'hls.js', 'dash.js',
        'flv.js', 'jplayer', 'videojs-contrib-hls', 'ffmpeg.js'
    ],
}

M_KEYWORDS = {
    'plot': [
        'CorePlot', 'Charts', 'PNChart', 'JBChartView'
    ],
    'table': [
        'UIKit', 'UITableView', 'CoreData', 'Realm'
    ],
    'diagram': [
        'DiagramKit', 'GraphKit', 'Graphviz'
    ],
    'gui': [
        'UIKit', 'AppKit', 'SpriteKit', 'SceneKit', 'QuartzCore'
    ],
    'image': [
        'UIKit', 'CoreImage', 'ImageIO', 'Photos', 'AVFoundation', 'GPUImage', 'SDWebImage'
    ],
    'audio': [
        'AVFoundation', 'AudioToolbox', 'OpenAL', 'libpd', 'TheAmazingAudioEngine'
    ],
    'video': [
        'AVFoundation', 'AVKit', 'CoreMedia', 'CoreVideo', 'GPUImage', 'VLCMediaPlayer'
    ],
}

# File extensions of multi-modal data for different languages
FILE_EXTENSIONS = {'.txt', '.rda', '.m4a', '.rtf', '.nc', '.pptx', '.hdf5', '.pkl', '.pdf', '.mov', '.ogg', '.db', '.flac', '.jld2', '.mp4', '.ogv', '.dta', '.sqlite', '.tsv', '.webp', '.rdata', '.wav', '.mp3', '.geojson', '.mat', '.sav', '.webm', '.sas7bdat', '.bin', '.jpg', '.xml', '.docx', '.yml', '.avi', '.png', '.arrow', '.csv', '.fst', '.doc', '.gif', '.ppt', '.xlsx', '.ini', '.h5', '.flv', '.rds', '.dat', '.svg', '.yaml', '.jpeg', '.aac', '.feather', '.xls', '.parquet', '.jld', '.hdf', '.json', '.h'}