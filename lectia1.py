# variabilele se creeaza automat
# (nu mai trebuie sa scriem "local numar")
numar = 10

# la python putem folosi ambele
# tipuri de ghilimele
# "mere" bun!
# 'mere' bun!
# "mere' rau!
print(numar,'mere')

# se pune \ ca sa nu ne strice textul
# bucati din cod
print('He\'s happy!')

# putem scrie chestii cu tastatura
# cu comanda input
age = input()


### IF/ELSE
if int(age) < 14:
    print('nu poti intra')
else:
    print('distractie placuta')


### BUCLE: while
### while verifica o conditie
###   true:  ruleaza codul
###   false: trece mai departe
numar = 5
while numar > 0:
    print('buna')
    numar = numar - 1

    
    
