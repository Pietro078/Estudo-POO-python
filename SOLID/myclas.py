class SistemaCadastral:

    def recebeDados(self, nome:str, cpf:int):
        if self.inputVerify(nome,cpf):
            self.cadastrar(nome,cpf)
        else:
            self.tratamentoErro()
    
    def cadastrar(self, nome,cpf):
        print(f"nome: {nome} e cpf: {cpf} cadastrados")
    
    def inputVerify(self,nome,cpf):
        return isinstance(nome,str) and isinstance(cpf,int)
    
    def tratamentoErro(self):
        return print("dados incorretos")

usu = SistemaCadastral()
usu.recebeDados("ola", 123123)