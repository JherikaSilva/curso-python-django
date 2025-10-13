import sqlite3
from datetime import datetime
from database import DatabaseConnection

class BlogModel:
    
    def __init__(self):
        self.db_conn= DatabaseConnection()
        self._create_table()
        
    def _creat_table(self):
        self.db_conn.connect()    
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS blogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                id_user INTEGER,
                FOREIGN KEY (id_user) REFERENCES usuarios(id)
                
            );
            """
        )
        
    
    def create_postagem(self, titulo, conteudo, id_user):
        """Cria uma postagem no blog do usuário."""
        
        self.db_conn.connect()
        self.db_conn.cursor.execute(
                """
                INSERT INTO blogs (titulo, conteudo, id_user)
                VALUES (?, ?, ?);
            """,
                (titulo, conteudo, id_user),
            )
        self.db_conn.cursor.execute("SELECT * FROM blogs WHERE titulo = ?;", (titulo,))
        post=self.db_conn.cursor.fetchall()
        self.db_conn.close()    
        print("Postagem realizada com sucesso")
        return post
    
    def get_all_postagem(self):
        """Retorna todas as postagens do usuários."""
        
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blogs;")
        posts = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return posts
    
    
    def find_postagem_by_id_user(self, id_user):
        """Busca uma postagem pelo ID USER."""
        
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blogs WHERE id_user = ?;", (id_user,))
        post = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return post
    
    def find_postagem_by_id(self, id):
        """Busca uma postagem pelo ID."""
        
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM blogs WHERE id = ?;", (id,))
        post = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return post
    
    def update_postagem_by_id(self, id, titulo=None, conteudo=None):
        """Atualiza informações de uma postagem pelo ID."""
        
        self.db_conn.connect()
        updates = []
        params = []
        if titulo:
            updates.append("titulo = ?")
            params.append(titulo)
        if conteudo:
            updates.append("conteudo = ?")
            params.append(conteudo)

        if not updates:
            print("Nenhum dado para atualizar.")
            self.db_conn.close()
            return

        updates.append("data_atualizacao = ?")
        params.append(datetime.now())
        params.append(id)
        query = f"UPDATE usuarios SET {', '.join(updates)} WHERE id = ?;"

        self.db_conn.cursor.execute(query, params)
        print("Postagem atualizada com sucesso!")
        self.db_conn.close()
        
        
    def delete_postagem_by_id(self, id):
        """Deleta uma postagem pelo ID."""
        
        self.db_conn.connect()
        self.db_conn.cursor.execute("DELETE FROM usuarios WHERE id = ?;", (id,))
        print("Postagem deletada com sucesso!")
        self.db_conn.close()
    