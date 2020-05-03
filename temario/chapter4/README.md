# Flask

Un microframework para desarrollar aplicaciones web con Python.


Instalando ```env```
```
# macOS/Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv env

# Windows
python -m venv env
```

Instalando **Flask**
```
# macOS/Linux
pip3 install flask

# Windows
pip install flask
```

## Hola mundo en Flask

```app.py```

```python
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "Mundo")
    return f'Hola, {escape(name)}!'    
```

Ejecutar:

```
$ env FLASK_APP=hello.py flask run
 * Serving Flask app "hello"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```


##  Modificando el archivo
```python
from flask import Flask
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content
```

## Creando proyecto con Flask

1. Creamos un directorio llamado proyectoFlask.
```
$ mkdir proyectoFlask
```

2. Creamos un entorno virtual (usando el directorio anteriormente creado).
```
$ virtualenv proyectoFlask
$ cd proyectoFlask
```

3. Activamos el entorno virtual. 

En Windows:

```
$ .\Scripts\activate
```

En Linux:
```
$ activate
```
4. Instalamos Flask.
```
$ pip install Flask
```

5. Comprobamos su instalación.
```
$ pip list
$ pip freeze
```

6. Creamos un archivo llamado app.py
```
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hola():
    return 'Flask funcionando correctamente!'
```

7. Colocamos la variable FLASK_APP. En Windows:
```
$ set FLASK_APP=app.py
```
En Linux:
```
$ export FLASK_APP=app.py
```

8. Ejecutamos la aplicación y abrimos el navegador en http://localhost:5000
```
$ flask run
```


Enlace:

* [Flask pallets](https://flask.palletsprojects.com/en/1.1.x/)
* [Full Stack Python](https://www.fullstackpython.com/flask.html)
