soma = 0  # Acumulador para a soma dos números

contador = 0

while contador < 5:
    numero = int(input("Digite um número: "))  # Solicita um número ao usuário
    soma += numero  # Adiciona o número digitado à soma
    contador += 1   # Incrementa o contador

print("A soma dos números digitados é:", soma)  # Exibe o resultado final