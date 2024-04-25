import os
import shutil
from css_html_js_minify import process_single_js_file, process_single_css_file, js_minify, css_minify

process_single_js_file('src/script.js', overwrite=False)
process_single_css_file('src/style.css', overwrite=False)

js_minify('var i = 1; i += 2 ;\n alert( "hello  "  ); //hi')
# 'var i=1;i+=2;alert("hello  ");'
css_minify('body {width: 50px;}\np {margin-top: 1em;/* hi */  }', comments=False)
# '@charset utf-8;body{width:50px}p{margin-top:1em}'

shutil.copyfile("src/script.min.js", "dist/script.js")
shutil.copyfile("src/style.min.css", "dist/style.js")
os.remove("src/script.min.js")
os.remove("src/style.min.css")