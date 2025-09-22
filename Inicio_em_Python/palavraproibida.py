print ("---- PALAVRA PROIBIDA ----")

frase= input("Digie sua frase: ")
proibida= "bomba"

if proibida in frase:
    print ("A frase contém a palavra proibida")
else:
    print ("Frase autorizada")    