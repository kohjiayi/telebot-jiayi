import telebot
import re
from telebot import types
import random

# Token Num: xxxxx
# https://github.com/eternnoir/pyTelegramBotAPI#message-handlers

bot = telebot.TeleBot("xxxxx", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
win = 0
lose = 0

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hello")

# /help command
@bot.message_handler(commands=['help'])
def handle_start_help(message):
	bot.send_message(message.chat.id, "Type '/' to see what I can do! If you are bored, tell me if you are bored and if you want to talk to nom, you can also call her in chat!")

# removes rps scores
@bot.message_handler(commands=['resetrps'])
def handle_reset(message):
    bot.send_message(message.chat.id, "AW Sorry you lost. Nvm try again")
    global win
    global lose
    win = 0
    lose = 0

#@bot.message_handler(commands=['removekeyboard'])
#def handle_keyboard(message):
    #bot.send_message(message.chat.id, "Done!", reply_markup = ReplyKeyboardRemove())

# echoes all incoming text messages back to the sender
#@bot.message_handler(func=lambda m: True)
#def echo_all(message):
	#bot.reply_to(message, message.text)

# replies to 'bored'
@bot.message_handler(regexp=".*[Bb]ored.*")
def handle_bored(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('Compliment me')
    itembtn2 = types.KeyboardButton('Play Scissors Paper Stone')
    itembtn3 = types.KeyboardButton('Beat me')
    markup.add(itembtn1, itembtn2, itembtn3)

#responses to 'bored'
@bot.message_handler(regexp="Compliment me")
def handle_compliment(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    list=['Wow u look great today :)', 'You look amazing!' ,'You look GREAT today :>','Wow you dress great today :)']
    msg = random.choice(list)
    bot.send_message(message.chat.id, msg)

@bot.message_handler(regexp="Play Scissors Paper Stone")
def handle_rpsqn(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtnrock = types.KeyboardButton('rock')
    itembtnpaper = types.KeyboardButton('paper')
    itembtnscissors = types.KeyboardButton('scissors')
    markup.add(itembtnrock, itembtnpaper, itembtnscissors)
    cid = message.chat.id
    x = bot.send_message(cid, "Choose!!!", reply_markup=markup)
    bot.register_next_step_handler(x , step_Set_Choice)

def step_Set_Choice(message):
    cid = message.chat.id
    user_action = message.text
    print(user_action)

    actions = ['rock', 'paper','scissors']
    computer_action = random.choice(actions)

    global win
    global lose

    bot.send_message(message.chat.id, "You chose " + user_action + ", I chose " + computer_action)
    if user_action == computer_action:
        bot.send_message(message.chat.id, "It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            bot.send_message(message.chat.id, "Rock smashes scissors!")
            win = win + 1
        else:
            bot.send_message(message.chat.id, "Paper covers rock!")
            lose = lose + 1
    elif user_action == "paper":
        if computer_action == "rock":
            bot.send_message(message.chat.id, "Paper covers rock!")
            win = win + 1
        else:
            bot.send_message(message.chat.id, "Scissors cuts paper!")
            lose = lose + 1
    elif user_action == "scissors":
        if computer_action == "paper":
            bot.send_message(message.chat.id, "Scissors cuts paper!")
            win = win + 1
        else:
            bot.send_message(message.chat.id, "Rock smashes scissors!")
            lose = lose + 1

    bot.send_message(message.chat.id, "Current Score: Me " + str(lose) + ", You " + str(win))

@bot.message_handler(regexp="scissors")
@bot.message_handler(regexp="rock")
@bot.message_handler(regexp="paper")
def handle_rpscontinue(message):
    user_action = message.text
    print(user_action)

    actions = ['rock', 'paper','scissors']
    computer_action = random.choice(actions)

    global win
    global lose

    if user_action == computer_action:
        bot.send_message(message.chat.id, "It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            bot.send_message(message.chat.id, "Rock smashes scissors!")
            win = win + 1
        else:
            bot.send_message(message.chat.id, "Paper covers rock!")
            lose = lose + 1
    elif user_action == "paper":
        if computer_action == "rock":
            bot.send_message(message.chat.id, "Paper covers rock!")
            win = win + 1
        else:
            bot.send_message(message.chat.id, "Scissors cuts paper!")
            lose = lose + 1
    elif user_action == "scissors":
        if computer_action == "paper":
            bot.send_message(message.chat.id, "Scissors cuts paper!")
            win = win + 1
        else:
            bot.send_message(message.chat.id, "Rock smashes scissors!")
            lose = lose + 1

    bot.send_message(message.chat.id, "Current Score: Me " + str(lose) + ", You " + str(win))

@bot.message_handler(regexp="Beat me")
def handle_kiss(message):
    bot.send_message(message.chat.id, "BONK")

#replies to 'nomz' or 'bun'
@bot.message_handler(regexp=".*[Nn]omz.*")
@bot.message_handler(regexp=".*[Bb]un.*")
def handle_bored(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtna = types.KeyboardButton('What you doing now?')
    itembtnb = types.KeyboardButton('Tell me a joke')
    markup.add(itembtna, itembtnb, itembtnc, itembtnd, itembtne)
    bot.send_message(message.chat.id, "HELLO", reply_markup=markup)

@bot.message_handler(regexp="What you doing now\?")
def handle_wyd(message):
    bot.send_message(message.chat.id, "EATING!!!")

@bot.message_handler(regexp="Tell me a joke")
def handle_jokenomz(message):
    bot.send_message(message.chat.id, "How do rabbits travel? By hareplane!")

bot.polling()
