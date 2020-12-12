# Python básico


1. Mostrar versión de **Python** instalado.

```java
$ python --version

```

Otra forma:
```java
$ python -V
```


2. Listar el **Zen de Python**.

```java
$ python
```

```java
> import this
```

3. REPL.

```java
$ python
```

```java
> cadena = 'Hola, mundo'
> numero = 33
> verdadero = 56 > 65
> falso =  34%5==0
> nada = None
> type(cadena)
> cadena = cadena.upper()
> help(str)
> help(type)
> dir(list())
> quit() #o exit()
```

4. Enumeraciones (en Python 3)

```java
import enum

class Programador(enum.Enum):
   Junior = 1
   Mid_Level = 2
   Senior = 3
   

#'Main'
print ("Valor: ",end="")
print (Programador.Senior)
junior = Programador.Junior
print(junior)
   
```

5. Listar módulos
```java
$ python 
>> help('modules')

```


## Usando Postgres

Para crear conexiones en Postgres necesitamos instalar la siguiente librería.

```
pip install psycopg2
```

## Usando MySQL

Para crear conexiones en Mysql necesitamos instalar la siguiente librería.


```
pip install mysql-connector-python
```



