"""Crie um programa que funcione como uma calculadora de bolso. Ele deve ser capaz de fazer
adição, subtração, multiplicação e divisão.
O programa deve sempre mostrar um menu de opções, pedir ao usuário para escolher a
operação e digitar dois números. No final, ele exibe o resultado da conta. Se houver algum
erro, como uma divisão por zero ou o usuário digitar algo que não é um número, o programa
deve avisar e não travar.
"""
def somar(primeiro_num:int, segundo_num:int) ->int:
    """Função para somar números"""
    return primeiro_num + segundo_num

def subtrair(primeiro_num:int, segundo_num:int) ->int:
    """Função para subtrair números"""
    return primeiro_num - segundo_num

def multiplicar(primeiro_num:int, segundo_num:int) ->int:
    """Função para multiplicar números"""
    return primeiro_num * segundo_num

def divisao(primeiro_num:int, segundo_num:int) ->int:
    """Função para dividir números"""
    return primeiro_num / segundo_num

while True:
    try:
        print("=== CALCULADORA ===\n1 - Somar\n2 - Subtrair\n3- Multiplicar\n4- Dividir\n5- Sair")
        opcao=int(input("Digite a sua opção:\n"))
        if opcao==1:
            primeiro_num=int(input("Digite o primeiro número: "))
            segundo_num=int(input("Digite o segundo número: "))
            resultado=somar(primeiro_num,segundo_num)
            print(f"A soma dos números é {resultado}")
        
        elif opcao==2:    
            primeiro_num=int(input("Digite o primeiro número: "))
            segundo_num=int(input("Digite o segundo número: "))
            resultado=subtrair(primeiro_num,segundo_num)
            print(f"A subtração dos números é {resultado}")
        
        elif opcao==3:
            primeiro_num=int(input("Digite o primeiro número: "))
            segundo_num=int(input("Digite o segundo número: "))
            resultado=multiplicar(primeiro_num,segundo_num)
            print(f"A multiplicação dos números é {resultado}")    
        
        elif opcao==4:
            primeiro_num=int(input("Digite o primeiro número: "))
            segundo_num=int(input("Digite o segundo número: "))
            if primeiro_num and segundo_num != 0:
                resultado=divisao(primeiro_num,segundo_num)
                print(f"A divisão dos números é {resultado}")    
            else:
                print("Não se pode fazer divisão com '0'")
        elif opcao==5:
            print("Finalizando o programa")
            break
        else:
            print("Opção inválida !")
            
    except ValueError:
        print("Somente números podem ser digitados")    