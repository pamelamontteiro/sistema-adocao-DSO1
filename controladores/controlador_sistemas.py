from telas.tela_sistema import TelaSistema
from .controlador_adotantes import ControladorAdotantes
from .controlador_gatos import ControladorGatos


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_adotantes = ControladorAdotantes(self)
        self.__controlador_gatos = ControladorGatos(self)

    @property
    def controlador_adotantes(self):
        return self.__controlador_adotantes

    @property
    def controlador_gatos(self):
        return self.__controlador_gatos

    def inicia_sistema(self):
        self.abre_tela()

    # 1 - Abre a tela de cadastro de Adotantes
    def cadastra_adotantes(self):
        self.__controlador_adotantes.abre_tela()

    # 2 - Abre a tela de cadastro de Gatos
    def cadastra_gatos(self):
        self.__controlador_gatos.abre_tela()

    # 0 - Encerra o Sistema
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastra_adotantes,
            2: self.cadastra_gatos,
            0: self.encerra_sistema,
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            while opcao_escolhida not in (1, 2, 0):
                self.__tela_sistema.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
