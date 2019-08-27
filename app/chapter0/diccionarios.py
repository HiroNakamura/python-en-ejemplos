#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Diccionario
def get_diccionario():
    diccionario = {} # también diccionario = dict()
    #agregar llave-valor
    diccionario["Alef"] = 1
    diccionario["Yod"] = 10
    diccionario["Tau"] = 400
    #Equivale a:
    #diccionario={"Alef":1,"Yod":10,"Tau":400}
    return diccionario

#Obtener llave-valor
def get_dato_diccionario():
    mi_diccionario = get_diccionario()
    print "Diccionario: ",mi_diccionario,", tipo: ",type(mi_diccionario)
    mi_diccionario["Beth"] = 2
    mi_diccionario["Lamed"] = 30
    for k in mi_diccionario:
        print k," : ",mi_diccionario[k]
    print "\n"
    for key, value in d.iteritems():
        print "Llave: ",key
        print "Valor: ",value
        
        
        
        
        
        
    
