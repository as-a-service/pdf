# Potrace as a service

A simple web service that traces the given bitmap image into an SVG file. 

## How to use:

(TODO) Send the input image as POST data or its URL in the `input` URL parameter.

### URL parameters:

* `input`: URL of the image to trace. Leave empty if sending data via POST request (TODO)

## Running the server locally

* Build with `docker build . -t trace`
* Start with `docker run -p 8080:8080 trace`
* Open in your browser at `http://localhost:8080/`