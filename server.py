# python3
# server.py

from Flask import Flask, response, request, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route("/")
# def hello():
#   return "Hello World!"

# @app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask on Docker Config</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")

def main():
    app.run(debug=args.debug, host='0.0.0.0', port=args.port)


if __name__ == "__main__":
  app.run()
