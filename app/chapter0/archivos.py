#!/bin/python
# coding=utf-8


import os


def leer_archivo():
	os.chdir(r'/home/fernando/Documentos/testRepositories/python-en-ejemplos/app/chapter0')
	arch = open('datos.csv')
	print "Ruta: ",open("datos.csv","r")
	try:
		if open("datos.csv","r"):
			print "Parece que el archivo existe"
	except IOError as e:
		print "Error: ",e

	try:
		file = open("datos.csv","r")
		print type(file)
		print "Contenido:",file.readlines()
	except IOError as e:
		print "Error: ",e
