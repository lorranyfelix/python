def calcula_media(formativa1, formativa2, provaBimestra):
    mediaFormativas = (formativa1 + formativa2) / 2
    mediaBimestral = ((mediaFormativas) * 0.3) + ((provaBimestra) * 0.7)
    print("A média das notas formativas é: ", mediaFormativas)
    print("A média do bimestre é: ", mediaBimestral)

formativa1 = int(input("Escreva sua nota da primeira formativa: "))
formativa2 = int(input("Escreva sua nota da segunda formativa: "))
provaBimestral = int(input("Escreva sua nota da prova bimestral: "))

calcula_media(formativa1, formativa2, provaBimestral)