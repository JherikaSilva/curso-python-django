"""3. Validador de Senha: Crie uma função que receba uma senha (string) e retorne True se
ela tiver pelo menos 8 caracteres e False caso contrário"""

def validador(senha:str)->bool:
    """Valida se a senha tem pelo menos 8 caracteres"""
    return len(senha)>=8
    
senha=input("Digite sua senha: ")
if validador(senha):  
     print("Senha válida")
else:
    print("Senha inválida")
    
               