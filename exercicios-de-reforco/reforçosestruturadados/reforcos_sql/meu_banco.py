import sqlite3

conn=sqlite3.connect('biblioteca.db')

print("Banco de dados 'biblioteca' criado com sucesso!")

conn.close()