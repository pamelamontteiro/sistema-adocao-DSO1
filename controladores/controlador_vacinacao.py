from entidades.vacinacao import Vacinacao
from entidades.vacina import Vacina
from telas.tela_vacinacao import TelaVacinacao
from controladores.controlador_vacina import ControladorVacina
from datetime import date

class ControladorVacinacao:
    def __init__(self, controlador_sistemas):
        self.__tela_vacinacao = TelaVacinacao()
        self.__controlador_vacina = ControladorVacina(controlador_sistemas)
        self.__controlador_sistemas = controlador_sistemas
        self.__vacinacoes = []

    def incluir_vacinacao(self):
        dados_vacinacao = self.__tela_vacinacao.pega_data_vacinacao()
        vacina_selecionada = self.__controlador_vacina.selecionar_vacina()
    
        if vacina_selecionada is not None:
            vacinacao = Vacinacao(dados_vacinacao["data_vacinacao"], vacina_selecionada)
            self.__vacinacoes.append(vacinacao)
            self.__tela_vacinacao.mostrar_mensagem("Vacinação incluída com sucesso!")
        else:
            self.__tela_vacinacao.mostrar_mensagem("Nenhuma vacina selecionada.")

    def alterar_vacinacao(self):
        if not self.__vacinacoes:
            self.__tela_vacinacao.mostrar_mensagem("Nenhuma vacinação cadastrada para alterar.")
            return
    
        codigo_vacinacao = self.__tela_vacinacao.seleciona_vacinacao()
        vacinacao = self.obter_vacinacao_por_codigo(codigo_vacinacao)
    
        if vacinacao:
            nova_data = self.__tela_vacinacao.pega_data_vacinacao()["data_vacinacao"]
            vacinacao.data_de_vacinacao = nova_data
            self.__tela_vacinacao.mostrar_mensagem("Data de vacinação alterada com sucesso!")
            
            nova_vacina = self.__controlador_vacina.selecionar_vacina()
            if nova_vacina is not None:
                vacinacao.vacina = nova_vacina
                self.__tela_vacinacao.mostrar_mensagem("Vacina alterada com sucesso!")
            else:
                self.__tela_vacinacao.mostrar_mensagem("Nenhuma vacina selecionada.")
        else:
            self.__tela_vacinacao.mostrar_mensagem("Vacinação não encontrada.")

    def listar_vacinacao(self):
        if self.__vacinacoes:
            for vacinacao in self.__vacinacoes:
                self.__tela_vacinacao.mostra_vacinacao(
                    {
                        "nome_vacina": vacinacao.vacina.nome_vacina,
                        "codigo_vacinacao": vacinacao.vacina.codigo_vacina,
                        "data_vacinacao": vacinacao.data_de_vacinacao
                    }
                )
        else:
            self.__tela_vacinacao.mostrar_mensagem("ERRO: Não existe nenhuma vacinação cadastrada no sistema.")
            self.__controlador_sistemas.abre_tela()
    
    def excluir_vacinacao(self):
        if not self.__vacinacoes:
            self.__tela_vacinacao.mostrar_mensagem("Nenhuma vacinação cadastrada para excluir.")
            return
        
        codigo_vacinacao = self.__tela_vacinacao.seleciona_vacinacao()
        vacinacao = self.obter_vacinacao_por_codigo(codigo_vacinacao)
        
        if vacinacao:
            self.__vacinacoes.remove(vacinacao)
            self.__tela_vacinacao.mostrar_mensagem("Vacinação excluída com sucesso!")
        else:
            self.__tela_vacinacao.mostrar_mensagem("Vacinação não encontrada.")

    def obter_vacinacao_por_codigo(self, codigo):
        for vacinacao in self.__vacinacoes:
            if vacinacao.vacina.codigo_vacina == codigo:
                return vacinacao
        return None

    def retornar(self):
        self.__controlador_sistemas.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_vacinacao,
            2: self.alterar_vacinacao,
            3: self.listar_vacinacao,
            4: self.excluir_vacinacao,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_vacinacao.tela_opcoes()
            if opcao_escolhida in lista_opcoes:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
            else:
                self.__tela_vacinacao.mostrar_mensagem("ERRO: Opção inválida, tente novamente.")
