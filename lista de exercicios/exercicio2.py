entrada = int(input("Digite um número com 5 digitos"))

digito1 = entrada // 10000
digito2 = (entrada % 10000) // 1000
digito3 = (entrada % 1000) // 100
digito4 = (entrada % 100) // 10
digito5 = entrada % 10

print(digito1)
print(digito2)
print(digito3)
print(digito4)
print(digito5)