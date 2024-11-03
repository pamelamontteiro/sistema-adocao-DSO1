from datetime import datetime
from entidades.adotante import Adotante
from telas.tela_adotante import TelaAdotante


class ControladorAdotantes:
    def __init__(self, controlador_sistemas):
        self.__adotantes = []
        self.__tela_adotante = TelaAdotante()
        self.__controlador_sistemas = controlador_sistemas

    def pega_adotante_por_cpf(self, cpf: int):
        for adotante in self.__adotantes:
            if adotante.cpf == cpf:
                return adotante
        return None

    def incluir_adotante(self):
        dados_adotante = self.__tela_adotante.pega_dados_adotante()
        tipo_habitacao = (
            self.__controlador_sistemas.controlador_tipo_habitacao.incluir_tipo_habitacao()
        )
        try:
            cpf_valido = self.pega_adotante_por_cpf(dados_adotante["cpf"])
            if cpf_valido is not None:
                raise Exception
            tem_outros_animais = dados_adotante["tem_outros_animais"].upper()
            if tem_outros_animais == "S" or tem_outros_animais == "N":
                if tem_outros_animais == "S":
                    tem_outros_animais = True
                else:
                    tem_outros_animais = False
                adotante = Adotante(
                    dados_adotante["cpf"],
                    dados_adotante["nome"],
                    datetime.strptime(dados_adotante["data_nascimento"], "%d/%m/%Y"),
                    dados_adotante["endereco"],
                    tem_outros_animais,
                    tipo_habitacao,
                )
                self.__adotantes.append(adotante)
                self.__tela_adotante.mostra_mensagem(
                    "Adotante cadastrado com sucesso no sistema."
                )
            else:
                self.__tela_adotante.mostra_mensagem(
                    "ERRO: Informações inválidas, digite novamente os dados:"
                )
                self.__tela_adotante.pega_dados_adotante()  # nao seria necessario um while(?)
        except Exception:
            self.__tela_adotante.mostra_mensagem(
                "ERRO: O Adotante ja esta cadastrado no Sistema."
            )

    def listar_adotantes(self):
        tam_lista_adotantes = len(self.__adotantes)
        if tam_lista_adotantes > 0:
            for adotante in self.__adotantes:
                self.__tela_adotante.mostra_adotante(
                    {
                        "cpf": adotante.cpf,
                        "nome": adotante.nome,
                        "data_nascimento": adotante.data_nascimento,
                        "endereco": adotante.endereco,
                        "tem_outros_animais": adotante.tem_outros_animais,
                        "tipo_habitacao": adotante.tipo_habitacao,
                    }
                )
        else:
            self.__tela_adotante.mostra_mensagem(
                "ATENÇÃO: não existe nenhum adotante cadastrado no Sistema."
            )
            self.__controlador_sistemas.abre_tela()

    def alterar_adotante(self):
        self.listar_adotantes()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        try:
            adotante = self.pega_adotante_por_cpf(cpf_adotante)
            if adotante is None:
                raise Exception
            novos_dados_adotante = self.__tela_adotante.pega_dados_adotante()
            novo_tipo_habitacao = (
                self.__controlador_sistemas.controlador_tipo_habitacao.incluir_tipo_habitacao()
            )
            adotante.nome = novos_dados_adotante["nome"]
            adotante.data_nascimento = novos_dados_adotante["data_nascimento"]
            adotante.endereco = novos_dados_adotante["endereco"]
            adotante.tem_outros_animais = novos_dados_adotante["tem_outros_animais"]
            adotante.tipo_habitacao = novo_tipo_habitacao
            self.__tela_adotante.mostra_mensagem(
                "Dados do Adotante alterados com sucesso."
            )
            self.listar_adotantes()
        except Exception:
            self.__tela_adotante.mostra_mensagem("ERRO: O Adotante não existe.")

    def excluir_adotante(self):
        self.listar_adotantes()
        cpf_adotante = self.__tela_adotante.seleciona_adotante()
        try:
            adotante = self.pega_adotante_por_cpf(cpf_adotante)
            if adotante is None:
                raise Exception
            self.__adotantes.remove(adotante)
            self.__tela_adotante.mostra_mensagem(
                f"Adotante de cpf: {cpf_adotante} foi excluido do sistema."
            )
            if len(self.__adotantes) == 0:
                self.__tela_adotante.mostra_mensagem(
                    f"Não existe mais nenhum adotante cadastrado no sistema."
                )
            else:
                self.__tela_adotante.tela_opcoes()
        except Exception:
            self.__tela_adotante.mostra_mensagem("ERRO: O Adotante não existe.")
            self.__tela_adotante.tela_opcoes()

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adotante,
            2: self.alterar_adotante,
            3: self.listar_adotantes,
            4: self.excluir_adotante,
            0: self.retornar,
        }
        while True:
            opcao_escolhida = self.__tela_adotante.tela_opcoes()
            while opcao_escolhida not in (1, 2, 3, 4, 0):
                self.__tela_adotante.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_adotante.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
