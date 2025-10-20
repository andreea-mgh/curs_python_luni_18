import os
from random import randint as rand
from random import choice as choose

def clear():
    os.system('cls')

game_map = ['████████████████',
            '█    █$█  !  █ █',
            '██ $ █       ! █',
            '█$   ███  $  ███',
            '█    ! █     ! █',
            '█   ████   ███ █',
            '█   █    m   █ █',
            '█   !        █$█',
            '████████████████', ]

game_map = [list(row) for row in game_map]

# putem sa cautam caracterul de la o pozitie
# cu game_map[linie][coloana]

def show_map():
    for linie in game_map:
        print(''.join(linie))

HP = 10
GOLD = 0

player_y = 6
player_x = 9

def combat():
    global HP
    global GOLD
    enemy_health = 4
    print("Entering combat...")
    while enemy_health > 0:
        print(f"Enemy HP: {enemy_health}")
        print(f"Your HP:  {HP}")
        action = input()

        if action in ['attack','a']:
            enemy_health -= rand(1,2)

            if enemy_health <= 0:
                GOLD += rand(2,5)
                print("Enemy defeated!")
                return True
            else:
                HP -= 1
                print(f"You were attacked, HP {HP}")

                if HP <= 0:
                    print("you died :((")
                    return False



while True:
    show_map()
    inst = input()
    clear()

    old_x = player_x
    old_y = player_y

    if inst == 'up' and game_map[player_y-1][player_x] != '█':
        player_y = player_y - 1
    
    if inst == 'down' and game_map[player_y+1][player_x] != '█':
        player_y = player_y + 1
    
    if inst == 'left' and game_map[player_y][player_x-1] != '█':
        player_x = player_x - 1
    
    if inst == 'right' and game_map[player_y][player_x+1] != '█':
        player_x = player_x + 1
    
    if inst == 'stat':
        print(f"HP:   {HP}")
        print(f"GOLD: {GOLD}")
    
    if inst in ['quit','exit','q','x']:
        print("exiting game...")
        break

    if game_map[player_y][player_x] == '$':
        GOLD += 1

    if game_map[player_y][player_x] == '!':
        fight = combat()
        if fight:
            print(f"combat ended! HP: {HP}, GOLD: {GOLD}")
        else:
            break
    


    game_map[old_y][old_x] = ' '
    game_map[player_y][player_x] = 'm'