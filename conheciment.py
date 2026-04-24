lista = [12,11,13,14,15,16,70,5,99]

print(lista) #### print na lista inteira
print("\n_________________________________________________")
lista.sort() #### ordenando a lista em ordem crescente
print(lista)
print("\n_________________________________________________")
lista.sort(reverse=True)  #### ordem decrescente
print(lista)
print("\n_________________________________________________")
print(lista)
lista.pop(-5)  # Excluir o ultimo elemento da lista, caso esteja vazio ()
print(lista)
print("\n_________________________________________________")
print(lista)
lista.insert(2,18) # Primeiro vem a posicao e depois o valor a ser inserido 
print(lista)

