from datetime import date
from utils import verifica_cpf
from exception.CPFException import CPFException


class TelaDoacao:
    def tela_opcoes(self):
        print("-------- DOAÇÃO --------")
        print("Escolha a opcao")
        print("1 - Incluir de doação")
        print("2 - Listar de doação")
        print("3 - Excluir de doação")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def seleciona_gato_ou_cachorro(self):
        print("Foi um gato ou um cachorro que foram doado?")
        print("1 - Gato")
        print("2 - Cachorro")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pegar_dados_doacao(self):
        print("-------- DADOS DE DOAÇÃO --------")
        cpf_doador = input("Cpf do doador: ")
        while True:
            try:
                verifica_cpf(cpf_doador)
                break
            except CPFException:
                print("O CPF digitado é inválido. Por favor, digite novamente.")
            cpf_doador = input("Cpf do doador: ")

        numero_chip_animal = int(input("Numero do chip do animal a ser doado: "))
        motivo = input("Motivo doação: ")
        return {"cpf": cpf_doador, "numero_chip": numero_chip_animal, "motivo": motivo}

    def mostrar_doacao(self, dados_doacao):
        print("ID REGISTRO DE DOAÇÃO: ", dados_doacao["id_registro"])
        print("DATA DE DOAÇÃO: ", dados_doacao["data_de_doacao"])
        print("NOME DO DOADOR: ", dados_doacao["nome_doador"])
        print("NOME DO ANIMAL: ", dados_doacao["nome_animal"])
        print("MOTIVO DA DOAÇÃO: ", dados_doacao["motivo"])
        print("\n")

    def seleciona_doacao(self):
        contrato_de_doacao = input("codigo do registro que deseja selecionar: ")
        return contrato_de_doacao

    def mostra_mensagem(self, msg):
        print(msg)
