numar = 10

# CTRL C opreste program

# testeaza conditii (mai mic, mai mare, egal etc.)
if numar < 15:
    print('da')
else:
    print("nu")


# daca o chestie ruleaza instructiuni, insrtuctiunile
# trebuie marcate cu TAB (spatiu) inaintea liniei

lista_cool = ['hot wheels', 'papusa', 'labubu', 'catelus']

print('lista mea:', lista_cool)

# numaratoarea la calculatoare incepe de la 0!!
# lista_cool[0] e primul element din lista_cool
print('al doilea element din lista:', lista_cool[1])
# elementul -1 e ultimul element
# elementul -2 e penultimul
# etc
print('ultimul element din lista:', lista_cool[-1])

lista_cool.append('papusa barbie')
lista_cool.remove('labubu')

print('lista noua:',lista_cool)

# asa sortam o lista
lista_cool.sort()

# asa intoarcem o lista pe dos
lista_cool.reverse()

print(lista_cool)

print(lista_cool.index('papusa'))
if 'labubu' in lista_cool:
    print(lista_cool.index('labubu'))
