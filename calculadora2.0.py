print("================================================")
print("                  CALCULADORA                   ")
print("================================================\n")
x = 1

while x != 0:
    x = int(input("Digite 1 para continuar ou 0 para sair!\n"))
    if x == 0:
        break
    print("================================================\n")
    print("                  ESCOLHA:                        ")
    print("1:Multiplicação; 2:Divisão; 3:Adição; 4:Subtração\n")
    esco = int(input("Digite sua escolha: "))
    print("================================================\n")

    if esco == 1:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        total = n1 * n2
        print(total)
    if esco == 2:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        total = (n1 / n2)
        print(total)
    if esco == 3:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        total = n1 + n2
        print(total)
    if esco == 4:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        total = n1 - n2
        print(total)
