import os
import shutil
import requests

from flask import Flask, request, abort, send_file, redirect
from subprocess import call

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = set(['doc', 'docx', 'xls', 'xlsx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Convert using Libre Office
def convert_file(output_dir, input_file):
    call('libreoffice --headless --convert-to pdf --outdir %s %s ' % (output_dir, input_file), shell=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def api():
    file_name = 'document' 
    folder_name = 'convert'
    input_dir = os.path.join('/tmp', folder_name)
    input_file =  os.path.join(input_dir, file_name)
    output_dir = input_dir
    output_file = os.path.join(output_dir, file_name + '.pdf')
    
    os.mkdir(input_dir)

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'No file provided'
        file = request.files['file']
        if file.filename == '':
            return 'No file provided'
        if file and allowed_file(file.filename):
            file.save(input_file)

    if request.method == 'GET':
        url = request.args.get('url', type = str)
        if not url:
            return '''
                <!doctype html>
                <title>Convert .doc to .pdf</title>
                <h1>Convert .doc to .pdf</h1>
                <h2>Upload new File</h2>
                <form method=post enctype=multipart/form-data>
                <input type=file name=file>
                <input type=submit value=Upload>
                <h2>or point to a file online</h2>
                <p>You can provide the URL of a document to convert with the <code>url</code> query parameter.
                For example <a href="/?url=http://homepages.inf.ed.ac.uk/neilb/TestWordDoc.doc">/?url=http://homepages.inf.ed.ac.uk/neilb/TestWordDoc.doc</a></p>
                </form>
                '''
        # Download from URL
        response = requests.get(url, stream=True)
        with open(input_file, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
        del response

    convert_file(output_dir, input_file)

    return send_file(output_file, mimetype='application/pdf')

@app.after_request
def cleanup(response):
    location = '/tmp/convert'
    if os.path.isdir(location):
        shutil.rmtree(location)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)