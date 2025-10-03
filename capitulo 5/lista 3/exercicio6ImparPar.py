def verifica_numero (numeroUsuario):
    if (numeroUsuario % 2 !=0):
        print(f"O {numeroUsuario} é um número ímpar")
    else: print(f"O {numeroUsuario} é um número par")

numeroUsuario = int(input("Digite um número: "))

verifica_numero(numeroUsuario)