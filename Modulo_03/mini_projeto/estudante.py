from pessoa import Pessoa

materias: dict[str, list[float]] = {}

class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula: str):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.notas = {}

    def get_notas(self):
        return self.notas
    
    def set_notas(self, materia: str, nota:float):
        aula: list | None = self.notas.get(materia)
        if aula:
            aula.append(nota)
        else:
            self.notas[materia]=[nota]
        
