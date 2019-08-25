#!/bin/python
# coding=utf-8

from PyZenity import InfoMessage


MENSAJE = "Bienvenido a Python for Beginners"

def get_mensaje():
	global MENSAJE
	InfoMessage(MENSAJE)
