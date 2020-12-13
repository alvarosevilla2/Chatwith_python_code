from PyQt5 import QtCore, QtGui, QtWidgets
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.conversation import Statement
import speech_recognition as sr


class Ui_chatbots(object):
    def setupUi(self, chatbots):
        chatbots.setObjectName("chatbots")
        chatbots.resize(380, 812)
        chatbots.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"\n"
"QWidget{\n"
"background: #464453;\n"
"}\n"
"\n"
"QPushButton{\n"
"background: #CDBCBC;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background: #CDBCBC;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"color: white;\n"
"font-size: 12pt;\n"
"}\n"
"\n"
"QTextEdit{\n"
"background: #EEDEDE;\n"
"border-radius:16px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(chatbots)
        self.centralwidget.setObjectName("centralwidget")
        self.enviar = QtWidgets.QPushButton(self.centralwidget)
        self.enviar.setGeometry(QtCore.QRect(290, 710, 71, 31))
        self.enviar.setObjectName("enviar")
        self.useredit = QtWidgets.QLineEdit(self.centralwidget,returnPressed=self.on_return_pressed)
        self.useredit.setGeometry(QtCore.QRect(10, 710, 271, 31))
        self.useredit.setText("")
        self.atras = QtWidgets.QPushButton(self.centralwidget)
        self.atras.setGeometry(QtCore.QRect(20, 20, 61, 31))
        self.atras.setObjectName("atras")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(150, 20, 91, 21))
        self.titulo.setObjectName("titulo")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget, readOnly=True)
        self.textEdit.setGeometry(QtCore.QRect(10, 80, 361, 591))
        self.textEdit.setObjectName("textEdit")
        chatbots.setCentralWidget(self.centralwidget)

        self.retranslateUi(chatbots)
        QtCore.QMetaObject.connectSlotsByName(chatbots)

    def on_return_pressed(self):

        chatbot=ChatBot('chatpet',

            input_adapter='chatterbot.input.TerminalAdapter', 
            output_adapter='chatterbot.output.TerminalAdapter',

            trainer='chatterbot.trainers.ListTrainer',

            logic_adapters =[
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


        request=str(self.useredit.text())
        if request=='grabar audio':
        r = sr.Recognizer()

        with sr.Microphone() as source:
            response=("Di algo...")
            audio = r.listen(source)

            try:
                request = r.recognize_google(audio, language='es-ES')
                response("Lo que dijiste: {}".format(request))
            except:
                response("Lo siento, no te entiendo!")
        response=chatbot.get_response(str(request))
        if levenshtein_distance.compare(Statement(request),error)>0.51:
            response=("¿Qué debería haber dicho?")
            entradaDelUsuarioCorreccion = str(self.useredit.text())
            traine.train([entradaDelUsuarioAnterior,entradaDelUsuarioCorreccion]) 
            response=("He aprendiendo que cuando digas {} debo responder {}".format(entradaDelUsuarioAnterior,entradaDelUsuarioCorreccion))
        
        
        self.textEdit.append(str(request))
        self.textEdit.setAlignment(QtCore.Qt.AlignRight)
        self.useredit.clear()
        
        self.textEdit.append(str(response))
        self.textEdit.setAlignment(QtCore.Qt.AlignLeft)
        self.useredit.setFocus()


    def retranslateUi(self, chatbots):
        _translate = QtCore.QCoreApplication.translate
        chatbots.setWindowTitle(_translate("chatbots", "chatbots"))
        self.enviar.setText(_translate("chatbots", "Enviar"))
        self.atras.setText(_translate("chatbots", "Atrás"))
        self.titulo.setText(_translate("chatbots", "Chatbot"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    chatbots = QtWidgets.QMainWindow()
    ui = Ui_chatbots()
    ui.setupUi(chatbots)
    chatbots.show()
    sys.exit(app.exec_())
