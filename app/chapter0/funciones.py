#!/bin/python
# coding=utf-8


from clases import *
from tuplas import *

def metodo():
    pass

def decir_hola():
    print "Buongiorno, bambina!!"
    
def tam_cadena(cadena):
    print "El tamaño de la cadena[",cadena,"] es: "
    return len(cadena)



def mockTestB():
	print "Tupla:\n\t",get_tupla()
	get_other_tupla()


def mockTestA():
	print "Clases:"
	tipo = Tipo()
	print "Tipo es de tipo: ",type(tipo)
	tipo.nombre = "Tomas"
	tipo.apellido = "Alcantara"
	print "Nombre: ",tipo.nombre,"",tipo.apellido
	tipo.edad = 2019-1978
	print "Edad: ",tipo.edad," años "
	tipo.libros = ['El general no tiene quien le escriba','La hija del canibal','El tablero de Flandes']
	print "Libros:"
	for libro in tipo.libros:
		print libro
	