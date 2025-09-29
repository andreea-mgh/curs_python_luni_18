# a = 1

# retine in variabila a (pe rand)
# numerele de la 0 la 9
for a in range(10):
    a += 1

    for b in range(10):
        b += 1
        print(f"{a} * {b} = {a*b}")
        # print(a,'*',b,'=',a*b)
    
    print()