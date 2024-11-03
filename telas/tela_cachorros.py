class TelaCachorro:
    def tela_opcoes(self):
        print("-------- CACHORRO --------")
        print("1 - Incluir cachorro")
        print("2 - Alterar cachorro")
        print("3 - Listar cachorros")
        print("4 - Excluir cachorro")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def tamanho_cachorro(self):
        print("-------- TAMANHO CACHORRO --------")
        print("P - Cachorro pequeno")
        print("M - Cachorro médio")
        print("G - Cachorro grande")
        opcao = input("Escolha a opcao: ")
        return opcao

    def pega_dados_cachorro(self, racas):
        print("-------- DADOS CACHORRO --------")
        nome = input("Nome: ")
        raca = self.pega_raca_cachorro(racas)
        return {"nome": nome, "raca": raca}

    def pega_raca_cachorro(self, racas):
        print("Escolha a raça do cachorro")
        for idx, raca in enumerate(racas):
            print(f"{idx+1} - {raca}")

        opcao_raca = int(input("Escolha a raca: "))
        opcao_raca = opcao_raca - 1
        return racas[opcao_raca]

    def mostra_cachorro(self, dados_cachorro):
        print("------------------------------------")
        print("NOME DO CACHORRO: ", dados_cachorro["nome"])
        print("RAÇA DO CACHORRO: ", dados_cachorro["raca"])
        print("TAMANHO DO CACHORRO: ", dados_cachorro["tamanho"])
        print("NUMERO CHIP DO CACHORRO: ", dados_cachorro["numero_chip"])
        print("HISTÓRICO DE VACINAÇÃO DO CACHORRO: ", dados_cachorro["vacinacao"])

    def seleciona_cachorro(self):
        numero_chip = int(input("Numero do chip do cachorro que deseja selecionar: "))
        return numero_chip

    def mostra_mensagem(self, msg):
        print(msg)
