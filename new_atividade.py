a = 1
b = 2
c = a != 2 or b == 1
d = a != 1 or b == 1
e = not(a == 1)
f = a == 2 and b!= 1
print("a != 2 or b == 1 :",c)
print("a != 1 or b == 1 :",d)
print("not(a == 1) :",e)
print("a == 2 and b!= 1",f)


print("\n==================================================\n")

x = 10
y = 15
z = 25

print("O resultado vai ser: ",x == z - y and z != y - x or not y != z - x)