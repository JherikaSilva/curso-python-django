-- Active: 1760444809460@@127.0.0.1@3306
CREATE TABLE autores (
        ID INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        nacionalidade TEXT NOT NULL
     );

INSERT INTO autores (nome, nacionalidade) VALUES ('Luis', 'Brasileiro'), ('Joao', 'Portugues')   

SELECT * FROM autores

CREATE TABLE livros (
        ID INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL,
        ano_publicacao TEXT NOT NULL,
        id_autor INTEGER,
        FOREIGN KEY (id_autor) REFERENCES autores(ID)
);

INSERT INTO livros (titulo, ano_publicacao, id_autor) VALUES ('O rato', '1998', 2)