
game_map = ['████████████████',
            '█    █$█  !  █ █',
            '██ $ █       ! █',
            '█$   ███  $  ███',
            '█    ! █     ! █',
            '█   ████     █ █',
            '█   █    m   █ █',
            '█   !        █$█',
            '████████████████', ]

game_map = [list(row) for row in game_map]

# putem sa cautam caracterul de la o pozitie
# cu game_map[linie][coloana]

def show_map():
    for linie in game_map:
        print(''.join(linie))

show_map()

player_y = 6
player_x = 9

while True:
    inst = input()
    
    if inst == 'up' and game_map[player_y-1][player_x] != '█':
        player_y = player_y - 1