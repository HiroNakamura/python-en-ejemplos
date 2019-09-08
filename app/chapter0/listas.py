#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os



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


def funciones_lista():
    print "Funciones lista:"
    print dir(list())


def get_pares(lista):
    pares = []
    if len(lista) > 0:
        for item in lista:
            if item%2==0:
                pares.append(item)

    return pares


#Usando comprensiones
def get_impares(lista):
    impares = []
    if len(lista) < 0:
        return []
    else:
        impares = [item for item in lista if item % 3 == 0]
        return impares


def listar_ficheros():
    ficheros_python = [f for f in os.listdir('.') if f.endswith('.py') and f.startswith('f')]
    print ficheros_python



def listar_capitalize(lista):
    capitalize = list()
    if len(lista) > 0:
        capitalize = [item.title() for item in lista if item !=' ']
    return capitalize



