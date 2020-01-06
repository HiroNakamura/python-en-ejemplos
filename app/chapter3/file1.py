#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Fer Carraro
@2019
'''


def get_archivo():
	msg = "Existe el archivo"
	print "Manejo de archivos:"
	try:
		file = open("datos.txt","r")
		existe = True if file != None else False
	except IOError as error:
		print error
		existe = False
		msg = "No existe el archivo"
	finally:
		print msg
		if existe:
			print "Contenido:"
			for line in file:
				print line


def main():
	get_archivo()


if __name__ == '__main__':
	main()