class MinhaClasse:
    def metodo_1(self):
        print('ola')
        return "aloooo"

class MinhaClasse2:
    def __init__(self, info): #Este sempre sera o primeiro metodo a iniciar. METODO CONSTRUTOR
        print("inicio do init")
        self.MeuAtributo1= "ola"
        self.MeuAtributo2= [1,2,"a"]
        self.MeuAtributo3 = info
    def meuMetodo(self):
        print(self.MeuAtributo1)
        print(self.MeuAtributo3)
        print(self.MeuAtributo2)
    def passagemLista(self):
        print(self.MeuAtributo2[2])
        for a in self.MeuAtributo2:
            print(a)

class MinhaClasse3:
    def __init__(self):
        self.nome = "nome"
    
    def uper(self):
        return self.nome.upper()

    def mostra(self):
        print(self.uper())
    
minha_classe3 = MinhaClasse3()
minha_classe3.mostra()

