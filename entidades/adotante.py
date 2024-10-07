from entidades.pessoa import Pessoa
from datetime import date

class Adotante(Pessoa):
    # herança da pessoa
    def __init__(self,
        cpf: str,
        nome: str,
        data_nascimento: date,
        endereco: str,
        tipo_habitacao: str,
        tem_outros_animais: bool,
    ):
        super().__init__(nome, cpf, data_nascimento, endereco)
        self.__tipo_habitacao = (
            tipo_habitacao  # Tipo de habitação (Casa ou Apartamento)
        )
        self.__tem_outros_animais = tem_outros_animais  # Se possui outros animais
        # boolena porque true ou false

    @property
    def tipo_habitacao(self):
        return self.__tipo_habitacao

    @tipo_habitacao.setter
    def tipo_habitacao(self, tipo_habitacao):
        self.__tipo_habitacao = tipo_habitacao

    @property
    def tem_outros_animais(self):
        return self.__tem_outros_animais

    @tem_outros_animais.setter
    def tem_outros_animais(self, tem_outros_animais):
        if isinstance(tem_outros_animais, bool):
            self.__tem_outros_animais = tem_outros_animais
