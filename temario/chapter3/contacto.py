#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Fer Carraro
@2020
'''


class Contacto(object):
	def __init__(self,id, nombre, apellidos, email):
		self.id = id 
		self.nombre = nombre
		self.apellidos = apellidos
		self.email = email

	def __repr__(self):
		return str(self.__dict__)


	def __str__(self):
	 return "Contacto{ nombre: "+self.nombre +", apellidos: "+self.apellidos+", email: "+self.email+"}"


class Cliente(Contacto):
	pass






file = open("datos.txt","r")
existe = False


def get_contacto():
	lista = []
	contactos = [] 
	tmp = None
	clave, email, apellidos, nombre = None, None, None, None
	global file 
	try:
		existe = True if file != None else False
	except IOError as error:
		print("Ha ocurrido una excepcion al abrir el archivo:")
		print(error)
	finally:
		if existe:
			for linea in file:
				lista.append(linea)

	print("No. registros: ",len(lista))
	print("Llenando...\n")
	if len(lista) > 0:
		print(lista)
		print("")
		for i in lista:
			tmp = i.split(" ")
			print(">> ",tmp)
			clave = tmp[0]
			email = tmp[1]
			apellidos = tmp[2]
			nombre = tmp[3]
			contacto = Contacto(clave,nombre,apellidos,email)
			contactos.append(contacto)
	print("Contactos:")
	print(contactos)
	print("Hecho")


def main():
   get_contacto()	

if __name__ == '__main__':
	main()
