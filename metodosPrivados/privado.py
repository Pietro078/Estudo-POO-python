class MinhaClassePrivada:
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.nome = nome
    
    def retornaNome(self):
        print(self.nome)
        self.__retornaCpf()
    def __retornaCpf(self):
        print(self.__cpf)



class MinhaContaBanco:
    def __init__(self,NumeroConta):
        self.__NumeroConta = NumeroConta    
        self.__valorMonetario = 100
        self.__valorTranferencia = 0

    def __mostraDinheiro(self):
        print("valor atual em conta: ",self.__valorMonetario)
    
    def tranferencia(self, valorTranferencia):
        self.__mostraDinheiro()
        self.__valorTranferencia = valorTranferencia
        if(not self.__valorTranferencia > self.__valorMonetario ):
            if (not self.__valorMonetario == 0 ):
                self.__valorMonetario -= self.__valorTranferencia
                print("Tranferencia executada")
                self.__mostraDinheiro()
            else:
                print("dinheiro insuficiente")

jao = MinhaContaBanco(111123123)
jao.tranferencia(10)