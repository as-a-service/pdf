# "to PDF" as a service

A simple web service that transforms the given document into a PDF file. 

Run with `docker run -p 8080:8080 gcr.io/as-a-service-dev/pdf`

### URL parameters:

* `input`: URL of the document to transform.

## Running the server locally

* Build with `docker build . -t pdf`
* Start with `docker run -p 8080:8080 pdf`
* Open in your browser at `http://localhost:8080/?url=http://homepages.inf.ed.ac.uk/neilb/TestWordDoc.doc`

## Deploy to your server

The following container image always reflects the latest version of the `master` branch of this repo: `gcr.io/as-a-service-dev/pdf`

## Deploy to Google Cloud

[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.svg)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/as-a-service/pdf.git)

Or use `gcloud beta run deploy --image gcr.io/as-a-service-dev/pdf`
