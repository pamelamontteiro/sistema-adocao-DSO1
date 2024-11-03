from datetime import date
from utils import verifica_cpf
from exception.CPFException import CPFException


class TelaAdocao:
    def tela_opcoes(self):
        print("-------- REGISTRO DE ADOÇÃO --------")
        print("Escolha a opcao")
        print("1 - Incluir adoção")
        print("2 - Listar adoção")
        print("3 - Excluir adoção")
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
        while True:
            try:
                verifica_cpf(cpf_adotante)
                break
            except CPFException:
                print("O CPF digitado é inválido. Por favor, digite novamente.")
            cpf_adotante = input("Cpf do adotante: ")

        numero_chip_animal = int(input("Numero do chip do animal: "))
        return {"cpf": cpf_adotante, "numero_chip": numero_chip_animal}

    def exibir_adocao(self, dados_adocao):
        print("ID  DE ADOÇÃO: ", dados_adocao["id_registro"])
        print("DATA DE ADOÇÃO: ", dados_adocao["data_adocao"])
        print(
            "STATUS DO TERMO DE RESPONSABILIDADE DE ADOÇÃO: ",
            dados_adocao["termo_assinado"],
        )
        print("CPF DO ADOTANTE PARA ADOÇÃO: ", dados_adocao["cpf_adotante"])

        print("\n")

    def seleciona_contrato_adocao(self):
        contrato_adocao = int(
            input("Código do contrato de adoção - id, que deseja selecionar: ")
        )
        return contrato_adocao

    def pega_assinatura_termo_assinado(self):
        termo_assinado = input("Assinar termo de responsabilidade?(S/N) ")
        return termo_assinado

    def mostra_mensagem(self, msg):
        print(msg)
