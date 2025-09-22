"""Crie um dicionário. Troque as chaves pelos valores e os valores
pelas chaves. Dica: Os valores devem ser únicos para que isso funcione"""

dicionario= {"jherika": 10, "pericles": 20, "nalva": 30 }

dicionario_invertido={}

for nome, valor in dicionario.items():
   dicionario_invertido[valor]=nome
   
print(f"Dicionário original {dicionario}")   
print(f"Dicionário invertido {dicionario_invertido}")    
    