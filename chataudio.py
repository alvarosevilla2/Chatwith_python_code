
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.conversation import Statement
import speech_recognition as sr

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
request=""
entradaDelUsuarioAnterior=""

while True:
    if request=='salir':
        break

    request=input("Yo: ")
    if request=='grabar audio':
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Di algo...")
            audio = r.listen(source)

            try:
                request = r.recognize_google(audio, language='es-ES')
                print("Lo que dijiste: {}".format(request))
            except:
                print("Lo siento, no te entiendo!")

    response=chatbot.get_response(request)
    if levenshtein_distance.compare(Statement(request),error)>0.51:
        print('Bot: ¿Qué debería haber dicho?')
        entradaDelUsuarioCorreccion = input("Yo: ")
        traine.train([entradaDelUsuarioAnterior,entradaDelUsuarioCorreccion]) 
        print("Bot: He aprendiendo que cuando digas {} debo responder {}".format(entradaDelUsuarioAnterior,entradaDelUsuarioCorreccion))

    entradaDelUsuarioAnterior=request
    print('Bot: ', response)


