#!/bin/python
# coding=utf-8

from flask import Flask
app = Flask(__name__)
 

@app.route('/')
def index():
    return '<h1>Flask funcionando correctamente!</h1>'


@app.route('/contacto')
def contacto():
    return '<p>Fernando Carraro Aguirre</p>'

if __name__ == '__main__':
    app.run()