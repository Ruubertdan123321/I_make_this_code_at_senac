nome = str(input("Digite o nome do cliente!\n"))
valor = 0.0
cont = 0
total = 0.0
media = 0.0
imposto = 0.12
desconto = 0.05
while(cont < 3):
    produto = float(input("Digite o valor do produto!\n"))
    cont = cont + 1   
    valor = valor + produto
    total = valor
media = total / 3
print("Total da compra R$%.2f"%total,"\nA media dos produtos vai ser R$%.2f"%media)
total = (total * imposto) - desconto
print("R$%.2f"%total)