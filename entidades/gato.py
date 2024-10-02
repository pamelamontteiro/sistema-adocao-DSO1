from entidades.animal import Animal

#importar o historico de vacinação

class gato:

     #incluir historico de vacinacao no init e super(classe super tmb)

    def __init__(self, nome:str, numero_chip:str, raca:str, tamanho:str, castrado:str):
        super().__init__(numero_chip, nome, raca)