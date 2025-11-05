class animal:
    def __init__(self, nome):
        self.nome = nome


    def __str__(self):
        return f"Eu sou o {self.nome}"
    

animal = animal("Rex")
print(animal)