time1 = input("nome do time 1:")
time2 = input("nome do time 2:")
print(f"o jogo é entre {time1} vs {time2}")
gols1 = int(input(f"quantos gols fez o {time1}?"))
gols2 = int(input(f"quantos gols fez o {time2}?"))
if gols1 == gols2:
    print("o jogo foi empate")
else:
    if gols1>gols2:
        print(f"vitoria do {time1}")
    else:
        print(f"vitoria do {time2}")





