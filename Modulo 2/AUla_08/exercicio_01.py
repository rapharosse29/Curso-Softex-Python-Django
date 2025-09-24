class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"{self.nome}, {self.idade} anos")

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        print(f"O estudante {self.nome} tem {self.idade} anos e cursa {self.curso}.")

pessoa = Pessoa("Raphael", 34)
estudante = Estudante("Raphael" , 34, "ADS")

lista: list[Pessoa] = [pessoa, estudante]

for i in lista:
    i.apresentar()