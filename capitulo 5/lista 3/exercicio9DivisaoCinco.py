def divisao_numero(numero):
    if (numero % 5 == 0):
        divisaoPorDois = numero / 5
        print(f"O {numero} é divisível por dois. A divisão é igual a {divisaoPorDois}")
    elif (numero % 2 == 0):
        divisaoPorTres = numero / 2
        print(f"O {numero} é divisível por três. A divisão é igual a {divisaoPorTres}")
    else: print(f"ERRO! O {numero} não é divisível por nenhum dos dois. Tente novamente.")

def mostra_mensagem():
        print(input("Pressione qualquer tecla para continuar..."))

numero = int(input("Digite um número: "))
print("Vou verificar se é divisivel por 2 ou 3")

mostra_mensagem()
divisao_numero (numero)
