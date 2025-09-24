

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def fazer_som(self):
        print("Ruff Ruff!!")

class Gato(Animal):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)
        self.especie = especie

    def fazer_som(self):
        print("Miaaaaaaauu!!!")


def emitir_som(animal:Animal):
    animal.fazer_som()

cao = Cachorro("Rex", 4, "Rotweiller")
gato = Gato("Felix", 2, "persa")

emitir_som(cao)
emitir_som(gato)


"""
cao = Cachorro("Rex", 4, "Rotweiller")
print(cao.nome)
print(cao.idade)
print(cao.raca)
cao.fazer_som()

gato = Gato("Felix", 2, "persa")
print(gato.nome)
print(gato.idade)
print(gato.especie)
gato.fazer_som()
"""