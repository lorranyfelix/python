def categorias_idade (idadeJogador):
    if (idadeJogador == 5 or idadeJogador <= 7):
        print(f"Você está na categoria Infantil A")

    elif (idadeJogador >= 8 or idadeJogador <= 10):
        print(f"Você está na categoria Infantil B")

    elif (idadeJogador >= 11 or idadeJogador <= 13):
        print(f"Você está na categoria Juvenil A")

    elif (idadeJogador >= 14 or idadeJogador <= 17):
        print(f"Você está na categoria Juvenil B")
    elif (idadeJogador >= 18):
        print(f"Você é Senior")

    else: print("Desculpa, você não pode participar do time :(")

def mostra_mensagem():
    print("Existe cinco categorias: ")
    print("Infantil A = 5 - 7 anos")
    print("Infantil B = 8 - 10 anos")
    print("Juvenil A = 11 - 13 anos")
    print("Juvenil B = 14 - 17 anos")
    print(input("Pressione ENTER para verificarmos sua classificação..."))

idadeJogador = int(input("Digite a sua idade: "))

mostra_mensagem()
categorias_idade (idadeJogador)