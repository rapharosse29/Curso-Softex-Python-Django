CREATE TABLE usuarios_cursos (
    id_usuario INTEGER,
    id_cursos INTEGER,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_cursos) REFERENCES cursos(id)
);

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE cursos (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL
);

INSERT INTO usuarios(nome) VALUES ('Pedro'), ('Michele'), ('Raphael'), ('Carol');

INSERT INTO cursos(titulo) VALUES ('backend'), ('frontend');

INSERT INTO usuarios_cursos(id_usuario, id_cursos) VALUES (1,1), (1,2), (2,1), (3,2);
INSERT INTO usuarios_cursos(id_usuario, id_cursos) VALUES (3,1);

SELECT * FROM usuarios;

SELECT * from cursos;

SELECT * FROM usuarios_cursos;

SELECT usuarios.nome, cursos.titulo FROM usuarios_cursos
INNER JOIN usuarios ON usuarios_cursos.id_usuario = usuarios.id
INNER JOIN cursos ON usuarios_cursos.id_cursos = cursos.id;

SELECT count(nome) FROM usuarios WHERE nome = 'Carol'

SELECT COUNT(usuarios.nome) AS QTD_alunos, cursos.titulo FROM usuarios_cursos
INNER JOIN usuarios ON usuarios_cursos.id_usuario = usuarios.id
INNER JOIN cursos ON usuarios_cursos.id_cursos = cursos.id
GROUP BY cursos.titulo;

SELECT COUNT(usuarios.nome) AS QTD_alunos, cursos.titulo FROM usuarios_cursos
INNER JOIN usuarios ON usuarios_cursos.id_usuario = usuarios.id
INNER JOIN cursos ON usuarios_cursos.id_cursos = cursos.id
GROUP BY cursos.titulo
HAVING count(usuarios.nome) > 2;