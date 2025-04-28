jogos = int(input())
string  = input()


cont_d = 0
cont_a = 0
for i in string:
    if i == "A":
        cont_a += 1
    else:
        cont_d += 1
if cont_d == cont_a:
    print("Friendship")
elif cont_d > cont_a:
    print("Danik")
else:
    print("Anton")