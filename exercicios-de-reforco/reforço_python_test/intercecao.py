
def intercecao(list1:list, list2: list):
    
    conj1= set(list1)
    conj2= set(list2)

    res= conj1.intersection(conj2)

    res_list= list(res)
    return res_list

