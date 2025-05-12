class Mae:
    def __init__(self):
        self.sobre_nome = "Julia"

    def comer(self):
        print("comendo")

class Filha(Mae):
    #ATRIBUTOS E COMPORTAMENTOS PUBLICOS SÃO PASSADOS PARA A FILHA
    def __init__(self):
        super().__init__()

filha = Filha()
print(filha.sobre_nome)
