#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import *


hecho = ''

def main():
    global hecho
    hecho = 'Terminado.'
    try:
        print("Conectandonos a la BD 'mensajes'...")
        connect('mensajes')
        print("Nos hemos conectado!!")
    except TypeError as error:
        hecho = 'Ha ocurrido un error: '+str(error)
    finally:
        print(hecho)


if __name__ == '__main__':
    main()