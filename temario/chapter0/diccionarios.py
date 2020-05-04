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
    #diccionario = {"Alef":1,"Yod":10,"Tau":400}
    #diccionario = dict(Alef=1,Yod=10,Tau=400)
    return diccionario

#Obtener llave-valor
def get_dato_diccionario():
    mi_diccionario = get_diccionario()
    print("Diccionario: ",mi_diccionario,", tipo: ",type(mi_diccionario))
    mi_diccionario["Beth"] = 2
    mi_diccionario["Lamed"] = 30
    for k in mi_diccionario:
        print(k," : ",mi_diccionario[k])
    print("\n")
    for key, value in d.iteritems():
        print("Llave: ",key)
        print("Valor: ",value)
    print("")
    letras = dict(A=1,B=2,C=3,D=4,E=5)
    print("Letras(tipo):",type(letras))
    for letra in letras.keys():
        numero = letras[letra]
        print(letra,":",numero)
    print(dir(letras))
        
  
def poner_quitar_item():
    print("Poner-quitar item de un diccionario:")
    diccionario = dict(A=3,B=4,C=7,D=2,E=8)
    print(diccionario)
    print("Quitamos item usando pop('A'):")
    diccionario.pop('A')
    print(diccionario)
    print("Quitamos item usando pop('D'):")
    diccionario.pop('D')
    print(diccionario)
    print("Quitamos item usando pop('E'):")
    diccionario.pop('E')
    print(diccionario)
    for item in diccionario.values():
        print(item)


def funciones_diccionario():
    print("Funciones diccionario:")
    print(dir(dict()))
    diccionario = dict()
    diccionario["A"] = 1
    diccionario["B"] = 2
    diccionario["X"] = 4
    diccionario["Q"] = 11
    print("Llaves: ",diccionario.items())
    print("Valores: ",diccionario.values())



def recorre_diccionarios():
    print("Diccionarios:")
    valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
    for v in valores.values():
        print(v)
    print("**************************************")
    for k, v in valores.items():
        print('k=', k, ', v=', v)
    



def main():
    print("Diccionario: ",get_diccionario())
    causa =''
    try:
        print("Lamed",get_dato_diccionario["Lamed"])
    except TypeError as error:
        print("Ha ocurrido una excepcion: operacion invalida")
        causa = 'La causa ha sido: '+str(error)
    finally:
        print(causa)
    funciones_diccionario()
    poner_quitar_item()



if __name__ == '__main__':
    main()
