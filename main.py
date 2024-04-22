# import telebot
# from bot import *
# from time import sleep
#
# bot = telebot.TeleBot(TOKEN)
#
#
# @bot.message_handler(content_types=['text'])
# def text(message):
#     if message.text == "Привет":
#         bot.send_message(message.from_user.id, 'Привет')
#     elif message.text == "Как дела":
#         sleep(5)
#         bot.send_message(message.from_user.id, 'Нормально.')
#
#     elif message.text == "Что делаешь?":
#         sleep(2)
#         bot.send_message(message.from_user.id, 'Данный момент обшаюсь с тобой .')
#
#     elif message.text == "А как тебя зовут":
#         sleep(3)
#         bot.send_message(message.from_user.id, 'Меня зовут Марат')
#
#     else:
#         bot.send_message(message.from_user.id, 'Я тебя не понял.')
#
# bot.infinity_polling()


# import telebot
# from bot import *
# from time import sleep
#
# bot = telebot.TeleBot(TOKEN)
#
#
#
#
#
#
# @bot.message_handler(content_types=['text'])
# def text(message):
#     if message.text == " Привет, как дела?":
#         bot.send_message(message.from_user.id, 'Привет! Да, все отлично, спасибо. А у тебя?')
#     elif message.text == "Тоже неплохо, спасибо за спрос. Что нового?":
#         sleep(5)
#         bot.send_message(message.from_user.id, 'Ничего особенного, работа, учеба... Но в выходные планирую с друзьями на природу,  А у тебя есть какие-то планы?')
#
#     elif message.text == "! А я, наверное, просто проведу время дома, почитаю книгу или посмотрю что-нибудь интересное.":
#         sleep(2)
#         bot.send_message(message.from_user.id, ' Звучит отлично. Время для себя всегда важно. Кстати, ты недавно что-нибудь интересное читала?')
#
#     elif message.text == " Да, я недавно закончила книгу про манаса. Очень увлекательно было! А ты читаешь что-то сейчас?":
#         sleep(3)
#         bot.send_message(message.from_user.id, 'Нет, пока ничего конкретного. Может быть, пора выбираться в книжный магазин и что-то новенькое купить.')
#
#
#     elif message.text == " Да, я недавно закончила книгу про Манаса. Очень увлекательно было! А ты читаешь что-то сейчас?":
#         sleep(3)
#         bot.send_message(message.from_user.id, ' Звучит как отличный план! Думаю, я тоже присоединюсь к тебе в это выходные.')
#
#     elif message.text == "Прекрасно! Тогда давай так и сделаем. А сейчас мне пора идти, у меня еще пара дел. Поговорим еще?":
#         sleep(3)
#         bot.send_message(message.from_user.id, ' Удачи с делами, до встречи!')
#     else:
#         bot.send_message(message.from_user.id, 'Я тебя не понял.')
#
#
# bot.infinity_polling()
#


# import cv2
# from telegram.ext import Updater, MessageHandler, Filters
#
# # Функция для обработки изображений
# def handle_image(update, context):
#     file_id = update.message.photo[-1].file_id
#     context.bot.get_file(file_id).download('image.jpg')
#     # Обработка изображения (например, просто отправим его обратно)
#     context.bot.send_photo(update.message.chat_id, open('image.jpg', 'rb'))
#
# # Функция для обработки видео
# def handle_video(update, context):
#     file_id = update.message.video.file_id
#     context.bot.get_file(file_id).download('video.mp4')
#     # Обработка видео (например, просто отправим его обратно)
#     context.bot.send_video(update.message.chat_id, open('video.mp4', 'rb'))
#
# def main():
#     updater = Updater("YOUR_BOT_TOKEN", use_context=True)
#     dp = updater.dispatcher
#
#     # Обработка изображений и видео
#     dp.add_handler(MessageHandler(Filters.photo, handle_image))
#     dp.add_handler(MessageHandler(Filters.video, handle_video))
#
#     updater.start_polling()
#     updater.idle()
#
# if name == 'main':
#     main()


# from telegram.ext import (Updater, CommandHandler, MessageHandler,Filters)
# from telegram.ext import (Updater, CommandHandler, MessageHandler, filters)
# import openai
#
#
# # Установите ваш API ключ от OpenAI
# openai.api_key = 'YOUR_BOT_TOKEN'
#
# # Callback функция для обработки сообщений пользователя и генерации ответа через GPT-3 модель
# def chat_gpt(update, context):
#     user_input = update.message.text
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=user_input,
#         max_tokens=100
#     )
#     bot_response = response.choices[0].text.strip()
#     update.message.reply_text(bot_response)
#
# # Функция для старта бота
# def start(update, context):
#     update.message.reply_text('Привет! Я бот, который готов чатиться с тобой.')
#
# def main():
#     # Создание экземпляра Updater и передача токена бота
#     updater = Updater('YOUR_BOT_TOKEN', use_context=True)
#
#     # Получаем диспетчер для регистрации обработчиков
#     dp = updater.dispatcher
#
#     # Регистрация обработчиков команд
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat_gpt))
#
#     # Запуск бота
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == '__main__':
#     main()


from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'


def chat_gpt(update, context):
    user_input = update.message.text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=user_input,
        max_tokens=100
    )
    bot_response = response.choices[0].text.strip()
    update.message.reply_text(bot_response)


def start(update, context):
    update.message.reply_text('Привет! Я бот, который готов чатиться с тобой.')


def main():
    updater = Updater('YOUR_BOT_TOKEN')

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.Text & ~filters.Command, chat_gpt))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
