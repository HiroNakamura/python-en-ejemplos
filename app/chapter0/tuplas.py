#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime


def get_tupla():
    tupla = () #tupla = tuple()
    tupla = tupla + (1,)
    tupla = tupla + (2,)
    tupla = tupla + (3,4,5)
    return tupla #(1,2,3,4)


def get_other_tupla():
	tupla = tuple()
	tupla = tupla + ('Hola',)
	tupla = tupla + ('Mundo','Mundial',)
	tupla = tupla + (True, None,'X',chr(32),str(32),int("21"))
	otra = (None, False,float("2.43"), 1,2,3,3,4,object)
	iguales = "No son iguales" if tupla == otra else "No son iguales"
	print "Tupla A: ",tupla 
	print "Tupla B: ",otra
	print iguales 
	proveedor = (datetime.datetime.now(), "Servicios Informaticos Saavedra","555-212-321",True, None)
	print "Proveedor es de tipo: ",type(proveedor)
	fecha = proveedor[0]
	nombre = proveedor[1]
	telefono = proveedor[2]
	disponible = "Disponible" if proveedor[3] == True else "No esta disponible"
	web = "No tiene pagina web " if proveedor[4] == None else "Su pagina web es "+proveedor[4]
	print "Fecha: ",fecha
	print "Nombre: ",nombre
	print "Telefono: ",telefono 
	print disponible
	print web
	
	
def funciones_tupla():
	print "Funciones tupla:"
	print dir(tuple())