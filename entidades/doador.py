from pessoa import Pessoa
from datetime import date

class Doador(Pessoa):
    #herança da pessoa 
    def __init__(cpf: str, nome: str,  data_nascimento: date, endereco: str):
        super().__init__(nome, cpf,data_nascimento,endereco)
