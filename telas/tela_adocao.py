from datetime import date


class TelaRegistroAdocao():
    def tela_opcoes(self):
        print("-------- REGISTRO DE ADOÇÃO --------")
        print("Escolha a opcao")
        print("1 - Incluir de adoção")
        print("2 - Listar de adoção")
        print("3 - Excluir de adoção")
        print("4 - Gerar relatório de adoção")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def seleciona_gato_ou_cachorro(self):
        print("Um cachorro um gato será adotado?")
        print("1 - Gato")
        print("2 - Cachorro")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_adocao(self):
        print("-------- DADOS De ADOÇÃO --------")
        cpf_adotante = input("Cpf do adotante: ")
        numero_chip_animal = int(input("Numero do chip do animal: "))
        return {"cpf": cpf_adotante, "numero_chip": numero_chip_animal}

    def exibir_adocao(self, dados_adocao):
        print("ID  DE ADOÇÃO: ",
              dados_adocao["id_registro"])
        print("DATA DE ADOÇÃO: ", dados_adocao["data_adocao"])
        print("STATUS DO TERMO DE RESPONSABILIDADE DE ADOÇÃO: ",
              dados_adocao["termo_assinado"])
        print("CPF DO ADOTANTE PARA ADOÇÃO: ",
              dados_adocao["cpf_adotante"])

        print("\n")

    def seleciona_registro_adocao(self):
        contrato_adocao  = int(input("Código do contrato de adoção - id, que deseja selecionar: "))
        return contrato_adocao 

    def pega_assinatura_termo_responsabilidade(self):
        assinatura = input("Assinar termo de responsabilidade?(S/N) ")
        return assinatura

    def pega_datas_relatorio(self, text):
        print(f'Digite a {text} do período:')
        dia = input("Dia: ")
        mes = input("Mês: ")
        ano = input("Ano: ")
        data = date(int(ano), int(mes), int(dia))
        return data

    def mostra_mensagem(self, msg):
        print(msg)