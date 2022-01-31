#!/usr/bin/env python
# -*- coding: utf-8 -*-


mapa_numerologico = {"A":1, "B":2, "C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":1,"K":2,"L":3,"M":4,"N":5,"O":6,"P":7,"Q":8,"R":9,"S":1,"T":2,"U":3,"V":4,"W":5,"X":6,"Y":7,"Z":8}

tabla_numerica = {1:"1. Inicio, progreso, desarrollo y liderazgo",2:"2. Armonía, cooperación, conexión",3:"3. Creatividad, expresión, optimismo",4:"4. Practicidad, estancamiento, limitaciones",5:"5. Creación, fertilidad, libertad, cambio",6:"6. Realización, familia, amistad, cuidar",7:"7. Espíritu, iluminación, magia, misterio",8:"8. Abundancia, éxito, suerte,carisma",9:"9. Finalizacón, cierre, servicio, desinterés",11:"11. El Mensajero; misticismo, sensibilidad; fanatismo, desorientación, impaciencia, injusticia",22:"22. Maestro material; perspicacia, idealismo, ética; falsa superioridad, depresión, avaricia",33:"33. Protección al prójimo; ingenio, bondad, espiritualidad; indecisión, inestabilidad, celos"}


def mision_vida(fecha):
    print("Fecha introducida:",fecha)
    divideFecha = fecha.split("-")
    print("Longitud:",len(divideFecha))
    dia = divideFecha[0]
    mes = divideFecha[1]
    anyo = divideFecha[2]
    sumaPreliminar = int(dia)+int(mes)+int(anyo)
    sumaPreliminar = suma_final(sumaPreliminar)
    return tabla_numerica[sumaPreliminar]


def suma_final(numero):
    numero_str = str(numero)
    suma = 0
    if len(numero_str)>=2:
        for element in range(0, len(numero_str)):
            suma+=int(numero_str[element])
    else:
        suma = numero
    return suma

def quitarEspacio(cadena):
    final = ""
    for element in range(0, len(cadena)):
        if cadena[element] !=" ":
            final+=str(cadena[element])
    return str(final)

def obtener_valor(letra):
    return mapa_numerologico[letra]


def sumar_letras(cadena):
    suma = 0
    for element in range(0, len(cadena)):
        suma+=obtener_valor(cadena[element])
    return suma

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
    nombre = input("Escribe tu nombre completo:")
    nombre = nombre.upper()
    print("Nombre:",nombre)
    try:
        sin_espacios = quitarEspacio(nombre)
        obtener_numero = sumar_letras(sin_espacios)
    except TypeError as excepcion:
        causa = "Excepcion: "+str(excepcion)
    finally:
        print("Número onomástico:",suma_final(obtener_numero))
    fecha = input("Introduce fecha de nacimiento en formato dd-mm-yyyy : ")
    try:
        print("Tu fecha es:",fecha)
        print("Tu numero de misión de vida es: ",mision_vida(fecha))
    except TypeError as excepcion:
        print("Ha ocurrido una excepcion al obtener fecha: "+str(excepcion))
    finally:
        print("Hecho")

if __name__ == '__main__':
    main()
