
def  classifica_aparelho(letra):
    match letra:
        case "A":
            print(f"A geladeira é muito eficiente")
        case "B":
            print(f"A geladeira é eficiente")
        case "C":
            print(f"A geladeira é pouco eficiente")
        case "D":
            print(f"A geladeira é ineficiente")
        case _:
            print(f"A {letra} não existe na classificação")

def main():
    print("Digite a letra do consumo/eficiência de energia da geladeira: ")
    letra = str(input())


    classifica_aparelho(letra)

if __name__ == "__main__":
    main()