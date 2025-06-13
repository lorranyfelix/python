def calculaDiametro(raio):
    return 2 * raioCirculo

def calculaCircunferencia(raio, pi):
    return (2 * raioCirculo) * pi

def calculaAreaCircunferencia(pi, raio):
    return pi * (raioCirculo ** raioCirculo)

# main
raioCirculo = int(input("Digite o raio do círculo: "))
pi = 3.14159

diametro = calculaDiametro(raioCirculo)
circunferencia = calculaCircunferencia(raioCirculo, pi)
areaCircunferencia = calculaAreaCircunferencia(pi, raioCirculo)

print("O valor do diâmetro é: ", diametro)
print("O valor da circunferência é:", circunferencia)
print("O valor da área da circunferência é: ", areaCircunferencia)