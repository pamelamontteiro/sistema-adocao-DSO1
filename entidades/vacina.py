class Vacina:
    def __init__(self, nome_vacina: str):
        self.__nome_vacina = nome_vacina  # Atribuição direta sem isinstance

    @property
    def nome_vacina(self):
        return self.__nome_vacina

    @nome_vacina.setter
    def nome_vacina(self, nome_vacina: str):
        self.__nome_vacina = nome_vacina  # Atribuição direta sem isinstance
