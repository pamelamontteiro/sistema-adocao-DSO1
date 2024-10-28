from uuid import uuid4
from entidades.gato import Gato
from telas.tela_gatos import TelaGato


class ControladorGatos:
    __RACAS = ['Siamês', 'Persa', 'Ragdoll', 'Sphynx', 'Vira-lata', 'Munchkin']

    def __init__(self, controlador_sistemas):
        self.__gatos = []
        self.__tela_gatos = TelaGato()
        self.__controlador_sistemas = controlador_sistemas

    @property
    def gatos(self):
        return self.__gatos

    def pega_gato_por_numero_chip(self, numero_chip: int):
        for gato in self.__gatos:
            if gato.numero_chip == numero_chip:
                return gato
        return None

    def incluir_gato(self):
        dados_gato = self.__tela_gatos.pega_dados_gato(self.__RACAS)
        numero_chip = uuid4().int
        gato = Gato(numero_chip, dados_gato["nome"], dados_gato["raca"])
        dados_gato["numero_chip"] = numero_chip
        self.__gatos.append(gato)
        self.__tela_gatos.mostra_mensagem("Animal cadastrado com sucesso no Sistema.")

    def listar_gatos(self):
        tam_lista_gatos = len(self.__gatos)
        if tam_lista_gatos > 0:
            for gato in self.__gatos:
                self.__tela_gatos.mostra_gato(
                    {
                        "numero_chip": gato.numero_chip,
                        "nome": gato.nome,
                        "raca": gato.raca,
                        "vacinacao": gato.listar_vacinacao(),
                    }
                )
        else:
            self.__tela_gatos.mostra_mensagem(
                "ERRO: Não existe nenhum gato cadastrado no sistema."
            )
            self.__controlador_sistemas.abre_tela()

    def alterar_gato(self):
        self.listar_gatos()
        numero_chip = self.__tela_gatos.seleciona_gato()
        gato = self.pega_gato_por_numero_chip(numero_chip)

        if gato is not None:
            novos_dados_gato = self.__tela_gatos.pega_dados_gato()
            gato.nome = novos_dados_gato["nome"]
            gato.raca = novos_dados_gato["raca"]
            # numero_chip é fixo (?) resposta: vou considerar q sim
            # historico_vacinacao só pode ser alterado na sua tela (?)
            self.listar_gatos()
        else:
            self.__tela_gatos.mostra_mensagem("ERRO: O gato não existe.")
            self.__tela_gatos.tela_opcoes()

    def excluir_gato(self):
        self.listar_gatos()
        numero_chip = self.__tela_gatos.seleciona_gato()
        gato = self.pega_gato_por_numero_chip(numero_chip)

        if gato is not None:
            self.__gatos.remove(gato)
            self.__tela_gatos.mostra_mensagem(
                f"O gato de numero chip: {numero_chip} foi excluido do sistema"
            )
            if len(self.__gatos) == 0:
                self.__tela_gatos.mostra_mensagem(
                    "Não existe mais nenhum gato cadastrado no sistema"
                )
            else:
                self.__tela_gatos.tela_opcoes()
        else:
            self.__tela_gatos.mostra_mensagem("ERRO: O gato não existe.")
            self.__tela_gatos.tela_opcoes()

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_gato,
            2: self.alterar_gato,
            3: self.listar_gatos,
            4: self.excluir_gato,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_gatos.tela_opcoes()
            while opcao_escolhida not in (1, 2, 3, 4, 0):
                self.__tela_gatos.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_gatos.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()