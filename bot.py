"""
@file bot.py
@author Jose
@brief cuerpo del bot, desde aquí se llama a la función clase algorith que es el que "mimifica"
"""
from algorithm import mimifica
from config import TOKEN

from telegram.ext import Updater, CommandHandler


def mimi(bot, update):
    """ Función que reenvía un mensaje mimificado (utiliza la función mimifica):
"""
    respuesta = mimifica(update.message.reply_to_message.text)
    update.message.reply_to_message.reply_text(respuesta, quote = True)

# Token del bot:
updater = Updater(TOKEN)

# Comando /mimi:
updater.dispatcher.add_handler(CommandHandler('mimi', mimi))

# Puesta en funcionamiento del bot:
updater.start_polling()
updater.idle()
