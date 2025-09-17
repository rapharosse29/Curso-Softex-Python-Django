import random





class Personagem:
    def __init__(self, nome, vida, ataque, pocoes=0):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.pocoes = pocoes
        self.defendendo = False

    def atacar(self, alvo):
        dano = self.ataque
        if random.random() < 0.2:
            dano *= 2
            print(f"Ataque Crítico de {self.nome}!!")
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano.")
        alvo.receber_dano(dano)

    def defender(self):
        self.defendendo = True
        print(
            (
                f"{self.nome} está defendendo e reduzirá o dano em {}"
            )
        )

    def receber_dano(self, dano):
        if self.defendendo:
            dano = dano // 2
            print(f"{self.nome} defendeu e reduziu o dano para {dano}")
            self.defendendo = False
        self.vida -= dano
        self.vida = max(self.vida, 0)

    def usar_pocao(self):
        pass

