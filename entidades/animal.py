from abc import ABC, abstractmethod
from datetime import date


class Animal(ABC):
    @abstractmethod
    def __init__(
        self, numero_chip: int, nome: str, raca: str, tamanho: str, castrado=bool
    ):
        self.__historicos_vacinacao = []  # Lista para armazenar histórico de vacinação
        self.__numero_chip = numero_chip
        self.__nome = nome
        self.__raca = raca
        self.__tamanho = (
            tamanho  # Assumindo que o tamanho seja sempre uma string válida
        )
        self.__castrado = castrado  # bolleano true e false

    @property
    def historicos_vacinacao(self):
        return self.__historicos_vacinacao

    @historicos_vacinacao.setter
    def historico_vacinacao(self, historico_vacinacao):
        self.__historico_vacinacao = historico_vacinacao

    @property
    def numero_chip(self):
        return self.__numero_chip

    @numero_chip.setter
    def numero_chip(self, numero_chip):
        self.__numero_chip = numero_chip

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self):
        return self.__tamanho

    @property
    def castrado(self):
        return self.__castrado

    @castrado.setter
    def castrado(self):
        return self.__castrado

    @historicos_vacinacao.setter
    def historicos_vacinacao(self, historico_vacinacao):
        # Adiciona um histórico de vacinação
        self.__historicos_vacinacao.append(historico_vacinacao)

    def listar_vacinas_historico(self):
        # Retorna uma lista com o nome das vacinas aplicadas
        lista_historico = [
            historico["vacina"] for historico in self.__historicos_vacinacao
        ]
        return lista_historico

    def registrar_vacina(self, data_vacina: date, vacina: str):
        # Adiciona uma nova entrada no histórico de vacinação
        self.__historicos_vacinacao.append({"data": data_vacina, "vacina": vacina})
        print(
            f'Vacina "{vacina}" registrada com sucesso para {self.nome} na data {data_vacina}'
        )
