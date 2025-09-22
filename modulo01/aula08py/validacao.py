"""Crie um programa que recebe numero de telefone com 11 digitos, o numero e considerado invalido se tiver 3 ou mais digitos iguais, o programa deve verificar se o numero tem 11 digitos e se todos os caracteres sao numeros
se o numero for valido deve formatar no padrao (xx)xxxxx-xxxx, o programa deve imprimir o numero formatado ou uma mensagem de erro correspondente"""


print("------TELEFONE------")
numero_valido=""
numero=input("Digite seu numero: ")
numero=numero.replace("-","").replace("()","").replace(",","")
if len(numero)!=11:
     print("O número deve ter 11 caracteres!")   
elif not numero.isdigit():
    print("O número deve conter somente NÚMEROS!")
else:
    numero_valido=True                
    for a in numero:
        contador_repetidos=0
        for b in numero:
         a==b
        if a==b:
            contador_repetidos+=1
            if contador_repetidos >=3:
                print("Número não pode ter 3 caracteres iguais")
                numero_valido=False
                break

if not numero_valido:
    print("Não é possivel gerar um telefone com esses digitos!")

else:
    numero_valido==True
    novo_numero=numero 
    ddd=novo_numero[:2]
    primeira_parte=novo_numero[2:7] 
    segunda_parte=novo_numero[7:12]            
    print(f"O número é : ({ddd}){primeira_parte}-{segunda_parte}")            
                 
    