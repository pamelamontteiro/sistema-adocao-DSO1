from datetime import datetime, date

class TelaVacinacao:
    def tela_opcoes(self):
        print("-------- VACINAÇÃO --------")
        print("Escolha a opção:")
        print("1 - Incluir vacinação")
        print("2 - Alterar vacinação")
        print("3 - Listar vacinações")
        print("4 - Excluir vacinação")
        print("0 - Retornar")
        
        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_data_vacinacao(self):
        while True:
            data_vacinacao_input = input("Digite a data de vacinação (dd-mm-aaaa): ")
            try:
                data_vacinacao = datetime.strptime(data_vacinacao_input, "%d-%m-%Y").date()
                return {"data_vacinacao": data_vacinacao}  # Mover o return para fora do while
            except ValueError:
                print("Data inválida. Por favor, use o formato dd-mm-aaaa.")

    def seleciona_vacinacao(self):
        codigo_vacinacao = int(input("Digite o código da vacinação que deseja selecionar: "))
        return codigo_vacinacao

    def mostra_vacinacao(self, dados_vacinacao):
        print("------------------------------------")
        print("NOME DA VACINA: ", dados_vacinacao["nome_vacina"])
        print("CÓDIGO DA VACINAÇÃO: ", dados_vacinacao["codigo_vacinacao"])
        print("DATA DA VACINAÇÃO: ", dados_vacinacao["data_vacinacao"].strftime("%d-%m-%Y"))  # Formata a data para exibição

    def mostra_mensagem(self, msg):
        print(msg)
