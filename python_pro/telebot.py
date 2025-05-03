import telebot
import random
import os

    # Инициализация бота с использованием его токена
bot = telebot.TeleBot("7671817824:AAHtxBdPDeYH0kXdTQxLBsdIwOaw9bhFJw7671817824")
memes = os.listdir("./image")
    # Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
    
    # Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
    

@bot.message_handler(commands=['mem', 'meme', 'memes'])
def mem(message):
    
    global memes
    r_mem = random.choice(memes)
    with open(f"./image/{r_mem}", "rb") as f:
        bot.send_photo(message.chat.id, f)
    memes.remove(r_mem)
    if memes == {}:
        memes = os.listdir("./image")








@bot.message_handler(commands=['calc'])
def calc(message):
    words = message.text.split()
    if len(words) > 2:
        if words[1] == "summa":
            number = int(words[2])
            summa = 0
            if number < 0:
                for i in range(0, number, - 1, -1):
                    summa += 1
            elif number > 0:
                for i in range(0, number, + 1, +1):
                    summa +=1
            else:
                summa = 0

            bot.reply_to(message, f'сумма всех чисел является {summa}!')
        else:
            if len(words) == 4:
                number1 = int(words[1])
                number2 = int(words[3])
                simbol = words[2]
                result = 0
                if simbol == "+":
                    result = number1 + number2
                elif simbol == "-":
                    result = number1 - number2
                elif simbol == "*":
                    result = number1 * number2
                elif simbol == "/":
                    if number2 != 0:
                        result = number1 / number2
                    else:
                        result = "nu-uh!"
                bot.reply_to(message, f'ресультат: {result}!')
    else:
        print("и что это за фигня?")          
                    





    # Запуск бота
bot.polling()