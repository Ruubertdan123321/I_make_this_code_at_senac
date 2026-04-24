#TUDO SOBRE: LEN; CAPITALIZE;UPPER;LOWER;ISDIGIT;REPLACE;SPLIT;FIND;IN;COUNT;[]


#____________________________________
a = "Daniel"

print(len(a))
#Vai contar quantos caracteres tem, espaço tambem conta.
#____________________________________
b = "daniel"

print(b.capitalize())
#Vai deixar a primeira letra Maiuscula.
#____________________________________
c = "santana"

print(c.upper())
#Vai deixar tudo Maiusculo 
#____________________________________
d = "DANIEL"

print(d.lower()) # Pode usar tambem (casefold) para deixar tudo minusculo.
#Vai deixar tudo Minusculo
#____________________________________
e = "1234"

print(e.isdigit())
#Se tudo for numero vai ser verdadeiro agora caso tenha uma letra no meio vai ser falso.
#____________________________________
f = "Daniel Santana"

print(f.replace("Santana","San"))
#Vai trocar os dados de uma string.
#____________________________________
g = "Daniel-Andrade-Dos"

print(g.split("-"))
#Vai separar todos os ascentos e caso n coloque nada ele vai separar por espaço.
#____________________________________
h = "Daniel Andrade Dos Santos"

print(h.find("Andrade"))
#Vai começar contando do 0 até o dado que vai ser localizado da string, exemplo disso : Daniel Andrade (Localizar> Andrade) D=0,a=1,n=2,i=3,e=4,l=5," "=6,A = 7
#Andrade Foi encontrado no 7
#____________________________________
i = "Daniel Andrade Dos Santos"

print("Santos" in i)
#Vai localizar e caso encontre vai informar se é verdadeiro. E caso n encontre vai ser Falso.
#____________________________________
j = "Daniel Andrade"

print(j.count("a"))
#Vai contar quantas vezes o parametro esta la dentro. Exemplo: Daniel Andrade = 2 a minusculo caso o count("a")
#____________________________________
k = "Olá, mundo!"

print(k[0]) #-1
print(k[2]) #-2
print(k[6]) #-3
#Vai pegar o parametro milimetricamente calculado da esquerda para direita, agora se for negativo vai pegar da direita para a esquerda. Se quiser que pega inteiro a string coloca dois pontos :
#____________________________________
l = "Ola aaaaamundo!"

print(l[0:3])
#Vai pegar o caractere de acordo com o numero
#____________________________________