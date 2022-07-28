'''
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) (доп) Подумайте как наделить бота ""интеллектом""
'''

import random


def Get_candies_taken(candies_taken):
    while True:

        if candies_taken < 28 and candies_taken > 0:
            return candies_taken
        else:
            print("take candies from 1 to 28")
            candies_taken = int(input())


def Bot_mode(amount_candies):
    who_first = random.randint(1, 3)
    if who_first == 1:
        player = 'First player'
    else:
        player = 'Computer'

    winner = ''
    while amount_candies > 0:
        print(player, "take candies from 1 to 28")

        if player == 'First player':
            candies_taken = Get_candies_taken(int(input()))
        if player == 'Computer':
            candies_taken = random.randint(1, 29)
            print('Candies taken:', candies_taken)

        amount_candies = amount_candies - candies_taken
        print('Candies remain:', amount_candies)

        if player == 'First player' and amount_candies <= 0:
            winner = 'First player'
        if player == 'Computer' and amount_candies <= 0:
            winner = 'Computer'

        if player == 'First player':
            player = 'Computer'
        elif player == 'Computer':
            player = 'First player'

    print('And a winner is:', winner)


def Two_players_mode(amount_candies):
    who_first = random.randint(1, 3)
    if who_first == 1:
        player = 'First player'
    else:
        player = 'Second player'

    winner = ''
    while amount_candies > 0:
        print(player, "take candies from 1 to 28")
        candies_taken = Get_candies_taken(int(input()))

        amount_candies = amount_candies - candies_taken
        print('Candies remain:', amount_candies)

        if player == 'First player' and amount_candies <= 0:
            winner = 'First player'
        if player == 'Second player' and amount_candies <= 0:
            winner = 'Second player'

        if player == 'First player':
            player = 'Second player'
        elif player == 'Second player':
            player = 'First player'

    print('And a winner is:', winner)


amount_candies = 2021
print("Please choose who to play with: 1. 2nd player   2. Computer")


def Get_game_mode(game_mode):
    while True:
        if int(game_mode) == 1 or int(game_mode) == 2:
            return game_mode
        else:
            print("Choose proper mode, try again: ")
            game_mode = int(input())


game_mode = Get_game_mode(int(input()))

if game_mode == 1:
    Two_players_mode(amount_candies)
if game_mode == 2:
    Bot_mode(amount_candies)
