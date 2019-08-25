#!/bin/python
# coding=utf-8

def excepcion_testB():
	try:
		import noExiste()
	except Exception as e:
		print "Ha ocurrido una excepcion: ",e
	else:
		print "Tal vez pase otra cosa"
	finally:
		print "Ha finalizado el bloque de ejecucion"


def excepcion_testA():
	try:
		import noExiste()
    except e:
       print "Ha ocurrido una excepcion: ",e
