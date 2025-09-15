bani = 200

jucarii = ['teddy','masina', 'labubu', 'lego']
preturi = [10, 15, 180, 160]

rucsac = []

# bucla infinita
while True:
    print('Bani:',bani)
    print('Produse la magazin:')

    for j,p in zip(jucarii, preturi):
        # string-urile f'' inlocuiesc
        # acoladele cu variabilele din ele
        print(f'   {j}, {p} lei')


    optiune = input()

    # == : verifica daca e egal
    # =  : schimba valoarea la altceva
    if optiune == 'gata':
        print('am plecat de aici')
        print(rucsac)
        break
    # elif = else if (testeaza inca o conditie)
    elif optiune in jucarii:
        # index = pozitia unui element
        i = jucarii.index(optiune)
        if bani >= preturi[i]:
            rucsac.append(jucarii[i])
            bani = bani - preturi[i]
    else:
        print('nu inteleg ce zici')
        




        
        
