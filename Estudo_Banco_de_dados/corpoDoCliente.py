import sqlite3

class verificaCliente:
    def __init__(self, nomeDB="ClienteDB"):
        self.conectDB = sqlite3.connect(nomeDB)
        self.cursor = self.conectDB.cursor()

    def criaTabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone integer NOT NULL unique,
                cpf TEXT NOT NULL unique
            )
        ''')

    
        self.conectDB.close()

    def __inserirCliente(self, nome, telefone, cpf):
        self.cursor.execute("""
            insert into clientes (nome, telefone, cpf) values (?,?,?)
        """, (nome,telefone,cpf))

    def validacao_n_t_c(self nome, telefone, cpf):

    
a = verificaCliente()
