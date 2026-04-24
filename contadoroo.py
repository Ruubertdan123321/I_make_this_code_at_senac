cont = 0

while cont < 1000:
    print(cont)
    print("O número de Inimigos detectados são : ", cont)
    cont = cont + 1
print("\n========================================")
print("Droga! O Murilo é um deles...")
print("========================================")
if cont == 1000:
    print("\nMEU DEUSSSS O MUNDO ESTÁ INFESTADO DE INIMIGOS!!!\n")
    n1 = str(input("Deseja continuar pesquisando até achar o ALPHA DOS INIMIGOS ?\n"))
    print("========================================")
if n1 == "SIM":
    print("Você ACHOU O ALPHA DOS INIMIGOS!")
    print("========================================")

soma = 0
num = int(input("Digite um número: "))
while num != 0:
    soma += num
    num = int(input("Digite um número: "))
print("TOTAL : ",soma)

#print("Valor de cont após o while: ",cont)