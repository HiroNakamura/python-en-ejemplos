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
      
      def __str__(self):
            return "Nodo{ valor: "+str(self.valor)+", nodo: "+str(this.Nodo)+"}"

      
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
    def __init__(self, nombre, apellidos,edad,telefono):
        Persona.__init__(self,nombre,apellidos,edad)
        self.telefono = telefono
        print("Se creo e inicio objeto Autor")

    def __repr__(self):
        return str(self.__dict__)

 
#Subclase de Autor
class Escritor(Autor):
      def get_obras(self):
            pass


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
    escritor = Escritor("Diogenes","Haumaga",2020-1955,"555")
    libro = Libro('El increado y su realidad fantastica','122-WER-214-556',escritor)
    print(libro)
    nodo = None
    if nodo == None:
        nodo = Nodo(123, None)
        print("Valor: ",nodo.valor)

if __name__ == '__main__':
    main()
