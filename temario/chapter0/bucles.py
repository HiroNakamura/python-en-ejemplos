#!/bin/python
# -*- coding: utf-8 -*-

MAX = 100

#ciclo for
def ciclo_for():
    global MAX
    print("Ciclo for:")
    for i in range(1,MAX):
    	if i%3 == 0 and i%5 ==0:
    		print("No. ",i)
    print("\n")
    lista = [1,"2",True, 5, float(2), int("32") ]
    for i in range(len(lista)):
        print(i)
    cont = 0
    for letra in "Guayaba":
        print(letra)
        cont = cont + 1
    print("Cantidad: ",cont)
    for x in range(10):
        print("Hola no.",x)
    for y in range(0,10):
        print("Ciao no.",y)
    rango = range(0,MAX)
    for z in rango:
        if z%3==0 and z%5==0:
            print("Welcome, ",z)
    cont = 0
    while cont < MAX:
        print(cont)
        cont = cont + 3
        if cont > 50:
            break
    print("Contador: ",cont)
    

 
#ciclo for return
def ciclo_for_return():
    global MAX
    suma = 1.5
    print("Ciclo for return:")
    for c in range(2,MAX):
        suma += c
        print("Suma parcial = ",suma)
    return suma



#ciclo while return                   
def ciclo_while_return():
    global MAX
    print("Ciclo while:")
    contador, suma = 0,0
    while contador < MAX:
        suma += contador
        contador += 3
    return suma
    


def main():
    ciclo_for()
    print("Ciclo for return: ",ciclo_for_return())
    print("Ciclo while return: ",ciclo_for_return())



if __name__ == '__main__':
    main()