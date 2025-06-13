def calcula_media(notaHistoria, notaMatematica, notaBiologia, notaQuimica):
    return (notaHistoria + notaMatematica + notaBiologia + notaQuimica) / 4

# main
nome = input("Digite o seu nome: ")
notaHistoria = float(input("Digite sua nota em História: "))
notaMatematica = float(input("Digite sua nota em Matemática: "))
notaBiologia = float(input("Digite sua nota em Biologia: "))
notaQuimica = float(input("Digite sua nota em Química: "))

media = calcula_media(notaHistoria, notaMatematica, notaBiologia, notaQuimica)

print("A média do(a) aluno(a)",nome,"é",media)