#!/usr/bin/env python3

from a2wsgi import ASGIMiddleware
from fastapi import FastAPI
from wsgiref.handlers import CGIHandler

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World 👋"}


# 1. provide it as wsgi application
wsgi_application = ASGIMiddleware(app)

# 2. use wsgi handler to run as cgi
CGIHandler().run(wsgi_application)
