contador = 0
a=0
b=1
soma= 1
print ("----SEQUÊNCIA DE FIBONACCI----")
numero= int(input("Digite um número: "))

while contador <= numero :
  print (a)
  soma = a + b
  a = b
  b = soma

  contador+= 1    
print ("Sequência Fibonacci de número ", numero)  
  
    
     
