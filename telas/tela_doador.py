from utils import verifica_cpf, verifica_nome
from exception.CPFException import CPFException
from exception.NomeException import NomeException
from datetime import datetime


class TelaDoador:
    def tela_opcoes(self):
        print("-------- DOADOR --------")
        print("Escolha a opcao")
        print("1 - Incluir doador")
        print("2 - Alterar doador")
        print("3 - Listar doadores")
        print("4 - Excluir doador")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_doador(self):
        print("-------- DADOS DOADOR --------")

        cpf = input("CPF (XXX.XXX.XXX-XX): ")
        while True:
            try:
                verifica_cpf(cpf)
                break
            except CPFException:
                print("O CPF digitado é inválido. Por favor, digite novamente.")
            cpf = input("CPF (XXX.XXX.XXX-XX): ")

        nome = input("Nome completo: ")
        while True:
            try:
                verifica_nome(nome)
                break
            except NomeException:
                print("Nome precisa ser completo e não pode conter números.")
            nome = input("Nome completo: ")

        data_nascimento = input("Data de nascimento: ")
        while True:
            try:
                datetime.strptime(data_nascimento, "%d/%m/%Y")
                break
            except ValueError:
                print("Data de nascimento inválida. Por favor, digite novamente.")
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
