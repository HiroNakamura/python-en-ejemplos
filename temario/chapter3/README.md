# Manejo de archivos usando Python


**Python** se puede encargar del tratamiento de archivos fácilmente.


```python

file = open("datos.txt","r")
cont = 0
for line in file:
  print("Linea: ",line)
  cont = cont + 1

print("No. lineas: ",cont)
```
