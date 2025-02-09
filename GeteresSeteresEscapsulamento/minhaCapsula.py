class MinhaClassGeterSerter:
    def __init__(self):
        self.valor = None
    
    def setter(self, valor: int)->None:
        self.valor = valor

    @property 
    def getter(self)-> int:
        return self.valor

conta1 = MinhaClassGeterSerter()
conta1.setter(2)
valor = conta1.getter()
print(valor)