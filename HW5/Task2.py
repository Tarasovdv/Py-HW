# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

import random
candy_table = int(2021)
max_value_step = int(28)


def check(took_candy, remains_candy):
    return True if took_candy.isdigit() == True and int(took_candy) <= max_value_step and int(took_candy) > 0 and int(took_candy) <= remains_candy else ""

def player_vs_player(a, max_value_step):
    print('Game: Player vs. Player')
    player_1 = input('Ваше имя игрок 1: ')
    player_2 = input('Ваше имя игрок 2: ')
    play_random = (random.randint(1, 2))
    if play_random == 1:
        first = player_1
        second = player_2
    elif play_random == 2:
        second = player_1
        first = player_2
    print(f'\nFirst player: {first} \n Second player: {second}\n')
    count = 1
    my_dict = {first: 0, second: 0}
    candy_table = a
    while candy_table > max_value_step:
        if not count % 2 == 0:
            took_candy = input(f'{first}, Enter count of candy: ')
            while not check(took_candy, candy_table) == True:
                took_candy = input(
                    "You entered wrong count of candy. Enter count of candy again: ")
            my_dict[first] += int(took_candy)

        else:
            took_candy = input(f'{second}, Enter count of candy: ')
            while not check(took_candy, candy_table) == True:
                took_candy = input(
                    "You entered wrong count of candy. Enter count of candy again: ")
            my_dict[second] += int(took_candy)
        count += 1
        candy_table = a - my_dict[first] - my_dict[second]
        print(f'\n{candy_table} конфет осталось на столе')
    win = first if not count % 2 == 0 else second
    print(
        f'On the table {candy_table} candy. Its mean player {win}: you WIN! Congratulations!')


def player_vs_bot(a, max_value_step):
    print('Game: Player vs. BOT')
    player_1 = (random.randint(1, 2))  # player number 2 - bot
    #player_2 = 2 if player_1 == 1 else 1
    move = "man" if player_1 == 1 else "bot"
    print(f'Lets start! First stars player number: {player_1}')
    my_dict = {1 : 0, 2 : 0}
    candy_table = a
    while candy_table > max_value_step:
        if move == "man":
            took_candy = input("Player! Enter count of candy: ")
            while not check(took_candy, candy_table) == True:
                took_candy = input(
                    "You entered wrong count of candy. Enter count of candy again: ")
            my_dict[1] += int(took_candy)
            move = "bot"
        else:
            bot_move = random.randint(0, 29)
            my_dict[2] += bot_move
            print(f'Bot enter: {bot_move}')
            move = "man"
        candy_table = a - my_dict[1] - my_dict[2]
        print(f'Now on the table candy: {candy_table}')
    win = "bot" if move == "bot" else "man"
    print(f'Now on the table {candy_table} candy. Its mean {win} WIN! Congratulations!')

def player_vs_bot_clever(a, max_value_step):
    print('Game: Player vs. BOT')
    player_1 = (random.randint(1, 2))  # player number 2 - bot
    #player_2 = 2 if player_1 == 1 else 1
    move = "man" if player_1 == 1 else "bot"
    print(f'Lets start! First stars player number: {player_1}')
    my_dict = {1 : 0, 2 : 0}
    candy_table = a
    while candy_table > max_value_step:
        if move == "man":
            took_candy = input("Player! Enter count of candy: ")
            while not check(took_candy, candy_table) == True:
                took_candy = input(
                    "You entered wrong count of candy. Enter count of candy again: ")
            my_dict[1] += int(took_candy)
            move = "bot"
        else:
            bot_move = candy_table % (max_value_step + 1) if not candy_table % (max_value_step + 1) == 0 else 1
            my_dict[2] += bot_move
            print(f'Bot enter: {bot_move}')
            move = "man"
        candy_table = a - my_dict[1] - my_dict[2]
        print(f'Now on the table candy: {candy_table}')
    win = "bot" if move == "bot" else "man"
    print(f'Now on the table {candy_table} candy. Its mean {win} WIN! Congratulations!')

# player_vs_player(candy_table, max_value_step)
# player_vs_bot(candy_table, max_value_step)
player_vs_bot_clever(candy_table, max_value_step)
