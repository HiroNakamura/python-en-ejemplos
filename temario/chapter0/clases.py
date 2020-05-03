#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Clase básica
class Nodo(object):
      def __init__(self, valor,Nodo):
            self.Nodo = Nodo
            self.valor = valor
            print("Se ha creado objeto Nodo")

      def __del__(self):
          print("Objeto Nodo destruido")
            
      def __repr__(self):
            return str(self.__dict__)
      
      def __str__(self):
            return "Nodo{ valor: "+str(self.valor)+", nodo: "+str(self.Nodo)+"}"

      
#Clase base
class Persona(object):
    def __init__(self,nombre,apellidos,edad):
        self.nombre = nombre 
        self.apellidos = apellidos
        self.edad = edad
        print("Se creo e inicio objeto Persona")

    def __del__(self):
        print("Objeto Persona destruido")


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
lista = []
class Escritor(Autor):
      def set_obras(self, obra):
          global lista
          lista.append(obra)

      def get_obras(self):
          global lista
          return lista


class Libro(object):
    def __init__(self, titulo, isbn,autor):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor 
        print("Se ha creado e inicializado objeto Libro")

    def __del__(self):
        print("Objeto Libro destruido")

    def __repr__(self):
        return str(self.__dict__)
      
      
 
class Tipo:
    atributo = ''
    valor = 0

    def __init__(self):
      print("Objeto Tipo creado e inicializado")

    def __del__(self):
        print("Objeto Tipo destruido")
      
    def __str__(self):
      return "Tipo{ atributo: "+self.atributo+", valor: "+str(self.valor)+" }"

    def __repr__(self):
        return {'atributo':self.atributo, 'valor':str(self.valor)}




def main():
    tipo = Tipo()
    print(tipo)
    tipo.atributo = 'Atributo'
    tipo.valor= 133
    print(tipo)
    print("******************************************")
    escritor = Escritor("Diogenes","Haumaga",2020-1955,"555")
    libro = Libro('El increado y su realidad fantastica','122-WER-214-556',escritor)
    print(libro)
    print("******************************************")
    nodo = None
    if nodo == None:
        nodo = Nodo(123, None)
        print("Valor: ",nodo.valor)
    print("******************************************")
    escritor.set_obras(libro.titulo)
    escritor.set_obras("La Aurora boreal")
    escritor.set_obras("El cobre de oro")
    print("Obras del escritor: ",escritor.get_obras())
    print("******************************************")
    persona = Persona('Juan Miguel','Perez Prado',2020-1997)
    print(persona)
    autor = Autor(persona.nombre, persona.apellidos,persona.edad,'555')
    print(type(autor))
    #type solo muestra el tipo
    if type(autor) == "<class '__main__.Autor'>":
        print("Type: Autor")
    else:
        if isinstance(autor, Persona) == True:
            print("Instancia de Persona")
            print(autor)    
    #Destruimos objetos
    del tipo
    del libro
    del nodo
    del persona
    del autor


if __name__ == '__main__':
    main()
