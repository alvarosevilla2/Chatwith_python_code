import telebot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.conversation import Statement

bot=telebot.TeleBot("1404522334:AAESOUeU9j_Fn-4aTmt_XPwitmNAe0mD1mE")

def bot_coversacional(message):
    chatbot=ChatBot('chatpet',

        input_adapter='chatterbot.input.TerminalAdapter', 
        output_adapter='chatterbot.output.TerminalAdapter',

        trainer='chatterbot.trainers.ListTrainer',

        logic_adapters = [
            {
                "import_path": "chatterbot.logic.BestMatch",
                "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            }
        ],

        preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
        ],
    )

    traine=ListTrainer(chatbot)
    trainer=ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.spanish")
    trainer.train("./chattrain.yml")
    trainer.train("./psico.yml")
    trainer.train("./conversation.yml")
    trainer.train("./covid.yml")
    trainer.train("./mentals.yml")
    trainer.train("./medcurio.yml")

    levenshtein_distance = LevenshteinDistance()

    error=Statement('Te has equivocado')
    entradaDelUsuarioAnterior=""

    respuesta=chatbot.get_response(message)
    if levenshtein_distance.compare(Statement(message),error)>0.60:
        bot.reply_to(message, "¿Qué debería haber dicho?")
        entradaDelUsuarioCorreccion = message
        traine.train([entradaDelUsuarioAnterior,entradaDelUsuarioCorreccion]) 
        bot.reply_to(message, "Bot: He aprendiendo que cuando digas {} debo responder {}".format(entradaDelUsuarioAnterior,entradaDelUsuarioCorreccion))

    entradaDelUsuarioAnterior=message
    bot.reply_to(message, respuesta)
    mensaje=open("respuesta.txt", "w")
    mensaje.write(respuesta)
    mensaje.close()

@bot.message_handler(commands =["help", "start"])
def enviar_mensaje(message):
    bot.reply_to(message, "Hola soy un bot")

@bot.message_handler(func=lambda message:True)
def mensaje(message):
    bot_coversacional(message.text)
    respuesta = open("respuesta.txt", "r")
    respuesta = respuesta.read()
    bot.reply_to(message, respuesta)
bot.polling()
