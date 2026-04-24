
x = "nome"
y = "idade"
a = 1
b = 2
altura = 1.71111111111
va = "world"

nome = input("Digite o seu %s\n" %x)
idade = int(input("Digite a sua %s!\n" %y))


'''
USANDO O %
%s String
%d Inteiro
%b Boolean
%f Float

%.2f (Isso faz com que escolhe a quantidade de casas do lado da virgula)

USANDO O .2f
print(f"valor, {valor:.2f}")

'''

if(nome == "Daniel" and idade == 25 or nome == "daniel" and idade == 25):{
    print("Seja muito bem vindo ao jogo de escolhas,",nome),
    print("Sua altura é : %.2f" %(altura)),
    print("Você está numa sala de aula e seu professor pede uma atividade pra você!\n O que você escolhe :\n %d-Fazer a atividade.\n %d-Não fazer." %(a,b)),
    print(3*"Carregando...\n"),
    print("+" + 10 * "-" + "+"),
    print(("|"+""* 10+ "          |\n")* 5,end=""),
    print("+"+ 10*"-"+"+"),
    print("\n======================================\n"),
    print(f"Hello, {va}!")
}
else:{
    print("Você está reprovado!\n")
}