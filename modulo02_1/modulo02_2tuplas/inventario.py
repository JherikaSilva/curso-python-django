#Voce tem o inventario de uma loja em duas listas de tuplas, cada tupla representa um produto (nome do produto, id)
#estoque principal produtos disponiveis na loja, estoque online produtos disponiveis no site
#usando conjuntos descubra os produtos que estão disponiveis tanto em loja fisica quanto online
#produtos disponiveis apenas em loja fisica
#produtos disponiveis apenas em loja online

print("----- INVENTÁRIO -----")
estoque_fisica=[("Camiseta",101),("Calça",102),("Boné",103),("Tênis",104)]
estoque_online=[("Boné",103),("Camisa Polo",105),("Calça",102),("Chinelo",106)]
fisica=set(estoque_fisica)
online=set(estoque_online)
fisica_online=fisica.intersection(online)
disp_online=fisica.difference(online)
disp_fisica=online.difference(fisica)

print(f"\n Disponíveis em loja física e online{fisica_online}")
print(f"\n Disponíveis em loja física {disp_online}")
print(f"\n Disponíveis em loja online{disp_fisica}")
