#!/bin/python
# coding=utf-8

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
	print "\n\t*** Variables en Python ***"
	print "Entero = ",entero
	print "Caracter = ",character
	print "Cadena = ",cadena
	print "Booleana = ",booleana #False
	print "Constante global: ",TAM
	print "Variable nula: ",nula
	print "Variable if: ",variable
	
	
def get_type():
	global TAM
	print "#Obteniendo tipos:"
	entero = 33
	character = 'A'
	cadena = str("Python for Beginners")
	booleana = 34 > 3 #True
	booleana = not booleana #False
	nula = None
	variable = "Hola" if "A" in "AEIOU" else "Ciao"
	print "Entero = ",type(entero)
	print "Caracter = ",type(character)
	print "Cadena = ",type(cadena)
	print "Booleana = ",type(booleana) #False
	print "Constante global: ",type(TAM)
	print "Variable nula: ",type(nula)
	print "Variable if: ",type(variable)
	
	
