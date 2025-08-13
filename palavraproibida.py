#Palavra proibida com while, enquanto o usuário digitar algo que contenha a palavra 'spoiler' (use.lower e in), peça para digitar novamente

print("-------- PALAVRA PROIBIDA -------")

while True:
   frase= input("Digite sua frase: ").lower()
   if "spoiler" in frase:
     print("Frase inválida, digite novamente:")
   else:
     print("Frase válida")  
     break

