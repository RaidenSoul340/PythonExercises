print("=" * 30)
print("Bem-Vindo ao Banco.Net")
print("=" * 30)
valor = int(input("Digite a Valor que deseja sacar: R$ "))
total = valor 
céd = 100 
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f"O total foi de {totcéd} cedulas de R${céd}")
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd == 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 2
        elif céd == 2:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print("=" * 30)
print("Obrigado! Pela sua preferencia volte sempre!")
