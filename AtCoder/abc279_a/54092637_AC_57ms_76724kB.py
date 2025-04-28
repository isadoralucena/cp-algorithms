palavra = input()

cont = 0
for i in palavra:
    if i == "w":
        cont += 2
    else:
        cont += 1

print(cont)