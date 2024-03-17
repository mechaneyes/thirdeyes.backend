# Thirdeyes Backend



## Introduction

This is the the Flask API backend for the Thirdeyes music editorial drafting tool. There are multiple endpoints adding features and functionality incorporated into Thirdeyes.

### https://thirdeyes.fm/

### https://github.com/mechaneyes/thirdeyes


## Flask via Serverless Functions on Vercel

This is a hybrid Next.js + Python app that uses Next.js as the frontend and Flask as the API backend. One great use case of this is to write Next.js apps that use Python AI libraries on the backend.

## How It Works

The Python/Flask server is mapped into to Next.js app under `/api/`.

This is implemented using [`next.config.js` rewrites](https://github.com/vercel/examples/blob/main/python/nextjs-flask/next.config.js) to map any request to `/api/:path*` to the Flask API, which is hosted in the `/api` folder.

In production, the Flask server is hosted as [Python serverless functions](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python) on Vercel.

## Running Flask Server Locally

<!-- ```bash
FLASK_DEBUG=1 pip3 install -r requirements.txt && python3 -m flask --app api/flaskr --debug run -p 5328
``` -->

The Flask application is defined in the index.py file, and it's located in the api directory. The FLASK_APP environment variable is set to api.index and then run with the flask run command (here running with reloader):

```bash
export FLASK_APP=api.index; export FLASK_ENV=development; export FLASK_DEBUG=1; flask run -p 5328
```


## From the Flask Tutorial

### Blueprints and Views

https://flask.palletsprojects.com/en/2.3.x/tutorial/views/

A view function is the code you write to respond to requests to your application. Flask uses patterns to match the incoming request URL to the view that should handle it. The view returns data that Flask turns into an outgoing response. Flask can also go the other direction and generate a URL to a view based on its name and arguments.

