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