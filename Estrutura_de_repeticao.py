inicio = int(input("Digite o valor de inicio!"))
fim = int(input("Digite o valor final!"))

while inicio <= fim :
    print(inicio)
    inicio = inicio + 1
    if inicio == 1000:
        resposta = int(input("Digite 1 para continuar ou 0 para sair!"))
        if resposta == 1:
            continue
        if resposta == 0:
            print("Encerrando o programa!")
            break
    if inicio == 2000:
        resposta = int(input("Digite 1 para continuar ou 0 para sair!"))
        if resposta == 1:
            continue
        if resposta == 0:
            break
print("Fim algoritmo")

#==========================================================================#

print("escolha entre 1 ou 2")
esco = int(input("Qual a sua escolha ?"))
match esco:
    case 1:
        print("Você escolheu 1!")
    case 2:
        print("Você escolheu 2!")