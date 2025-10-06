-- Active: 1759768063162@@127.0.0.1@3306
create table alunos(
    id integer primary key,
    nome text not null,
    idade integer
);

INSERT INTO alunos (nome, idade) VALUES ('João', 20);
INSERT INTO alunos (nome, idade) VALUES ('Maria', 22); 

SELECT * FROM alunos;

SELECT nome, idade FROM alunos;

SELECT * FROM alunos WHERE idade=20;

SELECT * FROM alunos WHERE nome='Maria' AND idade=22;

UPDATE alunos SET idade=21 WHERE nome='João';

DELETE FROM alunos WHERE nome='Maria';