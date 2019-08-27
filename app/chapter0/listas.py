#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Lista
def get_lista():
    lista = list() # tambien lista = []
    #agregar elemento
    lista.append('A')
    lista.append('B')
    lista.append('C')
    lista.append(None)
    lista.append(str('123'))
    lista.append(True)
    return lista
    
    
#Llenar lista
def get_lista_add(item):
    lista = []
    if  not item == None:
        lista.append(item)
    return lista
