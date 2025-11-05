## O primeiro passo é criar sua "gaveta"(TABELA).

CREATE TABLE professores (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    id_professor INTEGER,
    FOREIGN KEY (id_professor) REFERENCES professores (id)
    ON DELETE CASCADE
);

INSERT INTO professores (nome) VALUES ('Anderson');
INSERT INTO professores (nome) VALUES ('Fabricio');


SELECT * FROM professores;

SELECT * FROM alunos;

SELECT id AS identificador, nome AS primeiro_nome FROM alunos;

SELECT alunos.nome AS nome_aluno, professores.nome AS nome_professor
FROM alunos
INNER JOIN professores ON alunos.id_professor = professores.id;



DROP TABLE alunos; -- Apaga tabelas
DELETE FROM alunos WHERE id_professor = 2;
INSERT INTO alunos (nome, id_professor) VALUES ('Raphael', 1);
INSERT INTO alunos (nome, id_professor) VALUES ('João', 1);

INSERT INTO alunos (nome, id_professor) VALUES ('Mauricio', 2);
INSERT INTO alunos (nome, id_professor) VALUES ('Pietra', 2);

