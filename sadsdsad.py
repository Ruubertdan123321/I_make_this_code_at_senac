# 3 iguais Equilatero
# 2 os tres lados diferentes Escaleno
# 1 Iso 2 iguais

lado1 = int(input("Digite o valor do primeiro lado!\n"))

lado2 = int(input("Digite o valor do primeiro lado!\n"))

lado3 = int(input("Digite o valor do primeiro lado!\n"))

if lado1 == lado2 == lado3:
    print("É um triangulo Equilatero!")
elif lado1 != lado2 and lado3:
    print("É Escaleno!")
elif lado1 == lado2 or lado2 == lado3 :
    print("É Isósceles!")