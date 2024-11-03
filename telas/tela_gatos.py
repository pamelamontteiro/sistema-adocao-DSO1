class TelaGato:
    def tela_opcoes(self):
        print("-------- GATO --------")
        print("Escolha a opcao")
        print("1 - Incluir gato")
        print("2 - Alterar gato")
        print("3 - Listar gatos")
        print("4 - Excluir gato")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_gato(self, racas):
        print("-------- DADOS GATO --------")
        nome = input("Nome: ")
        raca = self.pega_raca_gato(racas)
        return {"nome": nome, "raca": raca}

    def pega_raca_gato(self, racas):
        print("Escolha a raça do gato")
        for idx, raca in enumerate(racas):
            print(f"{idx+1} - {raca}")

        opcao_raca = int(input("Escolha a raca: "))
        opcao_raca = opcao_raca - 1
        return racas[opcao_raca]

    def mostra_gato(self, dados_gato):
        print("------------------------------------")
        print("NOME DO GATO: ", dados_gato["nome"])
        print("RAÇA DO GATO: ", dados_gato["raca"])
        print("NUMERO CHIP DO GATO: ", dados_gato["numero_chip"])
        print("HISTORICO VACINAÇÃO DO GATO: ", dados_gato["vacinacao"])

    def seleciona_gato(self):
        numero_chip = int(
            input("Numero do chip do gato que deseja selecionar: ").strip()
        )
        return numero_chip

    def mostra_mensagem(self, msg):
        print(msg)
