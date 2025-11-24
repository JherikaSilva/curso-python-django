
# SIMULADOR DE REDE SOCIAL (Versão Texto)
class Usuario:
    def __init__(self, nome, apelido):
        self.nome = nome
        self.apelido = apelido

class Post:
    def __init__(self, texto, dono):
        self.texto = texto
        self.dono = dono
        
class RedeSocial:
    def __init__(self):
        self.banco_de_posts = []
        
    def criar_post(self, texto, usuario_logado):
        novo_post = Post(texto, usuario_logado)
        self.banco_de_posts.append(novo_post)
        
 
    def ver_meu_perfil(self, usuario_logado):
        print(f"\n --- PERFIL DE {usuario_logado.nome.upper()} ---")
        print(f" Usuário: {usuario_logado.apelido}")
        print("-" *30)         
        
        encontrou_algo = False

        for post in self.banco_de_posts:
            
            if post.dono == usuario_logado:
                print(f" {post.texto} (Postado por: {post.dono.apelido})")
                encontrou_algo = True

        if not encontrou_algo:
            print(" (Nenhum post encontrado )")

            print("-" * 30 +"\n")     
        
        
usuario_principal = Usuario("Jherika", "rainhadaprogramação")     
usuario_secundario = Usuario("Pericles", "@reidaprogramação")   

minha_rede_social = RedeSocial()

minha_rede_social.criar_post("Adicionando uma segurança aqui", usuario_principal)
minha_rede_social.criar_post("Meu cabelo está precisando de um salão!", usuario_secundario)
minha_rede_social.criar_post("Felicidade...", usuario_principal)


print("\n--- TESTANDO MEU CÓDIGO ---")
minha_rede_social.ver_meu_perfil(usuario_principal)