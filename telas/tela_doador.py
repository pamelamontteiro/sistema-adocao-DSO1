class TelaDoador:
    def tela_opcoes(self):
        print("-------- DOADOR --------")
        print("Escolha a opcao")
        print("1 - Incluir doador")
        print("2 - Alterar doador")
        print("3 - Listar doadors")
        print("4 - Excluir doador")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_doador(self):
        print("-------- DADOS DOADOR --------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nascimento = input("Data de nascimento: ")
        endereco = input("Endereço: ")
        return {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
        }

    def mostra_doador(self, dados_doador):
        print("------------------------------------")
        print("NOME DO DOADOR: ", dados_doador["nome"])
        print("CPF DO DOADOR: ", dados_doador["cpf"])
        print("NASCIMENTO DO DOADOR: ", dados_doador["data_nascimento"])
        print("ENDEREÇO DO DOADOR: ", dados_doador["endereco"])

    def seleciona_doador(self):
        cpf = input("CPF do doador que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
