from datetime import date
from vacina import Vacina

class HistoricoVacinacao:
    def __init__(self, data_vacinacao: date, vacina: Vacina)
        self.__data_vacinacao = data
        self.__vacina = vacina
    
    @property
    def data_vacinacao(self):
        return self.__data_vacinacao
    
    @data_vacinacao.setter
    def data_vacinacao(self, date)
        self.__data_vacinacao = data
    
    @property
    def vacina(self)
        return self.__vacina
    
    @vacina.setter
    def vacina(self, Vacina)
        self.__vacina = vacina