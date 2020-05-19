#!/bin/python
# coding=utf-8


from archivos import *
from clases import *
from tuplas import *
from listas import *
from diccionarios import *


def suma(x, y):
    return x + y

def entrada():
	print("Suma: ",suma(int(input("x: ")),int(input("y: ")))

def metodo():
	pass

def decir_hola():
    print("Buongiorno, bambina!!")
    
def tam_cadena(cadena):
    print("El tamaño de la cadena[",cadena,"] es: ")
    return len(cadena)


def mockTestB():
    print("Tupla:\n\t",get_tupla())
    get_other_tupla()
    funciones_lista()
    funciones_tupla()
    funciones_diccionario()
    lista = [32,65,87,201,302,604,703,832,991]
    print("Lista: ",lista)
    print("Pares: ",get_pares(lista))
    print("Impares: ",get_impares(lista))
    print("Ficheros .py:")
    listar_ficheros()
    nombres = ['ana','fernando','miguel','laura','juana','hortencia',' ']
    print(nombres)
    print(listar_capitalize(nombres))


def mockTestA():
	print("Clases:")
	tipo = Tipo()
	print("Tipo es de tipo: ",type(tipo))
	tipo.nombre = "Tomas"
	tipo.apellido = "Alcantara"
	print("Nombre: ",tipo.nombre,"",tipo.apellido)
	tipo.edad = 2019-1978
	print("Edad: ",tipo.edad," años ")
	tipo.libros = ['El general no tiene quien le escriba','La hija del canibal','El tablero de Flandes']
	print("Libros:")
	for libro in tipo.libros:
		print(libro)
	

def ver_numero(numero):
	resultado,suma,numeroTmp = "",0,""
	if numero != " ":
		for num in numero:
			suma = suma + int(num)
	resultado = str(suma)
	if len(resultado) >= 2:
		resultado = ver_numero(resultado)
	return resultado


def mockTestC():
	lista = ["45","543","82","902","98","111","109","35"]
	for item in lista:
		print(item,":",ver_numero(item))
	print("")
	poner_quitar_item()


def mockTestD():
	numero = 32
	print(eval(str(numero)+"*2"))
	print(eval("32 ** 2"))
	numero = 21
	print(eval("numero + 2"))
	print(eval("numero ** 2"))
	code = compile("5 + 4", "<string>", "eval")
	print(eval(code))





def main():
	mockTestA()
	mockTestD()


if __name__ == '__main__':
    main()
