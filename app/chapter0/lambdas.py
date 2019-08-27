#!/bin/python
# coding=utf-8

#Lambdas
def get_lambdas():
    suma = lambda a,b : a+b
    doble = lambda x : x*2
    print "Suma(2,4) = ",suma(2,4)
    print "Suma(-5,4) = ",suma(-5,4)
    print "Doble de 2 es ",doble(2)
    print "Doble de -45.8 es ",doble(-45.8)
    
 #Lambda
def get_triple(cadena):
	triple = lambda cadena : cadena*3
	return triple(cadena)
    return lambda cadena : cadena * 3

    
