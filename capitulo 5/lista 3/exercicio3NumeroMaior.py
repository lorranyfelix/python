def comparacao_numeros (num1, num2, num3):

    if (num1 > num2):
        if (num1 > num3):
            print(f"O {num1} é o maior número")
    elif (num2 > num3):
            print(f"O {num2} é o maior número")
    else:
        print(f"O {num3} é o maior número")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))

comparacao_numeros (num1, num2, num3)