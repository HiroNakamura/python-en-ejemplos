#!/bin/python
# coding=utf-8

from PyZenity import ErrorMessage
from PyZenity import GetDirectory
from PyZenity import InfoMessage
from PyZenity import Notification
from PyZenity import GetFilename


#GetFilename
def get_archivo():
	print "#Get archivo:"
	try:
		archivo = GetFilename(multiple=True,sep='|')
		InfoMessage('Archivo seleccionado:' +str(archivo),width=200,height=150,title='Archivo seleccionado')
		print "Archivo: ",str(archivo)
	except Exception as ex:
		ErrorMessage('Ha ocurrido una excepcion: '+str(ex))
	finally:
		print "Ha finalizado el bloque"


#GetDirectory
def get_directorio():
	print "#Get directorio:"
	try:
		directorio = GetDirectory(multiple=False,selected=None,sep=None)
		InfoMessage('Tu selección es: '+str(directorio),width=200,height=150,title='Directorio seleccionado')
		Notification(text='Tu selección es: '+str(directorio))
		print "Directorio: ",str(directorio)
	except Exception as ex:
		ErrorMessage('Ha ocurrido una excepcion: '+str(e))
	finally:
		print "Ha finalizado el bloque"
