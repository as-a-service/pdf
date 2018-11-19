import os
import shutil
import requests

from flask import Flask
from flask import request
from flask import abort
from flask import send_file
from subprocess import call

app = Flask(__name__)

@app.route('/')
def trace():
    input_image_file = '/tmp/input'
    bmp_image_file = '/tmp/temp.bmp'
    svg_filename = '/tmp/trace.svg'

    url = request.args.get('url', type = str)   
    if not url:
        return "please provide URL of image to trace with ?url="

    # Download image from URL
    response = requests.get(url, stream=True)
    with open(input_image_file, 'wb') as file:
        shutil.copyfileobj(response.raw, file)
    del response

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