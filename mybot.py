from emoji import emojize
from glob import glob 
import logging
from random import randint, choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)


#PROXY = {'proxy_url':settings.PROXY_URL,
    #'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print("Вызван /Start")
    context.user_data['emoji']= get_smile(context.user_data)
    #print(1/0)
    #print(update)
    update.message.reply_text(f'Здравствуй, Пользователь {context.user_data["emoji"]}!')

def talk_to_me(update, context):
    context.user_data["emoji"] = get_smile(context.user_data)
    text =  update.message.text
    print(text)
    update.message.reply_text(f'{text} {context.user_data["emoji"]}')

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases = True)
    return user_data['emoji']

def guess_number(update, context):
    
    print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число!'
    else:
        message = 'Введите число'
    update.message.reply_text(message)

def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f'Ты загадал {user_number}, я загадал {bot_number}, ты выиграл!!!'
    elif user_number == bot_number:
        message = f'Ты загадал {user_number}, я загадал {bot_number}, ничья!!!'
    else:
        message = f'Ты загадал {user_number}, я загадал {bot_number}, Я выиграл!!!'
    return message

def send_cat_picture(update, context):
    cat_photos_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id = chat_id, photo = open(cat_pic_filename, 'rb'))

def main():
    mybot = Updater(settings.API_KEY, use_context=True)    #, request_kwargs=PROXY

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler('cat', send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()