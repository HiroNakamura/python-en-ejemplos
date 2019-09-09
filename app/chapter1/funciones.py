#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lista import *
from PyZenity import InfoMessage


def get_item_lista():
    item = lista()
    print "Elegiste: "
    print "Autor: ",item[0],", Lenguaje: ",item[1],", País:",item[2]
    InfoMessage("Autor: "+item[0]+", Lenguaje: "+item[1]+", País:"+item[2],width=250,height=140,title="Python for Beginners")
