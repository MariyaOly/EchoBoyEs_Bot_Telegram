import telebot

TOKEN = "6004391555:AAHHVbb2M8DpaMQjbWDwrJuVWwlX8eN6qWI"

bot = telebot.TeleBot(TOKEN)

# Manejador para los comandos '/start' y '/help'
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, "En qué puedo ayudarte?")

# Manejador para documentos y audios
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    bot.reply_to(message, "Vamos a ver qué es..")

@bot.message_handler(content_types=['photo'])
def handle_docs_audio(message):
    bot.reply_to(message, "Nice meme XXD")

@bot.message_handler(content_types=["voice"])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Bonita voz!")

@bot.message_handler(content_types=["text"])
def repeat(message: telebot.types.Message):
    username = message.from_user.username
    text = message.text.lower()

    if text == "hola":
        # Respuesta en español
        bot.reply_to(message, f"Hola @{username}, encantada de conocerte!")

    elif text == "привет":
        # Respuesta en ruso
        bot.reply_to(message, f"Привет @{username}, рада знакомству!")

    else:
        # Repetir el mensaje enviado por el usuario
        bot.reply_to(message, f"@{username} I don´t understand you...Please, don´t use punctuation marks.")

bot.polling(none_stop=True)


##TELEBOT WAS DELETED##