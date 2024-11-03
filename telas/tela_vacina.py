class TelaVacina:
    def pega_nome_vacina(self):
        print("-------- SELEÇÃO DE VACINA --------")
        print("1 - Raiva")
        print("2 - Leptospirose")
        print("3 - Hepatite Infecciosa")
        nome_vacina = int(input("Selecione a vacina: "))
        return nome_vacina

    def mostrar_mensagem(self, msg):
        print(msg)
