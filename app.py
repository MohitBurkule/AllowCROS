"""Flask App Project."""

from flask import Flask,request
app = Flask(__name__)
import urllib

@app.route('/<path:url>')
def index(url):
	req = urllib.request.Request(url, headers=request.headers)
	webUrl = urllib.request.urlopen(req, timeout=10)
	data = webUrl.read()
	return data


if __name__ == '__main__':
	app.run()
