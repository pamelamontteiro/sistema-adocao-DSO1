from datetime import date
from entidades.animal import Animal
from entidades.doador import Doador


class Doacao:
    def __init__(self, codigo_registro: int, data_de_doacao: date, animal: Animal, doador: Doador, motivo: str):
        self.__data_de_doacao = data_de_doacao
        self.__codigo_registro = codigo_registro
        self.__animal = animal
        self.__doador = doador
        self.__motivo = motivo

    @property
    def codigo_registro(self):
        return self.__codigo_registro

    @property
    def data_de_doacao(self):
        return self.__data_de_doacao

    @property
    def animal(self):
        return self.__animal

    @property
    def doador(self):
        return self.__doador

    @property
    def motivo(self):
        return self.__motivo

    @codigo_registro.setter
    def codigo_registro(self, codigo_registro: int):
        if isinstance(codigo_registro, int):
            self.__codigo_regstro = codigo_registro
    @motivo.setter
    def motivo(self, motivo: str):
        if isinstance(motivo, str):
            self.__motivo = motivo