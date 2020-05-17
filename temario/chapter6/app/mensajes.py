#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import *
from bson.objectid import ObjectId

connect('mensajes')


class Mensajes(Document):
    id = ObjectId()
    idioma = StringField(max_length = 5,required = True)
    mensaje = StringField(required = True)



def get_mensajes():
    print("Mensajes:")
    mensajes = Mensajes.objects()
    if mensajes != None:
        for mensaje in mensajes:
            print("Id: ",mensaje.id)
            print("Idioma: ",mensaje.idioma)
            print("Mensaje: ",mensaje.mensaje)
    else:
        print("No hay mensajes")
        


def crear(idioma, mensaje):
    hecho = 'Hecho. Documento guardado.'
    try:
        mensajes = Mensajes(
            id = ObjectId(),
            idioma = idioma,
            mensaje = mensaje).save()
        print(mensajes)
    except NameError as error:
        hecho = 'Ha ocurrido un error: '+str(error)
    finally:
        print(hecho)


def get_objeto(myobj):
    return "Mensaje{\n\tid:"+str(myobj.id)+",\n\tidioma:" +myobj.idioma + ",\n\tmensaje: "+myobj.mensaje+"\n}\n"


def main():
    crear('de_DE','Guten Tag!')
    get_mensajes()
    italiano = None
    try:
        italiano = Mensajes.objects(idioma='it_IT').get()
    except TypeError as error:
        italiano = "Error ocurrido: "+str(error)
    finally:
        print("Lo que se ha obtenido es:")
        print(get_objeto(italiano))


if __name__ == '__main__':
    main()