#!/bin/python
# coding=utf-8


from PyZenity import ErrorMessage
from PyZenity import GetDirectory
from PyZenity import InfoMessage
from PyZenity import Notification 


#GetDirectory
def get_directorio():
	try:
		directorio = GetDirectory(multiple=False,selected=None,sep=None)
		InfoMessage('Tu selección es: '+str(directorio),width=200,height=150,title='Directorio seleccionado')
		Notification(text='Tu selección es: '+str(directorio))
	except Exception as ex:
		ErrorMessage('Ha ocurrido una excepcion: '+str(e))
	finally:
		print "Ha finalizado el bloque"