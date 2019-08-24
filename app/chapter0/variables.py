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
	print "\n\t*** Variables en Python ***"
	print "Entero = ",entero
	print "Caracter = ",character
	print "Cadena = ",cadena
	print "Booleana = ",booleana #False
	print "Constante global: ",TAM
	print "Variable nula: ",nula
