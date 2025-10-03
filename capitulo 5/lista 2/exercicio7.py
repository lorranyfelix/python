def calculo_combustivel (precoCombustivel, marcacaoDoKmInicio, marcacaoDoKmFinal, gastoCombustivel, valorPassageiros):
    mediaConsumo = (gastoCombustivel * (marcacaoDoKmFinal - marcacaoDoKmInicio)) / precoCombustivel
    print(f"A média do consumo de combustível foi: {mediaConsumo}")
    lucroDia = valorPassageiros - mediaConsumo
    print(f"O lucro no final do dia foi de: {lucroDia}")

precoCombustivel = float(input("Quanto custa o preço do combustível? "))
marcacaoDoKmInicio = int(input("Quantos quilometros no ínicio do dia? "))
marcacaoDoKmFinal = int(input("Quantos quilometros no final do dia? "))
gastoCombustivel = int(input("Quantos litros foram gastos? "))
valorPassageiros = int(input("Qual o valor final recebido dos passageiros? "))

calculo_combustivel (precoCombustivel, marcacaoDoKmInicio, marcacaoDoKmFinal, gastoCombustivel, valorPassageiros)
