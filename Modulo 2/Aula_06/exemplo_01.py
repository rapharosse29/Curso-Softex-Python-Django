class Cachorro:
    def __init__(self, nome: str, cor: str) -> None:
        ## "O nome DESTE cachorro será..."
        self.nome = nome

        ## "A cor DESTE cao será..."
        self.cor = cor

    def latir(self, fala: str):
        print(f"{self.nome} diz: {fala}")

meu_cachorro = Cachorro("Rex", "Preto")

## Nome e Cor são atributos (variáveis) da classe cachorro.
## Por isso não são chamadas com parênteses: ()
print(meu_cachorro.nome)
print(meu_cachorro.cor)

meu_cachorro.latir("Au Au!!!")