"""Flask App Project."""

from flask import Flask,request
app = Flask(__name__)
import urllib

@app.route('/<path:url>')
def index(url):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	'Accept-Encoding': 'none',
	'Accept-Language': 'en-US,en;q=0.8',
	'Connection': 'keep-alive',
	'X-JAVASCRIPT-ENABLED': 'false'}
	req = urllib.request.Request(url, headers=hdr)
	webUrl = urllib.request.urlopen(req, timeout=10)
	data = webUrl.read()
	return data


if __name__ == '__main__':
	app.run()
