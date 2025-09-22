a = 26
b = 5

# a != b : a nu e egal b
# echivalent cu not a==b
if not a == b:
    print("diferite")

print(a+b)
print(a-b)
print(a*b)
print(a/b)  # 5.2 (impartirea cu virgula)
print(a//b) # 5 (catul impartirii cu rest)
print(a%b)  # 1 (restul impartirii cu rest)




a += 1    # a = a + 1
a -= 1    # a = a - 1
a *= 3 # ...

# plr.leaderstats.Score.Value += 1


# -----------------------
# | WHILE               |
# -----------------------

a = 25
b = 5

nr = 0
a2 = a
# a = b la puterea ceva
# cum aflu ceva

while a >= b:
    a = a // b
    nr+=1

# f"" -> ia valorile din acolada si le pune in text

if a == 1:
    print(f"{a2} = {b} ^ {nr}")
else:
    print(f"{a2} nu este putere a lui {b}")


# !!! bucla infinita se face cu while True

while True:
    print("scrie ceva")

    # input () -> programul asteapta sa scriem
    # ceva de la tastatura si salveaza acel ceva
    # intr-o variabila
    text = input()

    if text == "ceva":
        # break termina instant o bucla
        break

