import sys
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
	return "<h1>Hello CodeIn</h1><h3>mrezkys</h3>"

if __name__ == "__main__":
	app.run(host='localhost', port=8080, debug=True)