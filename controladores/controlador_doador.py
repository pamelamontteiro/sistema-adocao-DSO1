from entidades.doador import Doador
from telas.tela_doador import TelaDoador
from datetime import datetime


class ControladorDoadores:
    def __init__(self, controlador_sistemas):
        self.__doadores = []
        self.__tela_doador = TelaDoador()
        self.__controlador_sistemas = controlador_sistemas

    def pegar_doador_por_cpf(self, cpf: str):
        for doador in self.__doadores:
            if doador.cpf == cpf:
                return doador
        return None

    def incluir_doador(self):
        dados_doador = self.__tela_doador.pega_dados_doador()
        cpf_valido = self.pegar_doador_por_cpf(dados_doador["cpf"])
        if (
            cpf_valido is None
        ):  # Se não estiver cadastrado, cria um novo doador e adiciona à lista.
            doador = Doador(
                dados_doador["cpf"],
                dados_doador["nome"],
                datetime.strptime(dados_doador["data_nascimento"], "%d/%m/%Y").date(),
                dados_doador["endereco"],
            )
            self.__doadores.append(doador)
            self.__tela_doador.mostra_mensagem(
                "Doador cadastrado com sucesso no sistema."
            )
        else:
            # Se já estiver cadastrado, exibe mensagem de erro.
            self.__tela_doador.mostra_mensagem(
                "ERRO: o Doador ja esta cadastrado no Sistema."
            )

    def listar_doadores(self):
        tam_lista_doadores = len(self.__doadores)
        if tam_lista_doadores > 0:
            for doador in self.__doadores:
                self.__tela_doador.mostra_doador(
                    {
                        "nome": doador.nome,
                        "cpf": doador.cpf,
                        "data_nascimento": doador.data_nascimento,
                        "endereco": doador.endereco,
                    }
                )
        else:
            self.__tela_doador.mostra_mensagem(
                "ATENÇÃO: não existe nenhum doador cadastrado no Sistema."
            )
            self.__controlador_sistemas.abre_tela()

    def alterar_doador(self):
        self.listar_doadores()
        cpf_doador = self.__tela_doador.seleciona_doador()
        adotante = self.pegar_doador_por_cpf(cpf_doador)

        if adotante is not None:
            novos_dados_adotante = self.__tela_doador.pega_dados_doador()
            adotante.nome = novos_dados_adotante["nome"]
            adotante.cpf = novos_dados_adotante["cpf"]
            adotante.nascimento = novos_dados_adotante["data_nascimento"]
            adotante.endereco = novos_dados_adotante["endereco"]
            self.listar_doadores()
        else:
            # Se o doador não existe, exibe mensagem de erro.
            self.__tela_doador.mostra_mensagem("ERRO: O Adotante não existe.")

    def excluir_doador(self):
        self.listar_doadores()
        cpf_adotante = self.__tela_doador.seleciona_doador()
        adotante = self.pegar_doador_por_cpf(cpf_adotante)

        if adotante is not None:
            # Se o doador existe, remove da lista e confirma a exclusão
            self.__doadores.remove(adotante)
            self.__tela_doador.mostra_mensagem(
                f"Adotante de cpf: {cpf_adotante} foi excluido do sistema."
            )
            self.listar_doadores()
        else:
            # Se o doador não existe, exibe mensagem de erro.
            self.__tela_doador.mostra_mensagem("ERRO: O Adotante não existe.")

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        # Exibe as opções disponíveis para o usuário.
        lista_opcoes = {
            1: self.incluir_doador,
            2: self.alterar_doador,
            3: self.listar_doadores,
            4: self.excluir_doador,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_doador.tela_opcoes()
            while opcao_escolhida not in (1, 2, 3, 4, 0):
                self.__tela_doador.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_doador.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
