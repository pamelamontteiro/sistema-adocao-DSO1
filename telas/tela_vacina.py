class TelaVacina:
    def tela_opcoes(self):
        print("-------- LISTA DE VACINAS --------")
        print("1 - Raiva")
        print("2 - Leptospirose")
        print("3 - Hepatite Infecciosa")
        print("0 - Retornar")

        opcao = int(input("Selecione a vacina: "))
        return opcao

    def mostrar_mensagem(self, msg):
        print(msg)
