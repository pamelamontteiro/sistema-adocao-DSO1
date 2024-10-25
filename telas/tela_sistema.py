class TelaSistema:
    def tela_opcoes(self):
        print("-------- SISTEMA ADOÇÃO DE ANIMAIS --------")
        print("Escolha sua opção")
        print("1 - Menu adotante")
        print("2 - Menu doadores")
        print("3 - Menu gato")
        print("4 - Menu de adoção")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def mostra_mensagem(self, mensagem):
        print(mensagem)
