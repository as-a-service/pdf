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
    file_name = 'document' 
    input_file = '/tmp/' + file_name
    output_dir = '/tmp'
    output_file = output_dir + '/' + file_name + '.pdf'

    url = request.args.get('url', type = str)
    if not url:
        return "please provide URL of document to convert with ?url="
    
    # Download from URL
    response = requests.get(url, stream=True)
    with open(input_file, 'wb') as file:
        shutil.copyfileobj(response.raw, file)
    del response

    # Convert using Libre Office
    call('libreoffice --headless --convert-to pdf --outdir %s %s ' % (output_dir, input_file), shell=True)

    return send_file(output_file, mimetype='application/pdf')

@app.after_request
def cleanup(response):
    location = '/tmp/traces'
    if os.path.isdir(location):
        shutil.rmtree(location)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)