# Django Framework

Es un framework ridículamente fácil de configurar para crear aplicaciones web con Python.

## ¿Tengo Django instalado?

Es necesario tener **Django Framework** instalado:

```
$ python
>>> import django
>>> print(django.get_version())
3.0.6
```


```
$ pip list

#Salida
Django   3.0.6

```


En caso de no tenerlo instalado:
```
#Linux
$ python -m pip install Django  o
$ pip install Django

#Windows
$ python -m pip install Django o
$ pip install Django

```

Otra forma:
```
$ pip  install virtualenv
$ mkdir dev
$ cd dev
$ ls
$ pwd
$ mkdir newenv
$ cd newenv
$ virtualenv .
$ .\Scripts\activate
$ pip install django
$ pip freeze
$ .\Scripts\deactivate
$ .\Scripts\activate
```


## Creando proyecto Django

Creamos proyecto:

```
$ django-admin startproject proyecto
$ cd proyecto
```

Creamos aplicación:

```
$ python manage.py startapp PTarot
$ python manage.py makemigrations PTarot
$ python manage.py migrate PTarot
$ python manage.py migrate
```

Crear superusuario:

```
$ python manage.py createsuperuser
#Se te pedirá un nombre de usuario, correo electrónico y la clave de usuario.

#Migramos (para sincronizar los cambios y creación de la BD)

$ python manage.py migrate
```


Ejecutamos proyecto:
```
$ python manage.py runserver
```


Abrimos el navegador en: 

[http://localhost:8000/index](http://localhost:8000/index)






















Enlaces:

* [Django Framework](https://www.djangoproject.com/)
