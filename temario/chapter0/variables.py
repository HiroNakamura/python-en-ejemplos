#!/bin/python
# coding=utf-8


class Tipo:
	pass

TAM = 100

def funcion_variables():
	global TAM
	entero = 33
	character = 'A'
	cadena = str("Python for Beginners")
	booleana = 34 > 3 #True
	booleana = not booleana #False
	nula = None
	variable = "Hola" if "A" in "AEIOU" else "Ciao" 
	tipo = Tipo()
	print("\n\t*** Variables en Python ***")
	print("Entero = ",entero)
	print(type(entero))
	print("Caracter = ",character)
	print(type(character))
	print("Cadena = ",cadena)
	print(type(cadena))
	print("Booleana = ",booleana) #False
	print(type(booleana))
	print("Constante global: ",TAM)
	print(type(TAM))
	print("Variable nula: ",nula)
	print(type(nula))
	print("Variable if: ",variable)
	print(type(variable))
	print("Tipo: ",tipo)
	print("Tipo: ",type(tipo))
	
	
	
def get_type():
	global TAM
	print("#Obteniendo tipos:")
	entero = 33
	character = 'A'
	cadena = str("Python for Beginners")
	booleana = 34 > 3 #True
	booleana = not booleana #False
	nula = None
	variable = "Hola" if "A" in "AEIOU" else "Ciao"
	print("Entero = ",entero,", tipo: ",type(entero))
	print("Caracter = ",character,", tipo: ",type(character))
	print("Cadena = ",cadena,", tipo: ",type(cadena))
	print("Booleana = ",booleana,", tipo: ",type(booleana)) #False
	print("Constante global: ",TAM,", tipo: ",type(TAM))
	print("Variable nula: ",nula,", tipo: ",type(nula))
	print("Variable if: ",variable,", tipo: ",type(variable))
	
	
def main():
	get_type()
	funcion_variables()


if __name__ == '__main__':
    main()