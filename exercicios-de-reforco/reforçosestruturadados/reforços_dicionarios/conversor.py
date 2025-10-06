

try:
 
 distancia={"metros":1, "quilometros":1000}
 quantidade=int(input("Digite a quantidade que quer converter: "))
 unidade_origem=(input("Essa unidade é digite \n1-METROS \n2-QUILOMETROS \n"))

 while unidade_origem not in ["1","2"] :
    print("Opção inválida digite somente '1' ou '2'")
    unidade_origem=(input("Essa unidade é digite \n1-METROS \n2-QUILOMETROS \n"))
 unidade_convertida=(input("Qual a unidade quer converter? \n1-METROS \n2-QUILOMETROS \n"))   
 while unidade_convertida not in ["1","2"] :
        print("Opção inválida digite somente '1' ou '2'")
        unidade_convertida=(input("Qual a unidade quer converter? \n1-METROS \n2-QUILOMETROS \n"))  
        
 if unidade_origem=="1":
    if unidade_convertida=="1":
        valor=distancia["metros"]
        valor_convertido=quantidade*valor
        print(f"O valor convertido é {valor_convertido} metros!")
    if unidade_convertida=="2":
        valor=distancia["quilometros"]
        valor_convertido=quantidade/valor
        print(f"O valor convertido é {valor_convertido} quilometros!")
 elif unidade_origem=="2":   
    if unidade_convertida=="1":
        valor=distancia["quilometros"]
        valor_convertido=quantidade/valor
        print(f"O valor convertido é {valor_convertido} metros!")
    if unidade_convertida=="2":
        valor=distancia["metros"]
        valor_convertido=quantidade*valor
        print(f"O valor convertido é {valor_convertido} quilometros!")  

except ValueError:
    print("Digite somente números")
