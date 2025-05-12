# Classe base
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        return f"{self.marca} {self.modelo}"

    def ligar(self):
        print(f"{self.descricao()} está ligado.")

    def desligar(self):
        print(f"{self.descricao()} está desligado.")

# Subclasse Carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def descricao(self):
        return f"{super().descricao()} com {self.portas} portas"

# Subclasse Moto
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def descricao(self):
        return f"{super().descricao()} com {self.cilindradas}cc"

# Uso das classes
carro = Carro("Toyota", "Corolla", 4)
moto = Moto("Honda", "CB500", 500)

carro.ligar()      # Saída: Toyota Corolla com 4 portas está ligado.
moto.ligar()       # Saída: Honda CB500 com 500cc está ligado.
