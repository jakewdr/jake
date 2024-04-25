import os
import shutil
from css_html_js_minify import process_single_js_file, process_single_css_file, js_minify, css_minify

process_single_js_file('src/script.js', overwrite=False)
process_single_css_file('src/style.css', overwrite=False, sort=True)

shutil.copyfile("src/script.min.js", "dist/script.js")
shutil.copyfile("src/style.min.css", "dist/style.css")
os.remove("src/script.min.js")
os.remove("src/style.min.css")