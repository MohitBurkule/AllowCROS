"""Flask App Project."""

from flask import Flask
app = Flask(__name__)
import urllib

@app.route('/<path:url>')
def index():
	json_data = {'Hello': 'World!'}
	webUrl = urllib.request.urlopen(url)
	data = webUrl.read()
	return data


if __name__ == '__main__':
	app.run()
