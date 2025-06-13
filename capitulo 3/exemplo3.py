def minutos_segundos(minuto):
    print(minuto * 60)

minutos_segundos(1)

# uma chamada de função recebe argumento
# uma função tem parâmentro
# escreve def para definir a função

# uma variável dentro de uma função é local. apenas a global funciona em qualquer parte do programa e a local não.

def somar (n1, n2):
    resultado = n1 + n2
    print(f"A soma entre {n1} e {n2} é igual a {resultado}")

somar(50, 10)