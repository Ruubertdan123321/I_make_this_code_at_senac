a = int(input("DIgite o valor da variavel A\n"))
b = int(input("DIgite o valor da variavel B\n"))
c = int(input("DIgite o valor da variavel C\n"))

total = (a**2) + b + c

if a == 0:
    print("Encerrando o programa!\n")
elif total < 0:
    print("Não possui raizes reais!\n")
elif total == 0:
    print("Possui apenas uma Raiz Real")
    print(total)
elif total > 0:
    print("A equação possui duas raiz reais!\n")
    print(total)