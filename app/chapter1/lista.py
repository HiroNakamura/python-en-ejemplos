#!/bin/python
# coding=utf-8


from PyZenity import List


#List
def lista():
    return List(["Escoge","Autor","Lenguaje","País"], 
                title="Selecciona un lenguaje", boolstyle="radiolist", 
                editable=False, select_col="ALL", sep='|', data=[["","Guido van Rossum","Python","Países Bajos"]
                                                                 ,["","Anders Hejlsberg","C#","Dinamarca"]
                                                                 ,["","James Gosling","Java","Canadá"]
                                                                 ,["","Larry Wall","Perl","USA"]
                                                                 ,["","Gavin King","Ceylon","Unknow"]])
