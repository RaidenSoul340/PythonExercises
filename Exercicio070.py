total = totmil = menor = cont = 0
barato = ""
while True:
    produto = str(input("Digite o nome do produto: "))
    preço = float(input("Digite o preço: R$  "))
    cont += 1
    total += preço

    if preço > 1000:
        totmil +=1

    if cont == 1 or preço < menor:
        menor = preço
        barato = produto 
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Deseja continuar? [S/N]:  ")).strip().upper()[0]
    if resposta == "N":
        break 
print("FIM D0 PROGRAMA")
print(f"O total das compras foi R${total:.2f}")
print(f"Temos {totmil} produtos custando mais de R$1000,00")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")