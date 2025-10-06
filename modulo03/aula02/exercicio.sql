-- Active: 1759768063162@@127.0.0.1@3306
CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY,
    primeiro_nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);

CREATE TABLE postagens(
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    postagem TEXT NOT NULL,
    id_autor INTEGER

);

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha) VALUES ('Jherika', 'Silva', 'jherika@gmail', '1234');

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha) VALUES ('Pericles', 'Silva', 'pericles@gmail', '4321');

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha) VALUES ('Marinalva', 'Teixeira', 'nalva@gmail', 'abcd');

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha) VALUES ('Carlos', 'Teixeira', 'carlos@gmail', 'ab12'), 
('Jheme', 'Silva', 'jheme@gmail', 'bc24');

SELECT * FROM usuarios;

UPDATE usuarios set email= 'jherikagatinha@gmail' where primeiro_nome= 'Jherika'

UPDATE usuarios set sobrenome= 'P J' where email='pericles@gmail'

DELETE FROM usuarios WHERE email='jheme@gmail'


--Tabela postagem


INSERT INTO postagens (titulo, postagem, id_autor) VALUES ('Ola como vai', '25415bd', 847564),
('Bom dia', 'sjhde45', 475),
('Oi tudo bem', '541her', 253641),
('Josue', 'errrou', 541661),
('Jose', 'apostteu', 25417);

SELECT * FROM postagens

UPDATE postagens set titulo= 'Jesus é bom' where id_autor=25417

UPDATE postagens set postagem= 'Deus' where postagem= 'errrou'

DELETE FROM postagens where postagem= 'sjhde45' 