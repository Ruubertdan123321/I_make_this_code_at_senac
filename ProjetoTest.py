print("\n==========================================")
print("-        SEJA MUITO BEM-VINDO(A)         -")
print("==========================================\n")
print("Você está prestes a começar a sua aventura!\n")

jogador = input("Digite o nome do jogador!\n")
classe = ""
hp = 0
energia = 0
level = 1

print("\nQual classe você gostaria de escolher!\n"),
print(" 1-Guerreiro\n 2-Arqueiro\n 3-Mago\n"),

esco = input("Digite a sua classe!\n")

classe = esco

print("\n==========================================\n")

print(jogador," Embarca na sua primeira aventura, com apenas um objetivo!\n","\nResgatar um aldeão que foi sequestrado!\n")
if(classe == "Mago" or classe == "mago" or classe == "guerreiro" or classe == "Guerreiro" or classe == "arqueiro" or classe == "Arqueiro"):
    hp = 100
    energia = 100

    print("Seu status é: \nClasse: ",classe,"\nVida: ",hp,"\nEnergia: ",energia)

    print("\n==========================================\n")

    print("Você está explorando uma masmorra que acabou entrando por curiosidade e se depara com um esqueleto!\n", " O que você vai fazer em relação a tal situação!?\n","\n  1-Lutar\n","\nFugir!")
print("Encerrando o programa.")


