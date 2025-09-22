#Voce tem uma lista de tuplas(aluno e nota) identifique e imprima a maior noota alcançada, crie uma tupla com todos os alunos que tiraram maior nota
#crie um conjunto de todos os alunos que tiveram uma nota menor 7 

print("-------- NOTAS ---------")
notas=[("Ana",9.5),("João",8.0),("Maria",10.0),("Pedro",7.5),("Ana",10.0),("Carlos",6.5)]
maior=0
alunos_maior=set()
alunos_menor=set()
for nome,nota in notas:
    if nota > maior:
        maior = nota
        if nota == maior:
            alunos_maior.add(nome)
    if nota < 7.0:
        alunos_menor.add(nome)
alunos_maior=tuple(alunos_maior)  
      
print(f"\n A maior nota foi: {maior}")              
print(f"\n Alunos que tiraram a maior nota: {alunos_maior}")                
print(f"\n Alunos que tiraram menos que 7.0: {alunos_menor}")            
            