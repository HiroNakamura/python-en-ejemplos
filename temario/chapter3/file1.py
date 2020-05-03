#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os

'''
Fer Carraro
@2020
'''

def renombrar_archivo(archivo):
	renombrado = "El archivo "+archivo+" ha sido renombrado"
	try:
		os.rename(archivo,"renombrado.txt")
	except TypeError as error:
		print("Ha ocurrido un error: ",error)
		renombrado = "No se pudo reonmbrar el arhivo"
	finally:
		print(renombrado)



def get_archivo():
	msg = "Existe el archivo"
	print("Manejo de archivos:")
	try:
		file = open("datos.txt","r")
		existe = True if file != None else False
	except IOError as error:
		print(error)
		existe = False
		msg = "No existe el archivo"
	finally:
		print(msg)
		if existe:
			print("Contenido:")
			for line in file:
				print(line)


def main():
	get_archivo()
	renombrar_archivo("informe.txt")


if __name__ == '__main__':
	main()