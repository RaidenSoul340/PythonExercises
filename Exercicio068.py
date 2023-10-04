from random import randint

print("=-"*12)
print("VAMOS JOGAR IMPAR OU PAR")
print("=-"*12)
v = 1
while True:
    jogador = int(input("Digite um Número: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Você deseja escolher Par ou Impar [P/I]: ")).strip().upper()[0]
        print(f"Você jogou {jogador} e o computador jogou {computador}. O total é {total} ", end="")
        print("Deu PAR" if total % 2 == 0 else "DEU IMPAR")
        if tipo == "P":
            if total % 2 == 0:
                print("Você Ganhou")
                v += 1
            else:
                print("Você Perdeu")
                break
        elif tipo == "I":
            if total % 2 == 1:
                print("Você Ganhou")
                v += 1
            else:
                print("Você Perdeu")
                break
        print("Vamos Jogar Novamente :D!")
print(f"GAMER OVER! Você venceu {v} vezes")


