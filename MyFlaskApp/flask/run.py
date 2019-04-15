#!/usr/bin/env python3
import os
from flask import Flask

def keymaker(app,filename='secret_key'):
	pathname=os.path.join(app.instance_path,filename)
	try:
		app.config['SECRET_KEY'] = open(pathname,'rb').read()
	except IOError:
		parent_directory = os.path.dirname(pathname)
		if not os.path.isdir(parent_directory):
			os.system('mkdir -p {}'.format(parent_directory))
		os.system('head -c 24 /dev/urandom > {}'.format(pathname))
		app.config['SECRET_KEY'] = open(pathname,'rb').read()

app = Flask(__name__)         
keymaker(app)

@app.route("/")
def dashboard():
    return "Hello, World"

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=80,debug=True)
