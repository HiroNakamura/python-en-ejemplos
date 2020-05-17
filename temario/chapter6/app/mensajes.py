#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import *
from bson.objectid import ObjectId

connect('mensajes')


class Mensajes(Document):
    id = ObjectId()
    idioma = StringField(max_length = 5,required = True)
    mensaje = StringField(required = True)


def main():
    hecho = 'Hecho. Documento guardado.'
    try:
        mensajes = Mensajes(
            id = ObjectId(),
            idioma = 'es_ES',
            mensaje = 'Morituri te salutan').save()
        print(mensajes)
    except NameError as error:
        hecho = 'Ha ocurrido un error: '+str(error)
    finally:
        print(hecho)


if __name__ == '__main__':
    main()