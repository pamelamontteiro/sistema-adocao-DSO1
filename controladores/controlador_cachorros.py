from uuid import uuid4
from entidades.cachorro import Cachorro
from telas.tela_cachorros import TelaCachorro
from typing import List


class ControladorCachorros:
    __RACAS = ["Labrador", "Pug", "Poodle", "Pinscher", "Vira-lata", "Beagle"]

    def __init__(self, controlador_sistemas):
        self.__cachorros: List[Cachorro] = []
        self.__tela_cachorro = TelaCachorro()
        self.__controlador_sistemas = controlador_sistemas

    @property
    def cachorros(self):
        return self.__cachorros

    def pega_cachorro_por_numero_chip(self, numero_chip: int):
        for cachorro in self.__cachorros:
            if cachorro.numero_chip == numero_chip:
                return cachorro
        return None  # parei aqui

    def incluir_cachorro(self):
        dados_cachorro = self.__tela_cachorro.pega_dados_cachorro(self.__RACAS)
        numero_chip = uuid4().int
        tamanho = self.__tela_cachorro.tamanho_cachorro()
        while True:
            if tamanho.upper() not in ("P", "M", "G"):
                self.__tela_cachorro.mostra_mensagem(
                    "Informação inválida, selecione P, M ou G"
                )
                tamanho = self.__tela_cachorro.tamanho_cachorro()
            else:
                break
        dados_cachorro["tamanho"] = tamanho.upper()
        cachorro = Cachorro(
            numero_chip,
            dados_cachorro["nome"],
            dados_cachorro["raca"],
            dados_cachorro["tamanho"],
        )
        dados_cachorro["numero_chip"] = numero_chip
        self.__cachorros.append(cachorro)
        self.__tela_cachorro.mostra_mensagem(
            "Animal cadastrado com sucesso no Sistema."
        )

    def listar_cachorros(self, filtro: List[str] = []):
        tam_lista_cachorros = len(self.__cachorros)
        if tam_lista_cachorros > 0:
            for cachorro in self.__cachorros:
                if cachorro.numero_chip not in filtro:
                    self.__tela_cachorro.mostra_cachorro(
                        {
                            "numero_chip": cachorro.numero_chip,
                            "nome": cachorro.nome,
                            "raca": cachorro.raca,
                            "tamanho": cachorro.tamanho,
                            "vacinacao": cachorro.listar_vacinacao(),
                        }
                    )

        else:
            self.__tela_cachorro.mostra_mensagem(
                "ERRO: Não existe nenhum cachorro cadastrado no Sistema."
            )
            self.__controlador_sistemas.abre_tela()

    def alterar_cachorro(self):
        self.listar_cachorros()
        try:
            numero_chip = self.__tela_cachorro.seleciona_cachorro()
            cachorro_para_atualizar = self.pega_cachorro_por_numero_chip(numero_chip)
            if cachorro_para_atualizar is None:
                raise Exception

            novos_dados_cachorro = self.__tela_cachorro.pega_dados_cachorro(
                self.__RACAS
            )
            tamanho = self.__tela_cachorro.tamanho_cachorro()
            while True:
                if tamanho.upper() not in ("P", "M", "G"):
                    self.__tela_cachorro.mostra_mensagem(
                        "Informação inválida, selecione P, M ou G"
                    )
                    tamanho = self.__tela_cachorro.tamanho_cachorro()
                else:
                    break

            cachorro_para_atualizar.nome = novos_dados_cachorro["nome"]
            cachorro_para_atualizar.raca = novos_dados_cachorro["raca"]
            cachorro_para_atualizar.tamanho = tamanho.upper()
            self.__cachorros = [
                (
                    cachorro_para_atualizar
                    if cachorro.numero_chip == numero_chip
                    else cachorro
                )
                for cachorro in self.__cachorros
            ]

            self.__tela_cachorro.mostra_mensagem(
                "Dados do cachorro alterados com sucesso."
            )

        except Exception:
            self.__tela_cachorro.mostra_mensagem("ERRO: O cachorro não existe.")
            self.__tela_cachorro.tela_opcoes()

    def excluir_cachorro(self):
        self.listar_cachorros()
        try:
            numero_chip = self.__tela_cachorro.seleciona_cachorro()
            cachorro = self.pega_cachorro_por_numero_chip(numero_chip)

            self.__cachorros.remove(cachorro)
            self.__tela_cachorro.mostra_mensagem(
                f"O cachorro de numero chip: {numero_chip} foi excluido do sistema"
            )
            if len(self.__cachorros) == 0:
                self.__tela_cachorro.mostra_mensagem(
                    "Não existe mais nenhum cachorro cadastrado no sistema"
                )
            else:
                self.__tela_cachorro.tela_opcoes()

            if cachorro is None:
                raise Exception
        except Exception:
            self.__tela_cachorro.mostra_mensagem("ERRO: O cachorro não existe.")
            self.__tela_cachorro.tela_opcoes()

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_cachorro,
            2: self.alterar_cachorro,
            3: self.listar_cachorros,
            4: self.excluir_cachorro,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_cachorro.tela_opcoes()
            while opcao_escolhida not in (1, 2, 3, 4, 0):
                self.__tela_cachorro.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_cachorro.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
