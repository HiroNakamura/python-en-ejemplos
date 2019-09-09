#!/bin/python
# coding=utf-8


from PyZenity import List


#List
def lista():
    return List(["Escoge","Autor","Lenguaje"], title="Selecciona un lenguaje", boolstyle="radiolist", editable=False, select_col="ALL", sep='|', data=[["","Guido van Rossum","Python"],["","James Gosling","Java"],["","Gavin King","Ceylon"]])
