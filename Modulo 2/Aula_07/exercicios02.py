class Circulo:
    def __init__(self, raio: int):
        if raio < 0:
            print("O raio não deve ser negativo.")
            self._raio = 0
        else:
            self._raio = raio
    @property
    def raio(self) -> int:
        return self._raio
    
    @raio.setter
    def raio (self, novo_raio: int):
        if isinstance(novo_raio, int) and novo_raio > 0:
            self._raio = novo_raio
        else:
            print("Erro!!! O novo raio deve ser positivo e inteiro.")

    def calcular_area(self) -> None:
        area = 3.14159 * (self.raio**2)
        print(area)


roda = Circulo(-10)
print(roda.raio)
roda.raio = -10
roda.calcular_area()
