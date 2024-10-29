from entidades.vacina import Vacina
from telas.tela_vacina import TelaVacina

class ControladorVacina:
    def __init__(self, controlador_sistemas):
        self.__tela_vacina = TelaVacina()
        self.__controlador_sistemas = controlador_sistemas
        self.__vacinas = [
            Vacina("Raiva", 1),
            Vacina("Leptospirose", 2),
            Vacina("Hepatite Infecciosa", 3),
        ]
        self.__vacina_selecionada = None

    def selecionar_vacina(self):
        while True:
            opcao = self.__tela_vacina.tela_opcoes()
            if opcao == 0:
                print("Retornando ao menu anterior.")
                break
            if 1 <= opcao <= len(self.__vacinas):
                self.__vacina_selecionada = self.__vacinas[opcao - 1]
                self.exibir_vacina()
            else:
                self.__tela_vacina.mostrar_mensagem("ERRO: Digite um valor valido.")

    def exibir_vacina(self):
        if self.__vacina_selecionada:
            print(f"Vacina selecionada: {self.__vacina_selecionada.nome_vacina} (Código: {self.__vacina_selecionada.codigo_vacina})")
