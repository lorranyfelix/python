def checa_numero(negativoPositivo):
    if (negativoPositivo == 0):
        print(f"Erro! O número é zero")
    elif (negativoPositivo > 0):
        print(f"O {negativoPositivo} é positivo")
    else: print(f"O {negativoPositivo} é negativo")

negativoPositivo = int(input("Digite um número qualquer: "))

checa_numero (negativoPositivo)