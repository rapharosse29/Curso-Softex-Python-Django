## O primeiro passo é criar sua "gaveta"(TABELA).

CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER
);


INSERT INTO alunos (nome, idade) VALUES ('Jefferson', 29);
INSERT INTO alunos (nome, idade) VALUES ('Amanda', 32);
INSERT INTO alunos (nome, idade) VALUES ('Gabrila', 18);

SELECT * FROM alunos;

SELECT nome, idade FROM alunos;

SELECT * FROM alunos WHERE id = 2;

UPDATE alunos SET idade = 21 WHERE nome = 'João';

DELETE FROM alunos;