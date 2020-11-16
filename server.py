#!/bin/python3
# server.py

from flask import Flask, render_template, send_file, request
import os

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route("/")
def hello():
  return "Howdy World!"

# @app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask on Docker Config</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")

# def main():
#     app.run(debug=args.debug, host='0.0.0.0', port=args.port)

if __name__ == "__main__":
    # app.run()
    app.run(debug=true) #debug also allows for executing code, so take off before production
    # app.run(host = 0.0.0.0) # makes public, opens to users executing code on computer
