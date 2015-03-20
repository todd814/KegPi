#!/usr/bin/python

from flask import Flask

app = Flask(__name__)
app.debug = True

# Main
@app.route('/')
def hello():
	return "Hello beer."

if __name__ == '__main__':
	app.run()