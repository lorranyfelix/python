
def comparacaoNumeros (numero1, numero2, numero3):

    if (numero1 > numero2):
        if (numero1 > numero3):
            print(f"O primeiro número é o maior número")
    elif (numero2 > numero3):
            print(f"O segundo número é o maior número")
    else:
        print("O terceiro número é o maior número")



numero1 = int(input("Digite um número"))
numero2 = int(input("Digite outro número"))
numero3 = int(input("Digite mais um número"))

comparacaoNumeros (numero1, numero2, numero3)