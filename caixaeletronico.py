print ("CAIXA ELETRONICO")
saldo = 500
while True: 
  print (" OPÇÕES ")
  print (" 1 SACAR")
  print (" 2 DEPOSITAR")
  print (" 3 VER SALDO")
  print (" 4 SAIR")
  numero= int(input("Digite a opção desejada: "))
  if numero == 1:
    valor=int(input("Qual valor deseja sacar? $"))
    if valor <=  saldo: 
     print ("Saque autorizado!")
    elif  valor > saldo: 
     print ("Saldo insuficiente")
  elif numero ==2:
    deposito=int(input("Qual valor deseja depositar? $"))
    novo_saldo = saldo + deposito
    print ("O Novo saldo é : $", novo_saldo) 
    saldo= novo_saldo  
  elif numero == 3:
    print ("O seu saldo é : $", saldo)
  else: 
    numero == 4
    break  

print ("Você encerrou a sessão !")  
     
