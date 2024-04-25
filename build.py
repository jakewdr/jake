import os
import shutil
import pathlib
from css_html_js_minify import process_single_js_file, process_single_css_file, js_minify, css_minify

def pathLeaf(path) -> str:
    return str(os.path.split(path)[1])

files = [str(entry).replace(os.sep, '/') for entry in pathlib.Path("src/").iterdir()]

for file in files:
    if ".js" in file:
        process_single_js_file(file, overwrite=False)
        shutil.copyfile(file.replace(".js",".min.js"), f"dist/{pathLeaf(file)}")
        os.remove(file.replace(".js",".min.js"))
    if ".css" in file:
        process_single_css_file(file, overwrite=False, sort=True)
        shutil.copyfile(file.replace(".css",".min.css"), f"dist/{pathLeaf(file)}")
        os.remove(file.replace(".css",".min.css"))