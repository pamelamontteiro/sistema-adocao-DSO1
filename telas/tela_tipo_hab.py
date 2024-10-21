class TelaTipoHabitacao():
    def pega_tipo_habitacao(self):
        print("-------- TIPO DE HABITACAO DO ADOTANTE --------")
        print("1 - Casa pequena")
        print("2 - Casa média")
        print("3 - Casa grande")
        print("4 - Apartamento pequeno")
        print("5 - Apartamento médio")
        print("6 - Apartamento grande")
        tipo_hab = int(input("Selecione o tipo de habitacao: "))
        return tipo_hab

    def mostrar_mensagem(self, msg):
        print(msg)