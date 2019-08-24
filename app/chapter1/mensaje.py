#!/bin/python
# coding=utf-8

import PyZenity
#from PyZenity import InfoMessage
import os

def get_mensaje():
	print "\n*** PyZenity ***"
	print os.environ['PATH']
	#InfoMessage('Hola')
	PyZenity.InfoMessage('Usando una ventana de informacion')
	
	
