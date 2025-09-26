
def validaIdade(idade1, idade2, idade3, idade4, idade5, pontos):
    if (idade1 == 21):
        pontos + 1
        print("Uma pessoa tem 21 anos")

    if (idade2 == 21):
        pontos + 2
        print("Duas pessoa tem 21 anos")

    if (idade3 == 21):
        pontos + 3
        print("Três pessoa tem 21 anos")

    if (idade4 == 21):
        pontos + 4
        print("Quatro pessoa tem 21 anos")

    if (idade5 == 21):
        pontos + 5
        print("Cinco pessoa tem 21 anos")


idade1 = int(input("Digite a idade da primeira pessoa"))
idade2 = int(input("Digite a idade da segunda pessoa"))
idade3 = int(input("Digite a idade da terceira pessoa"))
idade4 = int(input("Digite a idade da quarta pessoa"))
idade5 = int(input("Digite a idade da quinta pessoa"))

pontos = 0

validaIdade (idade1, idade2, idade3, idade4, idade5, pontos)

