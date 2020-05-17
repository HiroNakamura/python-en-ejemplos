# MongoEngine

> MongoEngine is a Document-Object Mapper (think ORM, but for document databases) for working with MongoDB from Python. It uses a simple declarative API, similar to the Django ORM.


## Instalando MongoEngine

```
$ pip install mongoengine
```

## Comprobar instalación

```
$ python
>> from mongoengine import *
>> from mongoengine import connect
>> help(connect)
```

## Crear una conexión
```java
from mongoengine import *

#Creamos una conexión a una base de datos llamada 'mibase'
connect('mibase')
```


Enlaces:
* [MongoEngine](http://mongoengine.org/)
* [MongoEngine :: Python](https://github.com/MongoEngine/mongoengine)
* [MongoDB & Python](https://pythonise.com/series/mongodb-and-python/mongodb-python-mongoengine-pt1)
