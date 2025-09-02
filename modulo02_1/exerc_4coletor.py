"""Coletor de dados Robusto
Crie um programa que colete numeros de usuario e os armazene em uma lista, o programa deve continuar pedindo numeros ate que o usuario digite -1 para parar
Ele deve validar a entrada para garantir que o que foi digitado é realmente um numero antes de prosseguir, apenas os numeros entre 0 e 100 devem ser consideradoa validos e adicionados a lista
ao final imprima a soma dos numeros validos e a lista de numeros coletados"""

lista=[]
soma=0
while True:
     numero_valido=True
     print("Para sair do programa digite -1 !")
     numeros=input("Digite um numero: ")
     if numeros!="-1":
            if numeros.isdigit():
                numeros=int(numeros)
                if numeros >0 and numeros <=100:
                    lista.append(numeros)
                    soma+=numeros
                else:
                     print("Esse número não é valido e não será adicionado na lista e nem na soma, digite apenas números positivos!")  
            else:
                 print("Somente números podem ser digitados!")           
     else:
            print(f"Os números digitados válidos foram {lista} e a soma total deles é {soma}")   
            break     


