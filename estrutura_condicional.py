#01 - Ler 2 numeros int e 1 real. Calcular e mostrar O produto do primeiro com a metade do segundo, a soma do triplo do primeiro com o terceiro. O terceiro numero digitado ao cubo.

num1 = int(input("Digite o primeiro numero!\n"))
num2 = int(input("Digite o segundo numero!\n"))
num3 = float(input("Digite o terceiro numero!\n"))

result = num1 * (num2/2)
result2 = (num1*3) * num3
result3 = num3**3

print("num1 * (num2/2) : ",result)
print("(num1*3) * num3",result2)
print("num3**3",result3)

#02 - Criar se é maior ou menor que 10 

x = int(input("Digite um numero!\n"))

if x > 10:
    print("O numero é maior que 10!")
else:
    print("O numero é menor que 10!")

#03 - Programa que mostra qual valor é maior

x = 5
y = 10

if x > y:
    print("X é Maior",x)
else:
    print("Y é Menor")

#04 - Ordem crescente de numeros

