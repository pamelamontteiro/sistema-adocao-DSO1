from uuid import uuid4
from entidades.gato import Gato
from telas.tela_gatos import TelaGato
from typing import List


class ControladorGatos:
    __RACAS = ["Siamês", "Persa", "Ragdoll", "Sphynx", "Vira-lata", "Munchkin"]

    def __init__(self, controlador_sistemas):
        self.__gatos: List[Gato] = []
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

    def listar_gatos(self, filtro: List[str] = []):
        tam_lista_gatos = len(self.__gatos)
        if tam_lista_gatos > 0:
            for gato in self.__gatos:
                if gato.numero_chip not in filtro:
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
        print(numero_chip)
        try:
            gato_para_atualizar = self.pega_gato_por_numero_chip(numero_chip)
            if gato_para_atualizar is None:
                raise Exception

            novos_dados_gato = self.__tela_gatos.pega_dados_gato(self.__RACAS)
            gato_para_atualizar.nome = novos_dados_gato["nome"]
            gato_para_atualizar.raca = novos_dados_gato["raca"]
            self.__gatos = [
                gato_para_atualizar if gato.numero_chip == numero_chip else gato
                for gato in self.__gatos
            ]
            self.__tela_gatos.mostra_mensagem(
                "Dados do cachorro alterados com sucesso."
            )

        except Exception:
            self.__tela_gatos.mostra_mensagem("ERRO: O gato não existe.")

    def excluir_gato(self):
        self.listar_gatos()
        numero_chip = self.__tela_gatos.seleciona_gato()
        try:
            gato = self.pega_gato_por_numero_chip(numero_chip)
            if gato is None:
                raise Exception

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
        except Exception:
            self.__tela_gatos.mostra_mensagem("ERRO: O gato não existe.")

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
