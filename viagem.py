distancia = float(input("Digite a distancia!\n"))
consumo_do_carro = 0.0
juncao = 0.0
custo = 0.0
while(distancia != juncao):
    consumo_do_carro = float(input("Consumo do veiculo km/l\n"))
    juncao = juncao + consumo_do_carro
    preco_do_combustivel = float(input("Digite o preço do combustivel\n"))
    custo = custo + preco_do_combustivel
print("Litros necessario: %.2f"%juncao)
print("O custo total vai ser:R$%.2f"%custo)