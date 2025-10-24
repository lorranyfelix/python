maior = 0
menor = 0

for i in range(0, 4):
        numeroUsuario = int(input("Digite um número: "))

if(i == 0):
         maior = numeroUsuario

if (numeroUsuario > maior):
        maior = numeroUsuario

elif(numeroUsuario < menor):
        menor = numeroUsuario

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")

