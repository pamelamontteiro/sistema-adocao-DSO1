from entidades.animal import Animal

# importar o historico de vacinação


class Gato(Animal):

    # incluir historico de vacinacao no init e super(classe super tmb)

    def __init__(
        self, numero_chip: str, nome: str,raca: str, tamanho: str, castrado: bool
    ):
        super().__init__(numero_chip, nome, raca, tamanho, castrado)
