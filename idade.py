idade = int(input("Digite sua idade : "))
Liberado = ""

if idade >= 18:
    print("\nPode tirar a carteira de habilitação\n")
    Liberado = True
else:
    print("\nNão pode tirar a carteira de habilitação\n")
    Liberado = False

if Liberado == True:
    print("\n=========================")
    print("Prova para tirar CNH")
    print("=========================\n")
    nome = str(input("Digite o seu nome completo!\n"))
    prova = int(input("Digite sua nota :"))
    if prova >= 7 and idade >= 18:
        print("\nPassou na prova!")
    else:
        print("\nVocê reprovou!")