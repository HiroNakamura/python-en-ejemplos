#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import os.path


'''
Fer Carraro
@2020
'''


def leer_contenido(ruta):
	causa = "Hecho"
	try:
		with open(ruta) as f:
			print(f.readlines())
			f.close()
	except IOError as error:
		print("No se puede acceder al archivo")
		causa = "Error: "+str(error)
	finally:
		print(causa)




def crear_archivo(ruta,modo):
	if ruta == None or ruta == "":
		ruta = "nuevo.txt"
	if modo == None or modo == "":
		modo = "x"
	try:
		file = open(ruta,modo)
	except IOError as error:
		print("Ha ocurrido un error: ",error)
	finally:
		file.close()
	print("Archivo ",file," creado y cerrado")


def eliminar_archivo(ruta):
	if os.path.isfile(ruta):
		print("Existe el archivo")
		os.remove(ruta)
		print("Archivo eliminado")
	else:
		print("El archivo que quieres eliminar no existe")



def get_diretorio(ruta):
	pass


def eliminar_directorio(ruta):
	pass


def renombrar_archivo(archivo):
	renombrado = "El archivo "+archivo+" ha sido renombrado"
	try:
		os.rename(archivo,"renombrado.txt")
	except TypeError as error:
		print("Ha ocurrido un error: ",error)
		renombrado = "No se pudo renombrar el arhivo"
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
	#get_archivo()
	#renombrar_archivo("informe.txt")
	#crear_archivo(input("Introduce nombre del archivo: "),input("Introduce modo [x-crear, w-escribir]: "))
	leer_contenido("datos.txt")


if __name__ == '__main__':
	main()
