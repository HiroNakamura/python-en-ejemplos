#!/bin/python
# coding=utf-8

#Lambdas
def get_lambdas():
    suma = lambda a,b : a+b
    doble = lambda x : x*2
    divide = lambda numx,numy: numx / numy 
    print("Suma(2,4) = ",suma(2,4))
    print("Suma(-5,4) = ",suma(-5,4))
    print("Doble de 2 es ",doble(2))
    print("Doble de -45.8 es ",doble(-45.8))
    cadena = "Python is better language"
    print("Triple: ",get_triple(cadena))
    division = divide(43,2)
    print("Division: ",division)
    
 #Lambda
def get_triple(cadena):
	triple = lambda cadena : cadena*3
	return triple(cadena)


def suma_tres(a,b,c):
	suma = lambda x,y,z : x+y+z
	return suma
    

def main():
    print("Suma: ",suma_tres(1,4,5))
    print(get_triple("ARIEL"))
    get_lambdas()



if __name__ == '__main__':
    main()
    
