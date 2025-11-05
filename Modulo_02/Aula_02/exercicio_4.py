

notas = [
    ("Ana", 9.5),
    ("João", 8.0),
    ("Maria", 10.0),
    ("Pedro", 7.5),
    ("Ana", 10.0),
    ("Carlos", 6.5)
]

maior_nota = set()

alunos_maior_nota = list()

alunos_menor_nota = set()

nota_inicial = 0

for aluno, nota in notas:
    if nota >= nota_inicial:
        nota.add(maior_nota)
    else:
        nota_inicial += nota_inicial