#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Clase básica
class Nodo(object):
      def __init__(self, valor,Nodo):
            self.Nodo = Nodo
            self.valor = valor
            print("Se ha creado objeto Nodo")
            
      def __repr__(self):
            return str(self.__dict__)

#Clase base
class Persona(object):
    def __init__(self,nombre,apellidos,edad):
        self.nombre = nombre 
        self.apellidos = apellidos
        self.edad = edad
        print("Se creo e inicio objeto Persona")

    def __repr__(self):
        return str(self.__dict__)
      
      
#Subclase de Persona     
class Autor(Persona):
    def __init__(self, nombre, apellidos,telefono):
        Persona.__init__(self,nombre,apellidos)
        self.telefono = telefono
        print("Se creo e inicio objeto Autor")

    def __repr__(self):
        return str(self.__dict__)



class Libro(object):
    def __init__(self, titulo, isbn,autor):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor 
        print("Se ha creado e inicializado objeto Libro")

    def __repr__(self):
        return str(self.__dict__)
      
      
 
class Tipo:
    def __init__(self):
      print("Objeto Tipo creado e inicializado")
      
    def __str__(self):
      return "Tipo"


def main():
    tipo = Tipo()
    print(tipo)
    libro = Libro('El increado y su realidad fantastica','122-WER-212224556','Diogenes Haumaga')
    print(libro)
    nodo = None
    if nodo == None:
        nodo = Nodo(123, None)
        print("Valor: ",nodo.valor)

if __name__ == '__main__':
    main()