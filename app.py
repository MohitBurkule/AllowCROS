"""Flask App Project."""

from flask import Flask
app = Flask(__name__)
import urllib

@app.route('/')
def index():
	json_data = {'Hello': 'World!'}
	webUrl = urllib.urlopen("https://www.youtube.com/user/guru99com")
	data = webUrl.read()
	return data


if __name__ == '__main__':
	app.run()
