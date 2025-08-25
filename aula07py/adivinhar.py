#Crie um jogo simples onde o usuário deve adivinhar o número
secreto=10
for i in range(5):
    palpite=int(input("Digite seu palpite: "))
    if palpite>secreto:
        print("O número é muito baixo")
    elif palpite<secreto:
        print("O número é muito alto")  
    else:
        palpite==secreto
        print("Parabéns você acertou")  
        break
if i==4:
    print(f"Game Over, o número era: {secreto} ")
    
    
    