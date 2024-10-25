from entidades.adocao import Adocao
from telas.tela_adocao import TelaAdocao
from uuid import uuid4
from datetime import datetime
from datetime import date


class ControladorAdocao:
    def __init__(self, controlador_sistemas):
        self.__controlador_sistemas = controlador_sistemas
        self.__adocao = []  # Lista para armazenar adoções
        self.__tela_adocao = TelaAdocao()  # Objeto da tela de adoção

    def pega_adocao_por_codigo(self, codigo: int):
        for adocao in self.__adocao:
            if adocao.id_registro == codigo:
                return adocao
        return None

    # Verifica se o tipo de habitação do adotante é adequado para o animal
    def verifica_tipo_habitacao(self, adotante, animal):
        if (
            animal.tamanho == "G"
            and str(adotante.tipo_habitacao) == "apartamento pequeno"
        ):
            verifica = False
        else:
            verifica = True

        if (
            verifica
        ):  # Se a verificação falhar, mostra uma mensagem de aviso na tela e chama o método retornar
            return True
        else:
            self.__tela_adocao.mostra_mensagem(
                f"ATENÇAO: O tipo de habitação é inadequado."
            )  # Exibe a mensagem de erro na interface de adoção
            self.retornar()

    def verifica_maior_idade(self, data_nascimento):
        data_atual = datetime.now().date()
        idade_minima = 18
        try:
            data_formatada = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            diferenca_anos = data_atual.year - data_formatada.year
            if (data_atual.month, data_atual.day) < (
                data_formatada.month,
                data_formatada.day,
            ):
                diferenca_anos -= 1
            if diferenca_anos >= idade_minima:
                verifica = True
            else:
                verifica = False
        except ValueError:
            self.__tela_adocao.mostra_mensagem(
                "Formato de data inválido. Utilize o formato dd/mm/aaaa."
            )
        if verifica:
            return True
        else:
            self.__tela_adocao.mostra_mensagem(
                f"ATENÇAO: Somente maiores de idade podem adotar."
            )
            self.retornar()

    # TODO: a parte controle de doação não foi feita, arrumar o codigo depois
    def verifica_se_nao_doou(self, adotante):
        if (
            self.__controlador_sistema.controlador_doacao.pega_doacao_por_doador(
                adotante
            )
            is None
        ):
            verifica = True
        else:
            verifica = False

        if verifica:
            return True
        else:
            self.__tela_adocao.mostra_mensagem(
                f"ATENÇAO: O adotante já fez uma doaçao e não pode adotar."
            )
            self.retornar()

    # TODO: A tela vVacina e Vacinão não esta feita, depois verificar essa parte do codigo
    def verifica_vacinas(self, animal):
        quantidade_vacina = len(animal.vacinacao)
        if quantidade_vacina == 3:
            verifica = True
        else:
            verifica = False

        if verifica:
            return True
        else:
            self.__tela_adocao.mostra_mensagem(
                f"ATENÇAO: O animal não tem as três vacinas necessárias."
            )
            self.retornar()

    def incluir_adocao(self):
        gato_ou_cachorro = self.__tela_adocao.seleciona_gato_ou_cachorro()
        while True:
            if gato_ou_cachorro not in (1, 2):
                self.__tela_adocao.mostra_mensagem("Opção inválida! Selecione 1 ou 2!")
                gato_ou_cachorro = self.__tela_adocao.seleciona_gato_ou_cachorro()
            else:
                break
        self.__controlador_sistemas.controlador_adotantes.listar_adotantes()

        # TODO: Precisa fazer a parte da adoção do cachorro, controladores e telas de cachorros, ainda não foram feitos, verificar depois
        if gato_ou_cachorro == 1:
            self.__controlador_sistemas.controlador_gatos.listar_gatos()
            dados_adocao = self.__tela_adocao.pega_dados_adocao()
            adotante = (
                self.__controlador_sistemas.controlador_adotantes.pega_adotante_por_cpf(
                    dados_adocao["cpf"]
                )
            )
            gato = self.__controlador_sistemas.controlador_gatos.pega_gato_por_num_chip(
                dados_adocao["numero_chip"]
            )
            if adotante is not None and gato is not None:
                # Faz as verificaçoes necessarias para adoçao
                self.verifica_maior_idade(adotante.data_nascimento)
                self.verifica_vacinas(gato)
                self.verifica_se_nao_doou(adotante)
                id_registro = uuid4().int
                data = date.today()
                adocao = Adocao(id_registro, data, gato, adotante, False)
                self.__adocao.append(adocao)
                # Coleta a assinatura do termo de responsabilidade
                self.assinar_termo_assinado(id_registro)
                self.__controlador_sistemas.controlador_gatos.gatos.remove(
                    gato
                )  
                self.__tela_adocao.mostra_mensagem(
                    f"Inclusão de adoção realizada com sucesso."
                )
            else:
                self.__tela_adocao.mostra_mensagem(
                    "ERRO: Os dados que você forneceu estão incorretos."
                )

    def listar_adocao(self):
        for adocao in self.__adocao:
            # inserir animal fazer metodo abstrato em animal
            self.__tela_adocao.exibir_adocao(
                {
                    "codigo_registro": adocao.id_registro,
                    "data": adocao.data_adocao,
                    "cpf_adotante": adocao.adotante.cpf,
                    "termo_responsabilidade": adocao.termo_assinado,
                }
            )

    # TODO: verificar depois essa função
    def excluir_adocao(self):
        self.listar_adocao()
        codigo_adocao = self.__tela_adocao.seleciona_adocao()
        adocao = self.pega_adocao_por_codigo(int(codigo_adocao))

        if adocao is not None:
            self.__adocao.remove(adocao)
            self.__tela_adocao.mostra_mensagem(
                f"Registro de adoção com código {codigo_adocao} removido com sucesso."
            )
            self.listar_adocao()
        else:
            self.__tela_adocao.mostra_mensagem("ATENCAO: ID de Adoção não existente")

    def assinar_termo_assinado(self, id_adocao):
        adocao = self.pega_adocao_por_codigo(id_adocao)
        if adocao is not None:
            while True:
                termo_assinado = self.__tela_adocao.pega_assinatura_termo_assinado()
                if termo_assinado.upper() == "S":
                    termo_assinado = True
                    adocao.termo_assinado = termo_assinado
                    self.__tela_adocao.mostra_mensagem(
                        "Termo de responsabilidade assinado com sucesso!"
                    )
                    break
                else:
                    self.__tela_adocao.mostra_mensagem(
                        "ATENÇAO: Você deve assinar o termo para seguir com a adoção. Adoção cancelado."
                    )
                    self.__adocao.remove(adocao)
                    self.retornar()
        else:
            self.__tela_adocao.mostra_mensagem(
                "A adoção nao esta cadastrado no Sistema."
            )

    def gerar_relatorio_adocao(self):
        # Dados quantidade de animais adotados por periodo
        data_inicial = self.__tela_adocao.pega_datas_relatorio("Data Inicial")
        data_final = self.__tela_adocao.pega_datas_relatorio("Data Final")
        cont = 0
        for processo in self.__adocao:
            if processo.data > data_inicial and processo.data < data_final:
                cont += 1
        self.__tela_adocao.mostra_mensagem(
            f"Entre {data_inicial} e {data_final} foram adotados {cont} animais."
        )
        # Dados animais disponiveis para adoçao
        self.__tela_adocao.mostra_mensagem(
            "-------- ANIMAIS DISPONÍVEIS PARA ADOÇAO --------"
        )
        self.__tela_adocao.mostra_mensagem("-------- GATOS --------")
        tam_lista_gatos = len(self.__controlador_sistemas.controlador_gatos.gatos)
        if tam_lista_gatos > 0:
            self.__controlador_sistemas.controlador_gatos.listar_gatos()
        else:
            self.__tela_adocao.mostra_mensagem(
                "ATENÇAO: Não existe nenhum gato disponivel para adoçao."
            )
        # TODO: fazer a parte do relatorio da adoção do cachorro
        # self.__tela_adocao.mostra_mensagem(
        #     "-------- CACHORROS --------")

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_adocao,
            2: self.listar_adocao,
            3: self.excluir_adocao,
            4: self.gerar_relatorio_adocao,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_adocao.tela_opcoes()
            while opcao_escolhida not in (1, 2, 3, 4, 0):
                self.__tela_adocao.mostra_mensagem(
                    "ERRO: Opção inválida, tente novamente."
                )
                opcao_escolhida = self.__tela_adocao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
