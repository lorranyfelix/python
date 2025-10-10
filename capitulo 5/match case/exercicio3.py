def mes_ano(diaUsuario, mesUsuario):
    match mesUsuario:
        case 10, 12:
            print(f"Hoje é feriado.")




def main():
    print("Digite o dia: ")
    print("Digite o mês: ")
    diaUsuario = int(input())
    mesUsuario = int(input())

    mes_ano(diaUsuario, mesUsuario)


if __name__ == "__main__":
    main()