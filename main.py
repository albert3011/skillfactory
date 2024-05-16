a = ['-' for i in range(0, 9)]
user_to_code = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


def print_game(game):
    print(f'   0 1 2\n'
          f'0  {game[0]} {game[1]} {game[2]}\n'
          f'1  {game[3]} {game[4]} {game[5]}\n'
          f'2  {game[6]} {game[7]} {game[8]}\n')
    print('-------------------------------')


def check_full_win():
    win = False
    full = all([x != '-' for x in a])
    if full:
        return 'Ничья. Игра завершена.'
    else:
        win_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for variant in win_combos:
            if a[variant[0]] == a[variant[1]] == a[variant[2]]:
                if a[variant[0]] == 'O':
                    win = "Победил игрок №2. Игра завершена."
                elif a[variant[0]] == 'X':
                    win = "Победил игрок №1. Игра завершена."
        return win


def new_step(symbol, number, a):
    nice_step = False
    print('Необходимо совершить ход в пустой ячейке.')
    while not nice_step:
        row = input(f'Игрок №{number}, выберите строку (0, 1 или 2):\n')
        column = input('Выберите столбец (0, 1 или 2):\n')
        if row in ['0', '1', '2'] and column in ['0', '1', '2']:
            our_cell = user_to_code[int(row)][int(column)]
            if a[our_cell] == '-':
                a[our_cell] = symbol
                nice_step = True
            else:
                print('В эту ячейку нельзя ходить, она не пустая')
        else:
            print('Необходимо ввести 0, 1 или 2')
    print('\n\n\n\n\n\n\n------------------------------')
    print_game(a)
    return a


print_game(a)
while not check_full_win():
    a = new_step('X', 1, a)
    if not check_full_win():
        a = new_step('O', 2, a)
print(check_full_win())
