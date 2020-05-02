# Manejo de archivos usando Python





```python

file = open("datos.txt","r")
cont = 0
for line in file:
  print("Linea: ",line)
  cont = cont + 1

print("No. lineas: ",cont)
```
