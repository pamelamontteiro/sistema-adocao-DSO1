from entidades.animal import Animal
from entidades.historico_vacinacao import HistoricoVacinacao


class Gato(Animal):

    def __init__(
        self, numero_chip: str, nome: str, raca: str, tamanho: str, castrado: bool
    ):
        super().__init__(numero_chip, nome, raca, tamanho, castrado)
