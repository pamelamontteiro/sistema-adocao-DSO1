from uuid import uuid4
from entidades.cachorro import Cachorro
from telas.tela_cachorros import TelaCachorro


class ControladorCachorros:
    __RACAS = ['Labrador', 'Pug', 'Poodle', 'Pinscher', 'Vira-lata', 'Beagle']
    __TAMANHOS = ['Pequeno', 'Médio', 'Grande']

    def __init__(self, controlador_sistemas):
        self.__cachorros = []
        self.__tela_cachorros = TelaCachorro()
        self.__controlador_sistemas = controlador_sistemas

    @property
    def cachorros(self):
        return self.__cachorros

    def pega_cachorro_por_numero_chip(self, numero_chip: int):
        for cachorro in self.__cachorros:
            if cachorro.numero_chip == numero_chip:
                return cachorro
        return None

    def incluir_cachorro(self):
        dados_cachorro = self.__tela_cachorros.pega_dados_cachorro(self.__RACAS, self.__TAMANHOS)
        numero_chip = uuid4().int
        cachorro = Cachorro(numero_chip, dados_cachorro["nome"], dados_cachorro["raca"], dados_cachorro["tamanho"])
        dados_cachorro["numero_chip"] = numero_chip
        self.__cachorros.append(cachorro)
        self.__tela_cachorros.mostra_mensagem("Animal cadastrado com sucesso no Sistema.")

    def listar_cachorros(self):
        tam_lista_cachorros = len(self.__cachorros)
        if tam_lista_cachorros > 0:
            for cachorro in self.__cachorros:
                self.__tela_cachorros.mostra_cachorro(
                    {
                        "numero_chip": cachorro.numero_chip,
                        "nome": cachorro.nome,
                        "raca": cachorro.raca,
                        "tamanho": cachorro.tamanho,
                        "vacinacao": cachorro.listar_vacinacao()
                    }
                )
        else:
            self.__tela_cachorros.mostra_mensagem(
                "ERRO: Não existe nenhum cachorro cadastrado no sistema."
            )
            self.__controlador_sistemas.abre_tela()

    def alterar_cachorro(self):
        self.listar_cachorros()
        numero_chip = self.__tela_cachorros.seleciona_cachorro()
        cachorro = self.pega_cachorro_por_numero_chip(numero_chip)

        if cachorro is not None:
            novos_dados_cachorro = self.__tela_cachorros.pega_dados_cachorro()
            cachorro.nome = novos_dados_cachorro["nome"]
            cachorro.raca = novos_dados_cachorro["raca"]
            cachorro.tamanho = novos_dados_cachorro["tamanho"]
            self.listar_cachorros()
        else:
            self.__tela_cachorros.mostra_mensagem("ERRO: O cachorro não existe.")
            self.__tela_cachorros.tela_opcoes()

    def excluir_cachorro(self):
        self.listar_cachorros()
        numero_chip = self.__tela_cachorros.seleciona_cachorro()
        cachorro = self.pega_cachorro_por_numero_chip(numero_chip)

        if cachorro is not None:
            self.__cachorros.remove(cachorro)
            self.__tela_cachorros.mostra_mensagem(
                f"O cachorro de numero chip: {numero_chip} foi excluido do sistema"
            )
            if len(self.__cachorros) == 0:
                self.__tela_cachorros.mostra_mensagem(
                    "Não existe mais nenhum cachorro cadastrado no sistema"
                )
            else:
                self.__tela_cachorros.tela_opcoes()
        else:
            self.__tela_cachorros.mostra_mensagem("ERRO: O cachorro não existe.")
            self.__tela_cachorros.tela_opcoes()

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
            opcao_escolhida = self.__tela_cachorros.tela_opcoes()
            while opcao_escolhida not in (1, 2, 3, 4, 0):
                self.__tela_cachorros.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_cachorros.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()