from entidades.adotante import Adotante
from entidades.animal import Animal
from datetime import datetime
import uuid


class RegistroAdocao:
    def __init__(
        self,
        data_adocao: datetime,
        animal: Animal,
        adotante: Adotante,
        termo_assinado: bool,
    ):
        self.__data_adocao = data_adocao
        self.__animal = animal
        self.__adotante = adotante
        self.__termo_assinado = termo_assinado
        self.__id_registro = str(uuid.uuid4())  # Gera um código de registro único

    @property
    def id_registro(self):
        return self.__id_registro

    @property
    def data_adocao(self):
        return self.__data_adocao

    @data_adocao.setter
    def data_adocao(self, data_adocao):
        self.__data_adocao = data_adocao

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal):
        self.__animal = animal

    @property
    def adotante(self):
        return self.__adotante

    @adotante.setter
    def adotante(self, adotante):
        self.__adotante = adotante

    @property
    def termo_assinado(self):
        return self.__termo_assinado

    @termo_assinado.setter
    def termo_assinado(self, termo_assinado: bool):
        if isinstance(termo_assinado, bool):
            self.__termo_assinado = termo_assinado
