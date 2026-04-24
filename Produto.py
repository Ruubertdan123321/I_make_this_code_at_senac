nome_do_produto = input("Digite o nome do produto!\n")
quantidade = int(input("Digite a quantidade que gostaria de levar!\n"))
preco_do_produto = 00.00
desconto = 20.50

if(nome_do_produto == ""):
    print("Digite um valor valido!") 
else:
    preco_do_produto = 15.00 * quantidade
    print("O valor total deu R$: ",preco_do_produto)