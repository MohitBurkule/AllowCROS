"""Flask App Project."""

from flask import Flask
app = Flask(__name__)
import urllib

@app.route('/<path:url>')
def index(url):
	webUrl = urllib.request.urlopen(url, headers={'User-Agent': 'Mozilla/5.0'})
	data = webUrl.read()
	return data


if __name__ == '__main__':
	app.run()
