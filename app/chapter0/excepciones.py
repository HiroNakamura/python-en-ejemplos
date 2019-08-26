#!/bin/python
# coding=utf-8



def excepcion_testB():
	try:
		divide = 4/0
	except Exception as e:
		print "Ha ocurrido una excepcion: ",e
	else:
		print "Tal vez pase otra cosa"
	finally:
		print "Ha finalizado el bloque de ejecucion"


def excepcion_testA():
	try:
		division = 9/0.0
	except Exception as e:
		print "Exception:",e
