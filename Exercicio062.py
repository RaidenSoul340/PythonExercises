print("#==Gerador de PA==#")
print("=--=" *8)
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10    
while mais != 0:  
    total = total + mais 
    while cont <=  total:
        print("{} ->".format(termo), end="")
        termo += razão
        cont += 1
    print("PAUSA")
    mais = int(input("Você deseja que mostremos mais quantos termos? "))
print("""Pregressão finalizada :D
O número total de pregressões feitas foram {}""".format(total))