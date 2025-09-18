"""3. Validador de Senha: Crie uma função que receba uma senha (string) e retorne True se
ela tiver pelo menos 8 caracteres e False caso contrário"""

def validador(senha:str)-> bool:
    if len(senha)>=8:
        return True
    
    else:
        return False
    
    
senha=input("Digite sua senha: ")
validador(senha)        