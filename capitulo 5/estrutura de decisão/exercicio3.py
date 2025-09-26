
def comparacaoNumeros (numero1, numero2, numero3):
    if (numero1 > numero2):
        if (numero1 > numero3):
            print(f"O número {numero1} é o maior número")

    if (numero2 > numero1):
        if (numero2 > numero3):
            print("O", numero2, "é o maior numero")

    if (numero3 > numero1):
        if (numero3 > numero2):
            print("O", numero3, "é o maior numero")

numero1 = int(input("Digite um número"))
numero2 = int(input("Digite outro número"))
numero3 = int(input("Digite mais um número"))

comparacaoNumeros (numero1, numero2, numero3)