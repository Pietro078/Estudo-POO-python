class MinhaClasse:

    numero = 2 # valores estaticos

    def __init__(self,estado):
        self.estado = estado
        self.__a = "frase"

    def mostra(self):
        
        print(self.__a)

obj = MinhaClasse(True)
obj2 = MinhaClasse(True)

MinhaClasse.numero = 10 # mudam a raiz do valor

print(obj.mostra())