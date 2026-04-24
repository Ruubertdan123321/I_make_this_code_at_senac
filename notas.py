n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 6:
    print("\nAprovado\n")
    print("Sua media é :",media)
elif media < 6 and media >= 4:
    print("Você ficou de exame")
    print("Sua media é :",media)
else:
    print("\nReprovado\n")
    print("Sua media é :",media)