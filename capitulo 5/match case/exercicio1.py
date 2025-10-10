def apresenta_jogador(opcao):
    match opcao:
        case 1:
            print(f"Jogador 1 é o Hugo Souza")
        case 2:
            print(f"Jogador 2 é o Vitinho")
        case 3:
            print(f"Jogador 3 é o Gabriel")
        case 4:
            print(f"Jogador 4 é o Éder Militão")
        case 5:
            print(f"Jogador 5 é o Casimiro")
        case 6:
            print(f"Jogador 6 é o Douglas Santos")
        case 7:
            print(f"Jogador 7 é o Vinícius Junior")
        case 8:
            print(f"Jogador 8 é o Bruno Guimarães")
        case 9:
            print(f"Jogador 9 é o Richarlisson")
        case 10:
            print(f"Jogador 10 é o Rodrygo")
        case 11:
            print(f"Jogador 11 é o Lucas Paquetá")
        case _:
            print(f"Jogador {opcao} não encontrado.")

def main():
    print("Digite um número de camisa de 1 até 11: ")
    opcao = int(input())

    apresenta_jogador(opcao)

if __name__ == "__main__":
    main()