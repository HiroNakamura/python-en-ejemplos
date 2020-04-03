#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lista import *
from PyZenity import InfoMessage


def get_item_lista():
    item = lista()
    print("Elegiste: ")
    print("Autor: ",item[0],", Lenguaje: ",item[1],", País:",item[2])
    autor = item[0]

    if autor == 'Larry Wall':
    	autor = autor +", \n'Los verdaderos programadores pueden escribir código ensamblador en cualquier lenguaje.'"
    elif autor == 'James Gosling':
    	autor = autor +" \n'La imitación es la forma más sincera de adulación, muchas gracias.'"
    else: 
    	if autor == "Guido van Rossum":
    		autor = autor +" \n'Python es mejor que cualquier otro lenguaje.'"
    	else:
    		autor = autor +" \n'Hola.'"


    InfoMessage("Elegiste: \nAutor: "+autor+"\nLenguaje: "+item[1]+"\nPaís:"+item[2],width=250,height=140,title="Python for Beginners")
