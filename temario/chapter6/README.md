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
```python
from mongoengine import *

#Creamos una conexión a una base de datos llamada 'mibase'
connect('mibase')
```

## Crear y cerrar conexión 
```python
from mongoengine import connect

def main():
    mensajes = connect('mibase', host='localhost', port=27017)
    mensajes.close()

if __name__ == "__main__":
    main()
    
```

## Crear clase/documento
```python
from mongoengine import *
from bson.objectid import ObjectId

connect('mensajes')

class Mensajes(Document):
    id = ObjectId()
    idioma = StringField(max_length = 5,required = True)
    mensaje = StringField(required = True)

```

## Obtener documento
```python
from mongoengine import *
from bson.objectid import ObjectId

connect('mensajes')

class Mensajes(Document):
    id = ObjectId()
    idioma = StringField(max_length = 5,required = True)
    mensaje = StringField(required = True)
    

mensaje = Mensajes.objects(idioma='it_IT').get()
print(mensaje)

```




Enlaces:
* [MongoEngine](http://mongoengine.org/)
* [MongoEngine :: Python](https://github.com/MongoEngine/mongoengine)
* [MongoDB & Python](https://pythonise.com/series/mongodb-and-python/mongodb-python-mongoengine-pt1)
* [FreeMongoDbCourse](https://freemongodbcourse.com/)
