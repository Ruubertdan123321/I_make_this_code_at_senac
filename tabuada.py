#num = int(input("Digite um numero"))
#list = [1,2,3,4,5,6,7,8,9,10]
#for i in list:
#    result = i*num  
#    print(num, "x", i," = ",result)



num1 = int(input("Digite um numero: "))
print("=========================================")
print("             TABUADA DO ",num1)
print("=========================================")
cont = 1

while cont <= 10:
    result = num1*cont
    print(num1,"x",cont," = ",result)
    cont = cont + 1
print("=========================================")