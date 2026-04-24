#i = 50
#while i >= 0:
#    print(i)
#    i = i - 1
#print("Fim")

#x = 10
#================================================
#x = 10
#while not (x == 0):
#    x = x-1
#    if x % 2 != 0:
#        print(x)

terminou = False
p = i = 0
while (not terminou): # Enquanto não terminou ou seja vai rodar até que seja ao contrario 
    n = int(input("Digite um número, ou zero para terminar: "))
    if n == 0:
        terminou = True # Encerra o programa porque terminou vira True
    else:
        if n % 2 == 0: # Se numero terminar em zero isso significa que o numero é par
            p = p + 1  # Vai aumentar a quantidade no valor P para cada numero par que for colocado no N 
        else:
            i = i + 1  # Caso seja um numero IMPAR vai aumentar a variavel I 
print("P = ", p)
print("I = ", i)