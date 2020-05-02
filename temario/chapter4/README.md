# Flask

Un microframework para desarrollar aplicaciones web con Python.



**app.py**
```
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
```


```
$ env FLASK_APP=hello.py flask run
 * Serving Flask app "hello"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


Enlace:

* [Sitio oficial de Flask](https://flask.palletsprojects.com/en/1.1.x/)