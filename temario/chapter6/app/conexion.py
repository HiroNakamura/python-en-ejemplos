#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import *


hecho = ''

def main():
    global hecho
    hecho = 'Terminado. Conexion cerrada'
    conexion = None
    try:
        print("Conectandonos a la BD 'mensajes'...")
        conexion = connect('mensajes')
        print("Nos hemos conectado!!")
    except TypeError as error:
        hecho = 'Ha ocurrido un error: '+str(error)
    finally:
        conexion.close()
        print(hecho)
        


if __name__ == '__main__':
    main()