#lista1 = [10,20,30,40,50,60,70]
#lista2 = ["Daniel","Miguel","Joao"]

#print("",lista1,"\n",lista2)
#Criando listas
#_____________________________________
#lista3 = ["Oi",2.0,5,[10,20]]

#print(lista3) #Caso use o Len vai contar todos os dentro da lista e inclusive a sub lista e ela vai ser considerada apenas 1 caractere print(len(lista3)
#_____________________________________
#numero = [17,123,87,34,66,8398,44]

#print(numero[2])
#print(numero[9-8])
#print(numero[-2])
#print(numero[-1])

#uma_lista = [3,67,"gato",[56,57,"cachorro"],[],3.14,False]
#print(uma_lista[2][0]) #[2] = vai pegar o "gato". [0] = vai pegar o (g).
#_____________________________________
#frutas = ["maca", "laranja","banana", "cereja"]

#print("maca" in frutas)
#print("pera" in frutas)
#Vai dizer se é True caso esteja na lista e False caso nao esteja

#print([1,2] + [3,4])
#print(frutas + [6,7,8,9])

#print(["test"] * 4)
#print([1,2,["olá","adeus"]]*2)
#______________________________________
#a = [1,2,3,4,5,6,7,8,9]

#print(a)
#print(max(a))
#print(min(a))
#print(sum(a))
#______________________________________
#uma_lista = ["a","b","c","d","e","f"]
#print(uma_lista[1:3])
#print(uma_lista[:4])
#print(uma_lista[3:])
#print(uma_lista[:])
#print(uma_lista[0:6])
#______________________________________
#frutas = ["banana","maca"]
#frutas[0] = "pera"
#frutas[-1] = "abacate"

#print(frutas)
#______________________________________
#uma_lista = ["a","b","c","d","e","f"]
#uma_lista[1:3] = ["x","y"]
#print(uma_lista)
#Vai trocar certos dados

#______________________________________
#uma_lista = ["a","d","f"]
#uma_lista[1:1] = ["b","c"]
#print(uma_lista)
#uma_lista[4:4] = ["e"]
#print(uma_lista)
#Vai espremer o conteudo da direita para a esquerda, acrescentando ele.
#______________________________________
#a = ["um","dois","tres"]
#del a [1] #Vai deletar apenas o "dois"
#print(a)

#lista = ["a","b","c","d","e","f"]
#del lista[1:5] # O ultimo ou seja 5 n vai contar vai parar no 4  entao vai ser impresso no console : a , f
#print(lista)
#______________________________________
#a = [81,82,83]
#a.append(5)
#print(a)
#Vai colocar ou seja acrescentar na lista
#______________________________________
#a = [88,81,82,83]
#b = ["Daniel","Santana","Ana"]
#b.sort()
#a.sort()
#print(a)
#print(b)
#Vai ordenar
#______________________________________
#a = [1,2,3,4,5,6,7,8,9]
#print(a.index(9)) # pode ser string tambem para ser encontrado exemplo : (a.index("Daniel"))
#Vai mostrar onde que se encontra a posicao declarada 
#______________________________________
#a = [88,81,82,83]
#a.insert(1,100) # O primeiro numero vai escolher em qual posicao vai colocar e o segundo é o valor que vai ser colocado poderia ser string tambem no segundo valor 
#print(a)
#Vai inserir dados na lista
#______________________________________
#a = [88,2121,312134,34,56,786,32,82,88,88,88,88]
#print(a)
#print(a.count(88)) # Vai mostrar quantas vezes repetiu o numero ou string declarada no caso do exemplo ai vai mostrar quantos 88 existe na lista
#Vai contar quantos dados repetidos existe
#______________________________________
#a = [88,81,82,83,88,85,88,86]
#a.pop()
#print(a)
#Ele vai excluir o ultimo elemento da lista caso vc n declare nada dentro dos parenteses
#a.pop(0)#selecionando posicao
#print(a)
#Nesse caso ele vai excluir a posicao selecionada e dessa forma ele vai ser usado igual o del
#______________________________________
#lista = [1,2,3]
#lista.extend([4,5])
#print(lista)
#Diferente do append o extend pode colocar uma lista de uma vez ou varias informações na lista existente
#______________________________________
#t = [[1,2], [3], [4,5,6]] # Lista com subs listas

#print(sum(t[0]+t[1]+t[2]))  # Soma todas as sub listas

#print(t[0][0]+t[0][1]) # Vai somar 1 + 2 da primeira sub lista

#Somando dentro da lista. SUM(Vai somar os dados)
#______________________________________
#y = [1,2,3]

#resultado={
#     sum(y[0:1]),
#     sum(y[0:2]),
#     sum(y[0:3])
#}

#print(resultado)
#Para fazer isso precisa criar uma variavel e dentro dela usar o sum para imprimir o resultado depois
#______________________________________
#lista = ["Alemanha","Itália","Japao"]

#lista.append("Brasil")
#print(lista)
#Para colocar algum item dentro da lista usa o append
#______________________________________
#lista = [0,1,2,3,4,5,6,7,8,9,10]
#print(lista[1:10]) #Intervalo de 1 a 9
#print(lista[8:]) #Intervalo de 8 a 1
#print(sum(lista[0:])) # SOMA DA LISTA
#print(lista[-1],lista[-2],lista[-3],lista[-4],lista[-5],lista[-6],lista[-7],lista[-8],lista[-9],lista[-10]) #Lista Reversa
#print(lista[0],lista[1],lista[3],lista[5],lista[7],lista[9],"Impars") #Impares
#print(lista[2],lista[4],lista[6],lista[8],lista[10], "Pares")  #Pares
#______________________________________
#lista = [0,1,43,4,54,845,3245,323,543,7564,213421,5646,6767,8787,234]
#lista.sort()
#print()
#print(lista)
