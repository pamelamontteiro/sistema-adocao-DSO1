from entidades.animal import Animal
from entidades.gato import Gato
from entidades.doador import Doador
from entidades.adotante import Adotante
from entidades.registro_adocao import RegistroAdocao  # Corrigido o nome da classe aqui
from datetime import date


class Sistema:
    def __init__(self):
        self.__animais = []
        # self.__doacoes = []
        self.__registro_adocoes = []  # Mudança de nome da variável

    @property
    def doacoes(self):
        return self.__doacoes

    @property
    def registro_adocoes(self):  # Mudança de nome do método getter
        return self.__registro_adocoes

    def listar_animais_disponiveis(self):
        disponiveis = self.__animais[:]
        for animal in self.__animais:
            for registro in self.__registro_adocoes:  # Mudança de nome da lista
                if animal.numero_chip == registro.animal.numero_chip:
                    if animal in disponiveis:
                        disponiveis.remove(animal)
        return disponiveis

    # def registrar_doacao(self, data_doacao: date, animal: Animal, doador: Doador, motivo: str):
    #     if animal not in self.listar_animais_disponiveis():
    #         self.__doacoes.append(Doacao(data_doacao, animal, doador, motivo))
    #         self.__animais.append(animal)

    def registrar_adocao(
        self, data_adocao: date, animal: Gato, adotante: Adotante, termo_assinado: bool
    ):
        # Verifica se o adotante é maior de 18 anos
        if (date.today().year - adotante.data_nascimento.year) >= 18:

            # Verifica se o animal tem as vacinas necessárias
            vacinas_necessarias = ["Raiva", "Leptospirose", "Hepatite Infecciosa"]
            tem_vacinas = all(
                vacina in animal.vacinas for vacina in vacinas_necessarias
            )

            if not tem_vacinas:
                print("Animal não tem todas as vacinas necessárias.")
                return False

            # Verifica se o adotante já doou um animal
            for doacao in self.doacoes:
                if adotante.cpf == doacao.doador.cpf:
                    print("Adotante já doou um animal e não pode adotar.")
                    return False

            # Se todas as condições forem atendidas, permite a adoção
            self.__registro_adocoes.append(RegistroAdocao(data_adocao, animal, adotante, termo_assinado))  # Mudança de nome aqui
            print("Adoção registrada com sucesso.")
            return True
        else:
            print("Adotante deve ser maior de 18 anos.")
            return False


def main():
    gato = Gato("123", "Pandora", "Siamex", "pequeno", True)
    print(gato.nome)
    adotante = Adotante("4567", "Italo", date.fromisoformat('1990-10-30'), "Rua Lauro Linhares", "apartamento", True)
    print(adotante.nome)
    registro = RegistroAdocao( date.fromisoformat('2024-10-30'), gato, adotante, True)
    print(registro.adotante.nome)


if __name__ == "__main__":
    main()
