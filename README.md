# Potrace as a service

A simple web service that traces the given bitmap image into an SVG file. 

Run with `docker run -p 8080:8080 gcr.io/steren-demo/trace`

### URL parameters:

* `input`: URL of the image to trace.

## Running the server locally

* Build with `docker build . -t trace`
* Start with `docker run -p 8080:8080 trace`
* Open in your browser at `http://localhost:8080/?url=https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png`

## Deploy to your server

The following container image always reflects the latest version of the `master` branch of this repo: `gcr.io/steren-demo/trace`

## TODO

* also accept images via POST requests.
