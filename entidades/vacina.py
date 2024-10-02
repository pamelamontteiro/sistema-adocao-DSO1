from datetime import date


class Vacina:
    def __init__(self, nome_vacina: str, data_de_vacinacao: date):
        self.__nome_vacina = nome_vacina  # Atribuição direta sem isinstance
        self.__data_de_vacinacao = data_de_vacinacao  # Atribuição direta

    @property
    def nome_vacina(self):
        return self.__nome_vacina

    @nome_vacina.setter
    def nome_vacina(self, nome_vacina: str):
        self.__nome_vacina = nome_vacina

    @property
    def data_de_vacinacao(self):
        return self.__data_de_vacinacao

    @data_de_vacinacao.setter
    def data_de_vacinacao(self, data_de_vacinacao: date):
        self.__data_de_vacinacao = data_de_vacinacao
