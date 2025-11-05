class Midia():
    def __init__(self, titulo: str, duracao_seg: int):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

    def exibir(self):
        print(f"Titulo: {self.titulo}\nDuração: {self.duracao_seg}")

class Musica(Midia):
    def __init__(self, titulo: str, duracao_seg: int, artista: str):
        super().__init__(titulo, duracao_seg)
        self.artista = artista

    def exibir(self):
        print(f"Artista: {self.artista}\nTítulo: {self.titulo}\nDuração: {self.duracao_seg}\n\n")

class Video(Midia):
    def __init__(self, titulo: str, duracao_seg: int, resolucao: str):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao

    def exibir(self):
        print(f"Título: {self.titulo}\nDuração: {self.duracao_seg}\nResolução: {self.resolucao}\n\n")


musica1 = Musica("Tralala", 30, "Seu Zé")
video1 = Video("Juremba", 120, "16k")


dicionario_midias = {"Musicas":[], "videos":[]}
dicionario_midias["Musicas"].append(musica1)
dicionario_midias["videos"].append(video1)

print(dicionario_midias)

for item in dicionario_midias.values():
    for midia in item:
        midia.exibir()