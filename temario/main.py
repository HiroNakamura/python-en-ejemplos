#!/bin/python
# coding=utf-8


from chapter0.archivos import leer_archivo

'''
from chapter0.archivos import *
from chapter0.bucles import *
from chapter0.cadenas import *
from chapter0.clases import *
from chapter0.excepciones import *
from chapter0.funciones import *
from chapter0.lambdas import *
from chapter0.selectivas import *
from chapter0.tuplas import *
from chapter0.variables import *
from chapter1.directorio import *
from chapter1.entrada import *
from chapter1.funciones import *
from chapter1.mensaje import *
from chapter1.seleccion import *
from chapter2.ventana import *
from chapter2.botones import *
from chapter3.file1 import *
'''

def main():
	print("Python for Beginners")
	try:
		from chapter0.archivos import leer_archivo
		from chapter0.bucles import ciclo_for
		print("La importacion ha funcionado!!")
	except ImportError:
		print('La importacion ha fallado')
	finally:
		print("Hecho!!")
	
	try:
		from chapter2.ventana import get_ventana
		get_ventana()
	except ImportError:
		print("No se ha podido importar, quiza no tengas Tkinter para Python 3")
	finally:
		print("Hecho!!")



	#Chapter 0
	#ciclo_for()
	#print "Suma = ",ciclo_while_return()
	#print ciclo_for_return()
	#cadenas()
	#decir_hola()
	#print tam_cadena("Estalaquita")
	#excepcion_testA()
	#excepcion_testB()
	#division_cero()
	#error_tipo()
	#variable_no_definida()
	#archivo_no_existe()
	#archivo_no_encontrado()
	#error_de_nombre()
	#error_de_valor()
	#funcion_variables()
	#get_type()
	#get_lambdas()
	#print "El triple de 9 es: ", get_triple(9)
	#print "El triple de 'Python' es: ",get_triple('Python')
	#menu()
	#print get_color_rojo('red')
	#print get_color_rojo('verde')
	#print get_color_rojo('Amarillo')
	#leer_archivo()
	#mockTestA()#clases
	#mockTestB()#tuplas,etc.
	#lectura_archivo()#files
	#get_funciones_csv()
	#print ver_numero("333")
	#mockTestC()

	#Chapter 1
	#get_mensaje()
	#get_error(None)
	#get_notificacion()
	#introduce_dato()
	#linux_instalado()
	#get_directorio()
	#get_archivo()
	#get_item_lista()
	
	#Chapter 2
	#get_ventana()
	#view_botones()




if __name__ == '__main__':
	main()
