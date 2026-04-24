nota1 = float(input("Digite a sua primeira nota!\n"))
nota2 = float(input("Digite a sua segunda nota!\n"))

media = (nota1 + nota2) / 2

if media < 7:
    print("Reprovado!")
    print(media)
elif media == 10:
    print("Aprovado com Distinção!")
    print(media)
elif media >= 7:
    print("Aprovado!")
    print(media)
else:
    print("Digite um valor valido!")