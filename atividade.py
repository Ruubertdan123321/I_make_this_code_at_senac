x = True
y = False
z = True
t = False

res = x and y
res2 = x and z
res3 = y and t

print("Var x: ",x)
print("Var y:",y)
print("Var z:",z)
print("Var t:",t)

print("Resultado de X e Y:",res)
print("Resultado de X e Z:",res2)
print("Resultado de Y e T:",not(res3))