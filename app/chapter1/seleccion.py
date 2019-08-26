#!/bin/python
# coding=utf-8

from PyZenity import Question
from PyZenity import InfoMessage


#Question
def linux_instalado():
    if Question('Tienes instalado Linux?'): #nos devolverá un booleano
        InfoMessage('Bienvenido')
    else:
        InfoMessage('Deberias instalar Linux')
