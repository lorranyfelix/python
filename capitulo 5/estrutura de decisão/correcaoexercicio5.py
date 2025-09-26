def soma(numero1, numero2, numero3, numero4):
    total = 0

    if (numero1 % 2 == 0):
        total += numero1
    if (numero2 % 2 == 0):
        total += numero2
    if (numero3 % 2 == 0):
        total += numero3
    if (numero4 & 2 == 0):
        total += numero4

    return total


def contaPares(numero1, numero2, numero3, numero4):
    pares = 0

    if (numero1 % 2 == 0):
        pares += 1
    if (numero2 % 2 == 0):
        pares += 1
    if (numero3 % 2 == 0):
        pares += 1
    if (numero4 & 2 == 0):
        pares += 1

    return pares


def main():
    numero1 = int(input("Digite o primeiro número:"))
    numero2 = int(input("Digite o primeiro número:"))
    numero3 = int(input("Digite o primeiro número:"))
    numero4 = int(input("Digite o primeiro número:"))

    totalSoma = soma(numero1, numero2, numero3, numero4)
    totalPares = contaPares(numero1, numero2, numero3, numero4)
    media = totalSoma / totalPares

    print(f"A soma dos pares é: {totalSoma}")
    print(f"A média dos pares é: {media}")

if __name__ == "__main__":
    main ()