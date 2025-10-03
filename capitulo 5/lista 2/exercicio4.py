def realiza_operacoes(recebaValor1, recebaValor2):
    soma = recebaValor1 + recebaValor2
    print("A soma dos números é: ", soma)
    subtracao = recebaValor1 - recebaValor2
    print("A subtração dos números é: ", subtracao)
    multiplicacao = recebaValor1 * recebaValor2
    print("A multiplicação dos números é: ", multiplicacao)
    divisao = recebaValor1 / recebaValor2
    print("A divisão dos números é:", divisao)

recebaValor1 = int(input("Escreva o primeiro número: "))
recebaValor2 = int(input("Escreva o segundo número: "))

realiza_operacoes (recebaValor1, recebaValor2)