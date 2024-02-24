from flask import Flask
app = Flask(__name__)

@app.route("/api/web-explorer")
def hello_world():
    return "<p>Hello, World!</p>"