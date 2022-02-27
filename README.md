<h1 align="center">	Ejercicios  de recursividad</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/carmenm02/ejercicios_recursividad.git)

## Ejercicio 5:

**SOLUCION**
```
lista = [1,2,3,4,5,6,7,8]
elemento = " "
posicion = len(lista) // 2
repeticiones = 1

class listas:
  def  __init__(self,lista,n,i,j):
    self.i= i
    self.j= j
    self.n= n
    
  def busqueda_numero (self):
    
    if self.i > self.j:
      return'No hay ningún valor en la posición seleccionada'
      
    else:
      self.m = m
      if lista[self.m] == n:
        return self.m
      elif lista[self.m] > n:
        print (busqueda_numero(self))
        return busqueda_numero (self,self.m -1)
      else:
        return busqueda_numero (self, self.m + 1)
        
 
  resultado = listas(lista,n,j,i)
  print(resultado.busqueda_numero())
```
## Ejercicio 6:

**SOLUCION**
```
palabra = str(input("Introduce una palabra"))

class verificar:
  def _init_(self,palabra):
    self.palabra = palabra
  def palabra_palindroma(self):
    if str(self.palabra) == str(self.palabra)[::-1]:
      print("Verdadero, la palabra es palindroma")
    else:
      print("Falso, la palabra no es palindroma")
      
resultado = verificar(palabra)
print(resultado.palabra_palindroma)

word = palabra
class convertidor:
  def _init_(self,word):
    self.word=word
  def convertit_mayuscula(self):
    if word.islower():
      return word.upper()
    else:
      print (word)
```

## Ejercicio 7:

**SOLUCION**
```
import random
bandera = []

def crear_bandera():
    repe = random.randint(10, 20)
    for i in range(repe):
        num = random.randint(1, 3)
        if num == 1:
            bandera.append("R")
        elif num == 2:
            bandera.append("V")
        elif num == 3:
            bandera.append("A")
    return bandera

def ordenar_colores(tamaño, indice, contador):
    if contador < tamaño:
        if bandera[indice] == "R":
            rojo = bandera.pop(indice)
            bandera.insert(0, rojo)
            ordenar_colores(tamaño, indice + 1, contador + 1)
        elif bandera[indice] == "A":
            azul = bandera.pop(indice)
            bandera.insert(len(bandera), azul)
            ordenar_colores(tamaño, indice, contador + 1)
        else:
            ordenar_colores(tamaño, indice + 1, contador + 1)
    else:
        return bandera
        
bandera = crear_bandera()
print(bandera)
ordenar_colores(len(bandera), 0, 0)
print(bandera)
