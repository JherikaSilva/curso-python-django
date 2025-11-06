lista=[1,5,True, 3.5, "a", "c", False]

nova_lista=[i for i in lista if isinstance(i,(int, float)) and not isinstance(i, bool)]

print(nova_lista)