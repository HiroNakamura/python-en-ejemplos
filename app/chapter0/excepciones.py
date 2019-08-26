#!/bin/python
# coding=utf-8



#ZeroDivisionError:
def division_cero():
	print "#Division por cero"
	try:
		numero = 45/0
	except ZeroDivisionError as e:
		print "No puedes dividir entre cero:"
		print e


#ValueError
def error_tipo():
	print "#Error de tipos"
	try:
		numero = float("34R")
	except ValueError as e:
		print "No es el formato correcto:"
		print e


#No existente
def funcion_no_existe():
	print "#Funcion no existe"
	try:
		noExiste("Hola")
	except:
		print "Ha ocurrido una Exception"
	finally:
		print "Ha terminado el bloque"

#Variable no definida
def variable_no_definida():
	print "#Variable no definida"
	try:
		print cadena
	except Exception as e:
		print "Ha ocurrido una Excepcion:"
		print e
	else:
		print "No ha ocurrido ninguna Excepcion"


#Archivo no existe
def archivo_no_existe():
	print "#Archivo no existe"
	try:
		file = open("noExiste.pdf","r")
	except Exception as e:
		print "El archivo no existe:"
		print e
	finally:
		print "Bloque finalizado"



#Archivo no encontrado
def archivo_no_encontrado():
	print "#Archivo no encontrado"
	try:
		file = open("noExiste.txt","r")
	except IOError as e:
		print "Archivo no encontrado: "
		print e
	finally:
		print "Fin del bloque"

#Error de nombre
def error_de_nombre():
	print "#Error de nombre"
	try:
		clase = Extractor()
	except NameError as ex:
		print "Tipo no definido:"
		print ex


#Error de valor
def error_de_valor():
	print "#Error de valor"
	try:
		dato = int("32f")
	except ValueError as valorEx:
		print "El valor es incorrecto: "
		print valorEx
	except:
		print "Otra excepcion"
	finally:
		print "Fin de bloque"





#try-except-else-finally
def excepcion_testB():
	print "try-except-else-finally"
	try:
		divide = 4/0
	except Exception as e:
		print "Ha ocurrido una excepcion: ",e
	else:
		print "Tal vez pase otra cosa"
	finally:
		print "Ha finalizado el bloque de ejecucion"


#try-except
def excepcion_testA():
	print "try-except"
	try:
		division = 9/0.0
	except Exception as e:
		print "Exception:",e
