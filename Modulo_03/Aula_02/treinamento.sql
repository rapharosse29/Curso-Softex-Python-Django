Crie duas tabelas no seu banco: (Usuarios e Postagens)
Usuarios terá atributos (Colunas): id, primeiro_nome,sobrenome, email e senha
postagens terá atributos (Colunas): id, titulo, postagem e id_autor

o id_usuarios será um id existente de usuarios

Faça 5 inserções de valores em casa tabela

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    primeiro_nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);

CREATE TABLE postagens (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    postagem TEXT NOT NULL,
    id_autor INTEGER NOT NULL
);

INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES ('Raphael', 'Del Rosse', 'rapharosse29@gmail.com', 'senha123');
INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES ('Joel', 'Santanae', 'papaijoel@gmail.com', 'bafanabafanaplaygoodtothelefttotherightinthemornig');
INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES ('Cris', 'flores', 'ataldacrisflores@hotmail.com', 'edecasaeruim2025');
INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES ('Cristiano', 'Ronaldo', 'cr7maiorquemessi@gmail.com', 'ziiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiuu');
INSERT INTO usuarios(primeiro_nome, sobrenome, email, senha) VALUES ('Dilera', 'Oficial', 'naistateoistamaoquista@gmail.com', 'fazueledelulaladrao');




INSERT INTO postagens(titulo, postagem, id_autor) VALUES ('Vivendo e aprendendo', 'O céu de Maricá é lindo', 'rapharosse29');
INSERT INTO postagens(titulo, postagem, id_autor) VALUES ('Mais um treino da seleção, só tem fominha', 'Bafana Bafana play good today', 'santana_joelofc');
INSERT INTO postagens(titulo, postagem, id_autor) VALUES ('Hoje em dia no ar', '#chupafatima #chupatvglobinho', 'crisfloresofc');
INSERT INTO postagens(titulo, postagem, id_autor) VALUES ('Mais um golo pro papi', 'Ziiiiiiiiiiiiiiiuu', 'cr7');
INSERT INTO postagens(titulo, postagem, id_autor) VALUES ('Ao vivo no The Noite com o branquelo corno do Gentili', 'preto', 'dilera_oficial');


SELECT * FROM postagens;

SELECT * FROM usuarios;

UPDATE usuarios SET sobrenome = 'Santana' WHERE id = 2;
DELETE FROM postagens;