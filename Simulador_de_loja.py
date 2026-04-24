cont = 0
valor = 0.0
while(cont < 5):
    produto = input("Escolha o seu produto!\n")
    valor = 15.00 + valor
    cont = cont + 1
print("Valor: R$%.2f"%valor)
print("\n============================\n")
print("A vista fica :  10% de desconto!")
print("No cartao fica : 5% de desconto!")
print("Parcelado fica : sem desconto!")