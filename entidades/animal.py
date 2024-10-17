from abc import ABC, abstractmethod
from datetime import date


class Animal(ABC):
    @abstractmethod
    def __init__(self, numero_chip: int, nome: str, raca: str):
        self.__historicos_vacinacao = []  # Lista para armazenar histórico de vacinação
        self.__numero_chip = None
        self.__nome = None
        self.__raca = None

        if isinstance(numero_chip, int):
            self.__numero_chip = numero_chip
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(raca, str):
            self.__raca = raca

    @property
    def historicos_vacinacao(self):
        return self.__historicos_vacinacao

    @property
    def numero_chip(self):
        return self.__numero_chip

    @numero_chip.setter
    def numero_chip(self, numero_chip: int):
        if isinstance(numero_chip, int):
            self.__numero_chip = numero_chip

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca: str):
        if isinstance(raca, str):
            self.__raca = raca

    @historicos_vacinacao.setter
    def historicos_vacinacao(self, historico_vacinacao: dict):
        # Adiciona um histórico de vacinação, garantindo que seja um dicionário
        if isinstance(historico_vacinacao, dict):
            self.__historicos_vacinacao.append(historico_vacinacao)

    def listar_vacinas_historico(self):
        # Retorna uma lista com o nome das vacinas aplicadas
        return [historico["vacina"] for historico in self.__historicos_vacinacao]

    def registrar_vacina(self, data_vacina: date, vacina: str):
        # Adiciona uma nova entrada no histórico de vacinação
        if isinstance(data_vacina, date) and isinstance(vacina, str):
            self.__historicos_vacinacao.append({"data": data_vacina, "vacina": vacina})
            print(
                f'Vacina "{vacina}" registrada com sucesso para {self.nome} na data {data_vacina}'
            )
