#!/bin/python
# coding=utf-8

MAX = 100

#ciclo for
def ciclo_for():
    global MAX
    print "Ciclo for:"
    for i in range(1,MAX):
    	if i%3 == 0 and i%5 ==0:
    		print "No. ",i
            
#ciclo while return                   
def ciclo_while_return():
    global MAX
    print "Ciclo while:"
    contador, suma = 0,0
    while contador < MAX:
        suma += contador
        contador += 3
    return suma
    
