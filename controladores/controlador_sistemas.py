from telas.tela_sistema import TelaSistema
from .controlador_adotantes import ControladorAdotantes
from .controlador_doador import ControladorDoadores
from .controlador_gatos import ControladorGatos
from .controlador_tipo_habitacao import ControladorTipoHabitacao

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_adotantes = ControladorAdotantes(self)
        self.__controlador_doador = ControladorDoadores(self)
        self.__controlador_gatos = ControladorGatos(self)
        self.__controlador_tipo_habitacao = ControladorTipoHabitacao(self)
    @property
    def controlador_adotantes(self):
        return self.__controlador_adotantes
    
    @property
    def controlador_doador(self):
        return self.__controlador_doador

    @property
    def controlador_gatos(self):
        return self.__controlador_gatos
    
    @property
    def controlador_tipo_habitacao(self):
        return self.__controlador_tipo_habitacao


    def inicia_sistema(self):
        self.abre_tela()

    # 1 - Abre a tela de cadastro de Adotantes
    def cadastra_adotantes(self):
        self.__controlador_adotantes.abre_tela()
    
    # 2 - Abre a tela de cadastro de Doadores
    def cadastra_doador(self):
        self.__controlador_doador.abre_tela()

    # 3 - Abre a tela de cadastro de Gatos
    def cadastra_gatos(self):
        self.__controlador_gatos.abre_tela()
    
    

    # 0 - Encerra o Sistema
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastra_adotantes,
            2: self.cadastra_doador,
            3: self.cadastra_gatos,
            0: self.encerra_sistema,
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            while opcao_escolhida not in (1, 2, 3, 0):
                self.__tela_sistema.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
