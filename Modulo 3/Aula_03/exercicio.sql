CREATE TABLE autores (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT NOT NULL
);

CREATE TABLE livros (
    id_livro INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    ano_publicacao INTEGER NOT NULL,
    id_autor INTEGER,
    FOREIGN KEY (id_autor) REFERENCES autores (id)
);

INSERT INTO autores(nome, nacionalidade) VALUES ('Cheira Cola', 'Ghanes'), ('Chupa Bife', 'Venezuelano');
INSERT INTO livros(titulo, ano_publicacao, id_autor) VALUES ('Mamajonga', 2025, 1), ('Manja Jeba', 2023, 1), ('Mamiroscopila', 2021, 1), 
    ('Rebelda', 2005, 2), ('Alumbriano', 1955, 2), ('Solerianos', 2009, 2);
SELECT * from autores;
SELECT * from livros;


DROP TABLE autores;
DROP TABLE livros;

SELECT autores.nome, livros.titulo
FROM livros
INNER JOIN autores ON autores.id = id_autor;

SELECT autores.nome, livros.titulo
FROM livros
INNER JOIN autores ON autores.id = id_autor
WHERE nacionalidade = 'Britanica';

SELECT count(livros.titulo), autores.nome
FROM livros
INNER JOIN autores ON autores.id = id_autor
GROUP BY autores.nome;