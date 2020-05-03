#!/bin/python
# coding=utf-8


from PyZenity import ErrorMessage
from PyZenity import InfoMessage
from PyZenity import GetText


#GetText
def introduce_dato():
  numero=GetText(text='Introduce un número:', entry_text='', password=False)
  try:
    numero = int(numero)
    InfoMessage('Numero introducido es: '+str(numero), width=250,height=140,title="Python for Beginners")
  except ValueError as e:
    ErrorMessage('El formato no es el correcto: '+str(e))
      
   
def main():
	introduce_dato()


if __name__ == '__main__':
    main()