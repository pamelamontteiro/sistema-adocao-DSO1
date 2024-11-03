class TelaVacinacao:
    def tela_opcoes(self):
        print("-------- HISTÓRICO VACINAÇÃO --------")
        print("Escolha a opcao")
        print("1 - Incluir histórico de vacinação")
        print("2 - Listar históricos de vacinação")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def seleciona_gato_ou_cachorro(self):
        print("Um cachorro um gato será vacinado?")
        print("1 - Gato")
        print("2 - Cachorro")
        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_historico(self):
        print("-------- HISTÓRICO VACINAÇÃO --------")
        numero_chip_animal = int(input("Digite o número do chip do animal vacinado: "))
        return {"numero_chip_animal": numero_chip_animal}

    def mostra_vacinacao(self, dados_vacinacao):
        for vacinacao in dados_vacinacao:
            print("DATA VACINACAO: ", vacinacao["data_de_vacinacao"])
            print("ANIMAL: ", vacinacao["animal"])
            print("NOME DA VACINA: ", vacinacao["vacina"])
            print("\n")

    def mostra_mensagem(self, msg):
        print(msg)
