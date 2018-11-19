import os
import shutil

from flask import Flask
from flask import request
from flask import abort
from flask import send_file
from subprocess import call

app = Flask(__name__)

@app.route('/')
def trace():
    bmp_location = '/tmp/bmp/'
    traces_location = '/tmp/traces/'
    svg_name = 'trace'
    svg_filename = traces_location + svg_name + '.svg'

    input_image_file = 'head-orig3.png'
    bmp_image_file = bmp_location + 'temp.bmp'

    if not os.path.exists(bmp_location):
        os.makedirs(bmp_location)
    if not os.path.exists(traces_location):
        os.makedirs(traces_location)

    # Convert image to .bmp
    call('convert %s %s' % (input_image_file, bmp_image_file), shell=True)
    
    # Trace .bmp to .svg
    call('potrace %s -o %s --svg' % (bmp_image_file, svg_filename), shell=True)
    
    return send_file(svg_filename, mimetype='image/svg+xml')

@app.after_request
def cleanup(response):
    location = '/tmp/traces'
    if os.path.isdir(location):
        shutil.rmtree(location)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)