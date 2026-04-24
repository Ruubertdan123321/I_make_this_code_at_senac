nome = input("Digite seu nome!\n")
idade = int(input("Digite a sua idade!\n"))
sexo = input("Qual seu sexo?\n")

nota1 = float(input("Digite a sua primeira nota!\n"))
nota2 = float(input("Digite a sua segunda nota!\n"))

resultado = (nota1 + nota2) / 2

print(" O aluno: ",nome,"\n idade: ",idade, "\n sexo: ",sexo,"\n Sua nota é : %.2f" %resultado)