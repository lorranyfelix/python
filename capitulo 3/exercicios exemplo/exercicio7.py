def do_twice_linha(f):
    f()
    f()
    f()

def do_twice_coluna(f):
    f()
    f()
    f()
    f()

def linha_junto():
    print(linha)
linha = "+ - - - - + - - - - +"

def coluna_junto():
    coluna = "|"

do_twice_linha(linha_junto)
do_twice_coluna (coluna_junto)

print(do_twice_linha, do_twice_coluna)