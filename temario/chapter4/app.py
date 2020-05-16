#!/bin/python
# coding=utf-8

from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hola():
    return 'Flask funcionando correctamente!'



if __name__ == '__main__':
    app.run()