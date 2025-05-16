print("valor do primeiro: 8min e 15s")
minutoPrimeiroTrecho = 8 * 60
segundosPrimeiroTrecho = 15

print("Tempo do segundo trecho: 7min e 12s ")
minutoSegundoTrecho = (7 * 3) * 60
segundosSegundoTrecho = 12 * 3

print("valor do terceiro: 8min e 15s")
minutoTerceiroTrecho = 8 * 60
segundosTerceiroTrecho = 15

# Soma o total de minutos e converte todos os segundos em minutos

totalTempoTodosTrechosMinutos = (minutoPrimeiroTrecho + minutoSegundoTrecho + minutoTerceiroTrecho) / 60

# Soma valor total dos segundos
totalTempoTodosTrechosSegundos = (segundosSegundoTrecho + segundosTerceiroTrecho + segundosPrimeiroTrecho)

restanteMinutos = int(totalTempoTodosTrechosSegundos / 60)
restanteSegundos = totalTempoTodosTrechosSegundos % 60

totalMinutos = totalTempoTodosTrechosMinutos + restanteMinutos
totalSegundos = restanteSegundos

print("Soma de tempo de todos os trechos em minutos: ", totalMinutos, "minutos")
print("Soma de tempo de todos os trechos em minutos foi: ", totalSegundos, "segundos")

horaInicialSegundos = (6 * 60) * 60
minutoInicialSegundos = 52 * 60
horaraioInicialSegundos = horaInicialSegundos + minutoInicialSegundos

tempoTrechoMinutosSegundos = totalMinutos * 60

horaChegada = int(((horaraioInicialSegundos + tempoTrechoMinutosSegundos) / 60) / 60)
minutoChegada = int(((minutoInicialSegundos + tempoTrechoMinutosSegundos) / 60) % 60)
print("O horário de chegada foi",horaChegada,":",minutoChegada,".",restanteSegundos)
