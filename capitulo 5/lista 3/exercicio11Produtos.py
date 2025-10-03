def verifica_produto (codigoProduto):
    if (codigoProduto == 1):
        print(f"O {codigoProduto} é um alimento não-perecível")
    elif (codigoProduto <= 4):
        print(f"O {codigoProduto} é um alimento perecível")
    elif (codigoProduto == 5 or codigoProduto == 6):
        print(f"O {codigoProduto} é um vestuário")
    elif (codigoProduto == 7):
        print(f"O {codigoProduto} é de higiene pessoal")
    elif (codigoProduto >= 8 or codigoProduto <= 15):
        print(f"O {codigoProduto} é limpeza e utensílios domésticos")
    else: print("ERRO! Código inválido, não existe no sistema.")
codigoProduto = int(input("Digite o código do seu produto: "))

verifica_produto(codigoProduto)