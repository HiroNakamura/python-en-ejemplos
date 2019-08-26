#!/bin/python
# coding=utf-8

from PyZenity import ErrorMessage
from PyZenity import GetText


#GetText
def introduce_dato():
  numero=GetText(text='Introduce un número:', entry_text='', password=False)
  try:
    numero = int(numero)
  except ValueError as e:
    ErrorMessage('El formato no es el correcto: '+str(e))
      
   
