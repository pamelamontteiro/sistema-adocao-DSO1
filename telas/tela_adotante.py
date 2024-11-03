from utils import verifica_cpf, verifica_nome
from exception.CPFException import CPFException
from exception.NomeException import NomeException
from datetime import datetime


class TelaAdotante:
    def tela_opcoes(self):
        print("-------- ADOTANTE --------")
        print("Escolha a opcao")
        print("1 - Incluir adotante")
        print("2 - Alterar adotante")
        print("3 - Listar adotantes")
        print("4 - Excluir adotante")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_adotante(self):
        print("-------- DADOS ADOTANTE --------")

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

        tem_outros_animais = input("Possui outros animais?(S/N) ")

        return {
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
            "tem_outros_animais": tem_outros_animais,
        }

    def mostra_adotante(self, dados_adotante):
        print("------------------------------------")
        print("CPF DO ADOTANTE: ", dados_adotante["cpf"])
        print("NOME DO ADOTANTE: ", dados_adotante["nome"])
        print(
            "DATA DE NASCIMENTO DO ADOTANTE: ",
            dados_adotante["data_nascimento"].strftime("%d/%m/%Y"),
        )
        print("ENDERECO DO ADOTANTE: ", dados_adotante["endereco"])
        print("OUTROS ANIMAIS: ", dados_adotante["tem_outros_animais"])
        print("TIPO DE HABITACAO: ", dados_adotante["tipo_habitacao"])

    def seleciona_adotante(self):
        cpf = input("CPF do adotante que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
