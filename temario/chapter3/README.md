# Manejo de archivos y Regex usando Python


**Python** se puede encargar del tratamiento de archivos fácilmente.


## Ejemplos

Creamos y cerramos archivo

```python
f1 = open("archivo.txt", "x")
f2 = open("nuevo.txt", "w")#sobreescribe
#...
#...
f1.close()
f2.close()


```


Leer contenido de archivo.

```python
file = open("datos.txt","r")
cont = 0
for line in file:
  print("Linea: ",line)
  cont = cont + 1
print("No. lineas: ",cont)
```

Escribir y leer en archivo

```python
#Escribimos
f = open("archivo.txt", "a")#agregamos al final del archivo
f.write("Vamos a escribir unas cuantas lineas.")
f.close()

#Leemos
f = open("archivo.txt", "r")#modo lectura
print(f.read())
```
