from vacina import Vacina
from datetime import date


class HistoricoVacinacao:
    def __init__(self, data_de_vacinacao: date, vacina: Vacina):
        self.__data_de_vacinacao = data_de_vacinacao
        self.__vacina = vacina

    @property
    def data_de_vacinacao(self):
        return self.__data_de_vacinacao

    @data_de_vacinacao.setter
    def data_de_vacinacao(self, data_de_vacinacao):
        self.__data_de_vacinacao = data_de_vacinacao

    @property
    def vacina(self):
        return self.__vacina

    @vacina.setter
    def vacina(self, vacina):
        self.__vacina = vacina