from datetime import date


class TelaDoacao:
    def tela_opcoes(self):
        print("-------- REGISTRO DE DOAÇÃO --------")
        print("Escolha a opcao")
        print("1 - Incluir doação")
        print("2 - Listar doação")
        print("3 - Excluir doação")
        print("4 - Gerar relatório de doação")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def seleciona_gato_ou_cachorro(self):
        print("Um cachorro um gato será doado?")
        print("1 - Gato")
        print("2 - Cachorro")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_doacao(self):
        print("-------- DADOS DE DOAÇÃO --------")
        cpf_doador = input("Cpf do doador: ")
        numero_chip_animal = int(input("Numero do chip do animal: "))
        data = self.pega_data_doacao
        motivo = self.pega_motivo_doacao
        return {"cpf": cpf_doador, "numero_chip": numero_chip_animal, "data": data, "motivo": motivo}

    def exibir_doacao(self, dados_doacao):
        print("ID  DE DOAÇÃO: ", dados_doacao["id_registro"])
        print("CPF DO DOADOR PARA DOAÇÃO: ", dados_doacao["cpf_doador"])
        print("DATA DE DOAÇÃO: ", dados_doacao["data_doacao"])
        print("MOTIVO DA DOAÇÃO: ", dados_doacao["motivo_doacao"])

    def seleciona_contrato_doacao(self):
        contrato_doacao = int(
            input("Código do contrato de doação - id, que deseja selecionar: ")
        )
        return contrato_doacao

    def pega_motivo_doacao(self):
        motivo_doacao = input("Descreva o motivo da doação: ")
        return motivo_doacao

    def pega_data_doacao(self, text):
        print(f"Digite a {text} do período:")
        dia = input("Dia: ")
        mes = input("Mês: ")
        ano = input("Ano: ")
        data = date(int(ano), int(mes), int(dia))
        return data

    def mostra_mensagem(self, msg):
        print(msg)
