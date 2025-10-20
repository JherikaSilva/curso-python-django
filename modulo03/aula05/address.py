import sqlite3
from database import DatabaseConnection

class Address:
    """Gerencia a tabela endereços""" 
    def __init__(self, db_conn=DatabaseConnection):
       self.db_conn= db_conn
       self._create_table()
       
    def _create_table(self):
            self.db_conn.connect()
            self.db_conn.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS enderecos(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                endereco TEXT NOT NULL,       
                )
                
                """
            )
            self.db_conn.close()
            
    def create_address(self, endereco):
        """Cria um novo endereço."""
        self.db_conn.connect()
        
        self.db_conn.cursor.execute(
            "INSERT INTO enderecos (endereco) VALUES (?);",
               (endereco),
            )
        print(f"[SUCESSO] Endereço '{endereco}' criado.")
        
        self.db_conn.close()       
        
    def get_courses_by_student(self, id_aluno):
        """Busca todos os alunos que moram naquele endereço
        """
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            SELECT c.id, c.nome, m.data_matricula
            FROM cursos c
            INNER JOIN matriculas m ON c.id = m.id_curso
            WHERE m.id_aluno = ?;
            """,
            (id_aluno,),
        )    