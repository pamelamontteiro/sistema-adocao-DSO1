from datetime import datetime


class TelaRelatorio:
    def tela_opcoes(self):
        print("-------- RELATÓRIOS --------")
        print("Escolha sua opção")
        print("1 - Relatório de animais")
        print("2 - Relatório de doações")
        print("3 - Relatório de adoções")
        print("0 - Voltar")

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_datas_relatorio(self):
        print("Digite a data inicial e final do período do relatório.")
        data_inicial = input("Digite a data inicial (dd/mm/aaaa): ")
        while True:
            try:
                datetime.strptime(data_inicial, "%d/%m/%Y")
                break
            except ValueError:
                print("Data inválida. Por favor, digite novamente.")
            data_inicial = input("Digite a data inicial (dd/mm/aaaa): ")

        data_final = input("Digite a data final (dd/mm/aaaa): ")
        while True:
            try:
                datetime.strptime(data_final, "%d/%m/%Y")
                break
            except ValueError:
                print("Data inválida. Por favor, digite novamente.")
            data_final = input("Digite a data final (dd/mm/aaaa): ")

        return {"data_inicial": data_inicial, "data_final": data_final}

    def mostra_animal(self, dados_animal):
        print("------------------------------------")
        print(f'NOME DO {dados_animal["especie"].upper()}: {dados_animal["nome"]}')
        print(f'RAÇA DO {dados_animal["especie"].upper()}: {dados_animal["raca"]}')
        print(
            f'NÚMERO DO CHIP DO {dados_animal["especie"].upper()}: {dados_animal["numero_chip"]}'
        )
        if "tamanho" in dados_animal:
            print(
                f'TAMANHO DO {dados_animal["especie"].upper()}: {dados_animal["tamanho"]}'
            )
        print(
            f'HISTÓRICO DE VACINAÇÃO DO {dados_animal["especie"].upper()}: {dados_animal["vacinacao"]}'
        )

    def mostra_adocao(self, dados_adocao):
        print("------------------------------------")
        print(f'ID DE ADOÇÃO: {dados_adocao["id_registro"]}')
        print(f'DATA DE ADOÇÃO: {dados_adocao["data_adocao"]}')
        print(
            f'STATUS DO TERMO DE RESPONSABILIDADE DE ADOÇÃO: {dados_adocao["termo_assinado"]}'
        )
        print(f'CPF DO ADOTANTE PARA ADOÇÃO: {dados_adocao["cpf_adotante"]}')
        print(f'NOME DO ADOTANTE: {dados_adocao["nome_adotante"]}')
        print(f'NÚMERO DO CHIP DO ANIMAL: {dados_adocao["numero_chip"]}')
        print(f'NOME DO ANIMAL: {dados_adocao["nome_animal"]}')

    def mostra_doacao(self, dados_doacao):
        print("------------------------------------")
        print(f'ID DE REGISTRO DE DOAÇÃO: {dados_doacao["id_registro"]}')
        print(f'CPF DO DOADOR: {dados_doacao["cpf_doador"]}')
        print(f'NOME DO DOADOR: {dados_doacao["nome_doador"]}')
        print(f'NÚMERO DO CHIP DO ANIMAL: {dados_doacao["numero_chip"]}')
        print(f'NOME DO ANIMAL: {dados_doacao["nome_animal"]}')
        print(f'DATA DE DOAÇÃO: {dados_doacao["data_doacao"]}')

    def mostra_mensagem(self, mensagem):
        print(mensagem)
