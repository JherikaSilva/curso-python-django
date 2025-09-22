numero_secreto = 51
contador = 0

while True:
 tentativa = int(input("Digite um número entre 1 e 100: "))
 contador+=1

 if tentativa < numero_secreto :
    print("O numero é menor. ")

 elif tentativa > numero_secreto:
    print("O numero é maior. ")

 if tentativa == numero_secreto:
   
    print("Parabens você acertou !" )

    print("O numero de tentativas foi: ", contador )
    break

  


    






    


    
    











        