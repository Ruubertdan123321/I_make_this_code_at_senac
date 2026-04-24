salario_atual = (float(input("Digite seu Sálario atual!\n")))
if(salario_atual < 500 ):
    salario_atual = salario_atual / (15/100)
    print("O salario atual é : R$%.2f"%salario_atual)
elif(salario_atual <= 1000):
    salario_atual = salario_atual / (10/100)
    print("O salario atual é : R$%.2f"%salario_atual)
elif(salario_atual >= 1000):
    salario_atual = salario_atual / (5/100)
    print("O salario atual é : R$%.2f"%salario_atual)
    print(f"O salario atual é : R$ {salario_atual:.2f}")
else:
    print("erro!")