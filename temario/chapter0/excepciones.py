#!/bin/python
# coding=utf-8


excepcion = ''

#ZeroDivisionError:
def division_cero():
	global excepcion
	excepcion = ''
	print("10. Division por cero")
	try:
		numero = 45/0
	except ZeroDivisionError as e:
		print("No puedes dividir entre cero:")
		print(e)
		excepcion = 'La causa ha sido: '+ str(e)
	print(excepcion)


#ValueError
def error_tipo():
	print("9. Error de tipos")
	try:
		numero = float("34R")
	except ValueError as e:
		print("No es el formato correcto:")
		print(e)


#No existente
def funcion_no_existe():
	print("8. Funcion no existe")
	try:
		noExiste("Hola")
	except:
		print("Ha ocurrido una Exception")
	finally:
		print("Ha terminado el bloque")

#Variable no definida
def variable_no_definida():
	global excepcion
	excepcion = 'Hecho'
	print("7. Variable no definida")
	try:
		print(cadena)
	except Exception as e:
		print("Ha ocurrido una Excepcion:")
		excepcion = 'Causa de la excepcion: '+str(e)
		print(excepcion)
	else:
		print("No ha ocurrido ninguna Excepcion")


#Archivo no existe
def archivo_no_existe():
	global excepcion
	print("6. Archivo no existe")
	excepcion = 'Hecho, bloque finalizado'
	try:
		file = open("noExiste.pdf","r")
	except Exception as e:
		print("El archivo no existe:")
		excepcion = 'Causa de la excepcion: '+str(e)
	finally:
		print(excepcion)



#Archivo no encontrado
def archivo_no_encontrado():
	global excepcion
	print("5. Archivo no encontrado")
	excepcion = 'Hecho, bloque finalizado'
	try:
		file = open("noExiste.txt","r")
	except IOError as e:
		print("Archivo no encontrado: ")
		excepcion = 'Causa de la excepcion: '+str(e)
	finally:
		print(excepcion)



#Error de nombre
def error_de_nombre():
	print("4. Error de nombre")
	try:
		clase = Extractor()
	except NameError as ex:
		print("Tipo no definido:")
		print(ex)


#Error de valor
def error_de_valor():
	print("3. Error de valor")
	try:
		dato = int("32f")
	except ValueError as valorEx:
		print("El valor es incorrecto: ")
		print(valorEx)
	except:
		print("Otra excepcion")
	finally:
		print("Fin de bloque")



#try-except-else-finally
def excepcion_testB():
	print("2. try-except-else-finally")
	try:
		divide = 4/0
	except Exception as e:
		print("Ha ocurrido una excepcion: ",e)
	else:
		print("Tal vez pase otra cosa")
	finally:
		print("Ha finalizado el bloque de ejecucion")


#try-except
def excepcion_testA():
	print("1. try-except:")
	try:
		division = 9/0.0
	except Exception as e:
		print("Exception:",e)

		
		
#FileNotFoundException no existe en Python 2.7
def no_existe_arch_PythonTwo(path):
	try:
		f = open(path,"rb")
		data = f.read()
		print("Hecho, archivo leido")
		return data
	except IOError as err:
		print(err)
		raise
	else:
		f.close()
	finally:
		print("Fin del programa")
		

#ModuleNotFoundError
def modulo_no_existe():
	global excepcion
	excepcion = 'Hecho'
	try:
		import PyZenity
	except ModuleNotFoundError as error:
		print("Ha ocurrido uan excepcion al cargar modulo")
		excepcion = 'Causa: '+str(error)
	finally:
		print(excepcion)




def main():
	archivo_no_encontrado()
	excepcion_testA()
	excepcion_testB()
	funcion_no_existe()
	division_cero()
	modulo_no_existe()


if __name__ == '__main__':
    main()