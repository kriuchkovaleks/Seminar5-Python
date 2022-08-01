'''
Создайте программу для игры в ""Крестики-нолики"".
'''

from random import randint

arr_play = [['*', '*', '*'],
            ['*', '*', '*'],
            ['*', '*', '*']]


print(arr_play[1][0])


who_first = randint(1, 3)
if who_first == 1:
    player = 'First player'
else:
    player = 'Second player'

winner = ''
steps_amount = 9

while steps_amount != 0:

    print(player, " make your choise, input cell coordinates")

    if player == 'First player':
        print('Input X')
    if player == 'Second player':
        print('Input O')

    row = int(input('Input row:'))
    column = int(input('Input column:'))

    if player == 'First player':
        arr_play[row - 1][column - 1] = 'X'
    if player == 'Second player':
        arr_play[row - 1][column - 1] = 'O'

    steps_amount = steps_amount - 1
    print(arr_play)

    if player == 'First player':
        player = 'Second player'
    elif player == 'Second player':
        player = 'First player'

    if arr_play[0][0] == arr_play[0][1] == arr_play[0][2] == 'X':
        winner = 'First player'
        break
    if arr_play[0][0] == arr_play[0][1] == arr_play[0][2] == 'O':
        winner = 'Second player'
        break

    if arr_play[1][0] == arr_play[1][1] == arr_play[1][2] == 'X':
        winner = 'First player'
        break
    if arr_play[1][0] == arr_play[1][1] == arr_play[1][2] == 'X':
        winner = 'Second player'
        break

    if arr_play[2][0] == arr_play[2][1] == arr_play[2][2] == 'X':
        winner = 'First player'
        break
    if arr_play[2][0] == arr_play[2][1] == arr_play[2][2] == 'X':
        winner = 'Second player'
        break

    if arr_play[0][0] == arr_play[1][0] == arr_play[2][0] == 'X':
        winner = 'First player'
        break
    if arr_play[0][0] == arr_play[1][0] == arr_play[2][0] == 'O':
        winner = 'Second player'
        break

    if arr_play[0][0] == arr_play[1][1] == arr_play[2][1] == 'X':
        winner = 'First player'
        break
    if arr_play[0][0] == arr_play[1][1] == arr_play[2][1] == 'X':
        winner = 'Second player'
        break

    if arr_play[0][2] == arr_play[1][2] == arr_play[2][2] == 'X':
        winner = 'First player'
        break
    if arr_play[0][2] == arr_play[1][2] == arr_play[2][2] == 'X':
        winner = 'Second player'
        break

    if arr_play[0][0] == arr_play[1][1] == arr_play[2][2] == 'X':
        winner = 'First player'
        break
    if arr_play[0][0] == arr_play[1][1] == arr_play[2][2] == 'O':
        winner = 'Second player'
        break

    if arr_play[2][0] == arr_play[1][1] == arr_play[0][2] == 'X':
        winner = 'First player'
        break
    if arr_play[2][0] == arr_play[1][1] == arr_play[0][2] == 'O':
        winner = 'Second player'
        break


print('And a winner is:', winner)
