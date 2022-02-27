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