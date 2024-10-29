from datetime import date
from uuid import uuid4
from entidades.doacao import Doacao
from telas.tela_doacao import TelaDoacao


class ControladorDoacao:
    def __init__(self, controlador_sistemas):
        self.__controlador_sistemas = controlador_sistemas
        self.__doacao = [] # Lista para armazenar as doações
        self.__tela_doacao = TelaDoacao()

    def pega_doacao_por_id(self, id: int):
    # Busca uma doação na lista pelo ID do registro
        for doacao in self.__doacao:
            if doacao.id_registro == id:
                return doacao
        return None  # Retorna None se não encontrar

    def pega_doacao_por_doador(self, doador): # Busca uma doação na lista pelo CPF do doador
        for doacao in self.__doacao:
            if doacao.doador.cpf == doador.cpf:
                return doacao
        return None

    def incluir_doacao(self):  # Inicia o processo de inclusão de uma nova doação
        gato_ou_cachorro = self.__tela_doacao.seleciona_gato_ou_cachorro()
        while True:  # Valida a escolha entre gato (1) e cachorro (2)
            if gato_ou_cachorro not in (1, 2):
                self.__tela_doacao.mostra_mensagem("Opção inválida! Selecione 1 ou 2!")
                gato_ou_cachorro = self.__tela_doacao.seleciona_gato_ou_cachorro()
            else:
                break

        if gato_ou_cachorro == 1: # Processa a doação de um gato
            self.__controlador_sistemas.controlador_gatos.listar_gatos()
            self.__controlador_sistemas.controlador_doador.listar_doadores()
            self.__tela_doacao.mostra_mensagem(
                "Precisamos do CPF do doador, o número do chip do gato e o motivo da doação:"
            )
            dados_doacao = self.__tela_doacao.pega_dados_doacao()
            motivo = dados_doacao["motivo"]
            doador = (
                self.__controlador_sistemas.controlador_doador.pegar_doador_por_cpf(
                    dados_doacao["cpf"]
                )
            ) # Busca o doador pelo CPF
            gato = (
                self.__controlador_sistemas.controlador_gatos.pega_gato_por_numero_chip(
                    dados_doacao["numero_chip"]
                )
            )# Busca o gato pelo número do chip
            if doador is not None and gato is not None:
                 # Se o doador e o gato forem válidos, cria a doação
                id_registro = uuid4().int # Gera um ID único para a doação
                data_de_doacao = date.today()
                doacao = Doacao(id_registro, data_de_doacao, gato, doador, motivo)
                self.__doacao.append(doacao) # Adiciona a doação à lista
                self.__tela_doacao.mostra_mensagem(
                    f"Inclusão de registro de doação realizada com sucesso."
                )
            else:
                self.__tela_doacao.mostra_mensagem(
                    "Informações de doador ou chip animal invalidas, tente novamente."
                )

        elif gato_ou_cachorro == 2: # Processa a doação de um cachorro
            self.__controlador_sistemas.controlador_cachorros.listar_cachorros()
            self.__controlador_sistemas.controlador_doador.listar_doadores()
            self.__tela_doacao.mostra_mensagem(
                "Precisamos do CPF do doador, o número do chip do cachorro e o motivo da doação:"
            )
            dados_doacao = self.__tela_doacao.pega_dados_doacao()
            doador = (
                self.__controlador_sistemas.controlador_doador.pegar_doador_por_cpf(
                    dados_doacao["cpf"]
                )
            )
            cachorro = self.__controlador_sistemas.controlador_cachorros.pega_cachorro_por_numero_chip(
                dados_doacao["numero_chip"]
            ) # Busca o cachorro pelo número do chip

            if doador is not None and cachorro is not None: # Se o doador e o cachorro forem válidos, cria a doação
                id_registro = uuid4().int

                data_de_doacao = date.today()
                doacao = Doacao(
                    id_registro,
                    data_de_doacao,
                    cachorro,
                    doador,
                    dados_doacao["motivo"],
                )
                self.__doacao.append(doacao)
                self.__tela_doacao.mostra_mensagem(
                    f"Inclusão de registro de doação realizada com sucesso!"
                )
            else:
                self.__tela_doacao.mostra_mensagem(
                    "Informações de doador ou chip animal invalidas, tente novamente."
                )

    def listar_doacao(self): # Lista todas as doações e exibe suas informações
        for doacao in self.__doacao:
            self.__tela_doacao.exibir_doacao(
                {
                    "id_registro": doacao.id_registro,
                    "data_de_doacao": doacao.data_de_doacao,
                    "nome_doador": doacao.doador.cpf,
                    "motivo": doacao.motivo,
                }
            )

    def excluir_doacao(self): # Inicia o processo de exclusão de uma doação
        self.listar_doacao() # Lista as doações disponíveis
        id_registro_doacao = self.__tela_doacao.pega_motivo_doacao()  # Pede o ID da doação a ser excluída
        doacao = self.pega_doacao_por_id(int(id_registro_doacao)) # Busca a doação pelo ID

        if doacao is not None:
            # Se a doação for encontrada, remove da lista
            self.__doacao.remove(doacao)
            self.__tela_doacao.mostra_mensagem(
                f"Doação com ID {id_registro_doacao} removido com sucesso."
            )
            self.listar_doacao()
        else:
            self.__tela_doacao.mostra_mensagem("ATENCAO: Id não existente")

    def gerar_relatorio_doacao(self):
        data_inicial = self.__tela_doacao.pega_datas_relatorio("Data Inicial")
        data_final = self.__tela_doacao.pega_datas_relatorio("Data Final")
        cont = 0
        for contrato_adocao in self.__doacao:
            if (
                contrato_adocao.data_de_doacao > data_inicial
                and contrato_adocao.data_de_doacao < data_final
            ):
                cont += 1
        self.__tela_doacao.mostra_mensagem(
            f"Entre {data_inicial} e {data_final} foram adotados {cont} animais."
        )

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_doacao,
            2: self.listar_doacao,
            3: self.excluir_doacao,
            4: self.gerar_relatorio_doacao,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_doacao.tela_opcoes()
            while opcao_escolhida not in (1, 2, 3, 4, 0):
                self.__tela_doacao.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_doacao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()