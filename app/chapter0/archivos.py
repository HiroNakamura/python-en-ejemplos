#!/bin/python
# coding=utf-8


import os
import csv



def leer_archivo():
	os.chdir(r'/home/fernando/Documentos/testRepositories/python-en-ejemplos/app/chapter0')
	arch = open('datos.csv')
	print("Ruta: ",open("datos.csv","r"))
	try:
		if open("datos.csv","r"):
			print("Parece que el archivo existe")
	except IOError as e:
		print("Error: ",e)

	try:
		file = open("datos.csv","r")
		print(type(file))
		print("Contenido:",file.readlines())
	except IOError as e:
		print("Error: ",e)


def lectura_archivo():
	print("Leer archivo:")
	os.chdir(r'/home/fernando/Documentos/testRepositories/python-en-ejemplos/app/chapter0')
	arch = open('datos.csv','r')
	try:
		if arch:
			print("Archivo existe:")
			print(arch)
	except IOError as e:
		print("Error: ",e)
	finally:
		lineas = [linea for linea in arch]
		print("Contenido:")
		print(lineas)
		print("Linea 1:")
		print(lineas[1])
		print("Linea 2:")
		print(lineas[2])
		print("")
		print(lineas[1].strip())
		print(lineas[1].strip().split(','))
		print(lineas[2].strip())
		print(lineas[2].strip().split(','))

		

def get_funciones_csv():
	print("Funciones csv:")
	print(dir(csv))
	print("")
	os.chdir(r'/home/fernando/Documentos/testRepositories/python-en-ejemplos/app/chapter0')
	arch = open('datos.csv','r')
	try:
		if arch:
			print("Archivo existe")
			reader = csv.reader(arch)
			header = next(reader)
			data = [row for row in reader]
			print("Header: ",header)
			print("Datos: ",data)
	except IOError as e:
		print("Error: ",e)
	finally:
		print("Final de bloque")


