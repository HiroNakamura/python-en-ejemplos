#!/bin/python
# coding=utf-8

#List
def lista():
    return List(["Escoge","Autor","Lenguaje"], title="Selecciona un lenguaje", boolstyle="radiolist", editable=False, select_col="ALL", sep='|', data=[["","Guido","Python"],["","Gosling","Java"]])
