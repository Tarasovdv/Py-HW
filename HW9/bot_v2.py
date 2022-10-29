from array import array
from email import message
import telebot
from telebot import types
bot = telebot.TeleBot('5780078252:AAHdccUtESvBwB0-q-n82zY2WfhZhsFckRU')
@bot.message_handler(content_types=['text'])


def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Welcome to my game!Player number one: choose a symbol X or 0: \n")
        bot.register_next_step_handler(message, help) #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, "Enter /start")


def help(message):
    global player_1
    global player_2
    global array
    global move
    global player_1_turn
    global player_2_turn
    array= ["_"]*9
    player_1=message.text
    if player_1=="X":
        player_2=0
        bot.send_message(message.from_user.id, f"Player number two: your symbol: {player_2} \nAre you ready?")
        
    else:
        player_2="X"
        bot.send_message(message.from_user.id, f"Player number two: your symbol: {player_2} \nAre you ready?")

    player_1_step(message)

def player_1_step(messege):
    bot.send_message(messege.from_user.id, "Player one: Enter number of positoin: ")
    player_1_turn=message.text
    # while not check2(arr,player_1_turn)==True:
        #         player_1_turn=int(input("\nPlayer number one, you entered wrong number: Enter number of positoin again: "))
    move=True
    append(message)

def append(message):
    if move==True:
        array[int(message.text)-1]=player_1_turn 
        player_2_step(message)
    

    else:
        array[int(message.text)-1]=player_2_turn
        player_1_step(message)
    bot.send_message(message.from_user.id, "Hello my dear ")

def player_2_step(messege):
    bot.send_message(messege.from_user.id, "Player two: Enter number of positoin: ")
    player_2_turn=message.text
    # while not check2(arr,player_1_turn)==True:
        #         player_1_turn=int(input("\nPlayer number one, you entered wrong number: Enter number of positoin again: "))
    move=False
    append(message)


        


bot.polling(none_stop=False, interval=0)