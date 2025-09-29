
# funcția este o instrucțiune formată
# dintr-un set de alte instrucțiuni

# !!! Funcția este un mod de a reutiliza cod


def in_to_cm(number):
    return 0.393701*number


lungime = 3 #in
latime = 4 #in

aria = in_to_cm(lungime) * in_to_cm(latime)


# exemplu: temperatura

# ca sa convertesti de la celsius la fahrenheit,
# inmultesti cu 1.8 si adaugi 32

def CtoF(celsius):
    """
    Converteste de la grade Celsius la grade Fahrenheit.
    """
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

def FtoC(fahrenheit):
    """
    Converteste de la grade Fahrenheit la grade Celsius.
    """
    celsius = (fahrenheit - 32) / 1.8
    return celsius


print(f"15 grade C sunt {CtoF(15)} grade F")
print(f"15 grade F sunt {FtoC(15)} grade C")



# convertor de lungimi

def convertor_lungime(nr, unit, target='m'):
    """
    converteste lungimi
    mm, cm, m, km
    """
    if unit == 'mm':
        metri = nr / 1000
    if unit == 'cm':
        metri = nr / 100
    if unit == 'm':
        metri = nr
    if unit == 'km':
        metri = nr * 1000

    if target == 'mm':
        return metri * 1000
    if target == 'cm':
        return metri * 100
    if target == 'm':
        return metri
    if target == 'km':
        return metri / 1000


cm = 120
m = convertor_lungime(120, 'cm')
print(f"5400 cm sunt {convertor_lungime(5400, 'cm', 'km')} km")
