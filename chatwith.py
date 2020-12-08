from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from ui_register import source
import mysql.connector as mc
import mysql.connector
from ui_Perfil import saravic
from DIariofinal import source5
from monito import sourcemoni
from desafios import source_des
from ui_informacion5 import source50
from ui_principal5 import sourcep
from PyQt5 import QtCore, QtGui, QtWidgets
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.conversation import Statement
import webbrowser


class Ui_Perfil(object):
    def setupUi(self, Perfil):
        Perfil.setObjectName("Perfil")
        Perfil.resize(380, 812)
        Perfil.setFixedSize(380,812)
        Perfil.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"QWidget{\n"
"background-image: url(:/images/images/fondofinal.png);\n"
"}\n"
"QToolButton{\n"
"background: transparent;\n"
"}\n"
"\n"
"QFrame#zorrito{\n"
"background: transparent;\n"
"    image: url(:/images/images/zorro.png);\n"
"}\n"
"QFrame#nivel{\n"
"background: transparent;\n"
"    image: url(:/images/images/nivel sin fondo.png);\n"
"}\n"
"QFrame#contenedor{\n"
"border-radius:15px;\n"
"background: #FACEBB;\n"
"}\n"
"QLabel#nombre{\n"
"background: transparent;\n"
"color: white;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"}\n"
"QLabel{\n"
"background: transparent;\n"
"font-size: 14px;\n"
"}\n"
"QFrame#one{\n"
"border-radius:5px;\n"
"background: #940606;\n"
"}\n"
"QFrame#two{\n"
"border-radius:5px;\n"
"background: #940606;\n"
"}\n"
"QFrame#three{\n"
"border-radius:5px;\n"
"background: #940606;\n"
"}\n"
"QFrame#four{\n"
"border-radius:5px;\n"
"background: #940606;\n"
"}\n"
"QFrame#five{\n"
"border-radius:5px;\n"
"background: #940606;\n"
"}\n"
"QFrame#six{\n"
"border-radius:5px;\n"
"background: #940606;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Perfil)
        self.centralwidget.setObjectName("centralwidget")
        self.zorrito = QtWidgets.QFrame(self.centralwidget)
        self.zorrito.setGeometry(QtCore.QRect(110, 110, 151, 141))
        self.zorrito.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.zorrito.setFrameShadow(QtWidgets.QFrame.Raised)
        self.zorrito.setObjectName("zorrito")
        self.nivel = QtWidgets.QFrame(self.centralwidget)
        self.nivel.setGeometry(QtCore.QRect(240, 60, 131, 91))
        self.nivel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.nivel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.nivel.setObjectName("nivel")
        self.contenedor = QtWidgets.QFrame(self.centralwidget)
        self.contenedor.setGeometry(QtCore.QRect(40, 310, 311, 441))
        self.contenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedor.setObjectName("contenedor")
        self.uno = QtWidgets.QLabel(self.contenedor)
        self.uno.setGeometry(QtCore.QRect(60, 30, 171, 31))
        self.uno.setObjectName("uno")
        self.dos = QtWidgets.QLabel(self.contenedor)
        self.dos.setGeometry(QtCore.QRect(60, 100, 191, 21))
        self.dos.setObjectName("dos")
        self.tres = QtWidgets.QLabel(self.contenedor)
        self.tres.setGeometry(QtCore.QRect(60, 120, 111, 31))
        self.tres.setObjectName("tres")
        self.cuatro = QtWidgets.QLabel(self.contenedor)
        self.cuatro.setGeometry(QtCore.QRect(60, 170, 171, 31))
        self.cuatro.setObjectName("cuatro")
        self.cinco = QtWidgets.QLabel(self.contenedor)
        self.cinco.setGeometry(QtCore.QRect(60, 200, 61, 16))
        self.cinco.setObjectName("cinco")
        self.seis = QtWidgets.QLabel(self.contenedor)
        self.seis.setGeometry(QtCore.QRect(60, 250, 211, 21))
        self.seis.setObjectName("seis")
        self.siete = QtWidgets.QLabel(self.contenedor)
        self.siete.setGeometry(QtCore.QRect(60, 310, 241, 21))
        self.siete.setObjectName("siete")
        self.ocho = QtWidgets.QLabel(self.contenedor)
        self.ocho.setGeometry(QtCore.QRect(60, 330, 71, 21))
        self.ocho.setObjectName("ocho")
        self.label = QtWidgets.QLabel(self.contenedor)
        self.label.setGeometry(QtCore.QRect(60, 380, 191, 31))
        self.label.setObjectName("label")
        self.one = QtWidgets.QFrame(self.contenedor)
        self.one.setGeometry(QtCore.QRect(10, 40, 31, 21))
        self.one.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.one.setFrameShadow(QtWidgets.QFrame.Raised)
        self.one.setObjectName("one")
        self.two = QtWidgets.QFrame(self.contenedor)
        self.two.setGeometry(QtCore.QRect(10, 100, 31, 21))
        self.two.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.two.setFrameShadow(QtWidgets.QFrame.Raised)
        self.two.setObjectName("two")
        self.three = QtWidgets.QFrame(self.contenedor)
        self.three.setGeometry(QtCore.QRect(10, 180, 31, 21))
        self.three.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.three.setFrameShadow(QtWidgets.QFrame.Raised)
        self.three.setObjectName("three")
        self.four = QtWidgets.QFrame(self.contenedor)
        self.four.setGeometry(QtCore.QRect(10, 250, 31, 21))
        self.four.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.four.setFrameShadow(QtWidgets.QFrame.Raised)
        self.four.setObjectName("four")
        self.five = QtWidgets.QFrame(self.contenedor)
        self.five.setGeometry(QtCore.QRect(10, 310, 31, 21))
        self.five.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.five.setFrameShadow(QtWidgets.QFrame.Raised)
        self.five.setObjectName("five")
        self.six = QtWidgets.QFrame(self.contenedor)
        self.six.setGeometry(QtCore.QRect(10, 390, 31, 21))
        self.six.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.six.setFrameShadow(QtWidgets.QFrame.Raised)
        self.six.setObjectName("six")
        self.nombre = QtWidgets.QLabel(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(130, 260, 131, 21))
        self.nombre.setObjectName("nombre")
        self.atras = QtWidgets.QToolButton(self.centralwidget)
        self.atras.setGeometry(QtCore.QRect(10, 50, 71, 21))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/atras.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.atras.setIcon(icon)
        self.atras.setIconSize(QtCore.QSize(80, 80))
        self.atras.setObjectName("atras")
        Perfil.setCentralWidget(self.centralwidget)

        self.retranslateUi(Perfil)
        QtCore.QMetaObject.connectSlotsByName(Perfil)

    def retranslateUi(self, Perfil):
        _translate = QtCore.QCoreApplication.translate
        Perfil.setWindowTitle(_translate("Perfil", "Perfil"))
        self.uno.setText(_translate("Perfil", "Horas activas: 64 horas"))
        self.dos.setText(_translate("Perfil", "N° mascotas de mascotas "))
        self.tres.setText(_translate("Perfil", "desbloquedas : 1l"))
        self.cuatro.setText(_translate("Perfil", "Temática más recurrente: "))
        self.cinco.setText(_translate("Perfil", "Música"))
        self.seis.setText(_translate("Perfil", "Puntaje obtenido: 120 puntos"))
        self.siete.setText(_translate("Perfil", "Frecuencia de uso de la mascota:"))
        self.ocho.setText(_translate("Perfil", " regular"))
        self.label.setText(_translate("Perfil", "N° de trofeos obtenidos: 1"))
        self.nombre.setText(_translate("Perfil", "Alvaro Sevilla"))
        self.atras.setText(_translate("Perfil", "..."))

class Ui_chatbots(object):
    def setupUi(self, chatbots):
        chatbots.setObjectName("chatbots")
        chatbots.resize(380, 812)
        chatbots.setFixedSize(380,812)
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
        self.useredit = QtWidgets.QLineEdit(self.centralwidget)
        self.useredit.setGeometry(QtCore.QRect(10, 710, 271, 31))
        self.useredit.setText("")
        self.useredit.setObjectName("useredit")
        self.atras = QtWidgets.QPushButton(self.centralwidget)
        self.atras.setGeometry(QtCore.QRect(20, 20, 61, 31))
        self.atras.setObjectName("atras")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(150, 20, 91, 21))
        self.titulo.setObjectName("titulo")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 80, 361, 591))
        self.textEdit.setObjectName("textEdit")
        chatbots.setCentralWidget(self.centralwidget)

        self.retranslateUi(chatbots)
        QtCore.QMetaObject.connectSlotsByName(chatbots)

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

        levenshtein_distance = LevenshteinDistance()

        error=Statement('Te has equivocado')
        request=""
        entradaDelUsuarioAnterior=""

        request=str(self.useredit)
        response=str(chatbot.get_response(request))
        if levenshtein_distance.compare(Statement(request),error)>0.51:
            response='Bot: ¿Qué debería haber dicho?'
            entradaDelUsuarioCorreccion = self.useredit
            traine.train([entradaDelUsuarioAnterior,entradaDelUsuarioCorreccion]) 
            print("Bot: He aprendiendo que cuando digas {} debo responder {}".format(entradaDelUsuarioAnterior,entradaDelUsuarioCorreccion))

        entradaDelUsuarioAnterior=request
        if self.enviar.clicked :
            self.textEdit.append("{}".format(request))
        self.textEdit.setPlainText(response)

    def retranslateUi(self, chatbots):
        _translate = QtCore.QCoreApplication.translate
        chatbots.setWindowTitle(_translate("chatbots", "chatbots"))
        self.enviar.setText(_translate("chatbots", "Enviar"))
        self.atras.setText(_translate("chatbots", "Atrás"))
        self.titulo.setText(_translate("chatbots", "Chatbot"))

class Ui_Diario_1(object):
    def setupUi(self, Diario_1):
        Diario_1.setObjectName("Diario_1")
        Diario_1.resize(380, 812)
        Diario_1.setFixedSize(380,812)
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(65)
        Diario_1.setFont(font)
        Diario_1.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"\n"
"QWidget{\n"
"background-image: url(:/images/images/fondo.png);\n"
"}\n"
"QFrame#Escribe{\n"
"background: #EDCAC5;\n"
"border-radius: 15px;\n"
"}\n"
"QToolButton#guardar{\n"
"background: #51C55D;\n"
"border-radius: 15px;\n"
"}\n"
"QFrame#graba{\n"
"background: #EFE9B0;\n"
"border-radius: 15px;\n"
"}\n"
"QToolButton#voz{\n"
"background: #EFE9B0;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPlainTextEdit#Escribediario{\n"
"background: #EFC8C2;\n"
"border:  #EFC8C2;\n"
"}\n"
"QTextBrowser#Diario_2{\n"
"background: #FFFEEA;\n"
"border:  #FFFEEA;\n"
"}\n"
"QToolButton#anotaciones{\n"
"background: #DED482;\n"
"border-radius: 15px;\n"
"}\n"
"QLabel#graba_2{\n"
"color: black;\n"
"background: #EFE9B0;\n"
"}\n"
"QToolButton#atras{\n"
"background: #FFFEEA;\n"
"border-radius: 15px;\n"
"}\n"
"QFrame#wifi{\n"
"background: #FFFEEA;\n"
"border-radius: 15px;\n"
"image: url(:/images/images/hora.png);\n"
"}")
        Diario_1.setIconSize(QtCore.QSize(25, 25))
        self.centralwidget = QtWidgets.QWidget(Diario_1)
        self.centralwidget.setObjectName("centralwidget")
        self.Escribe = QtWidgets.QFrame(self.centralwidget)
        self.Escribe.setGeometry(QtCore.QRect(20, 240, 331, 301))
        self.Escribe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Escribe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Escribe.setObjectName("Escribe")
        self.Escribediario = QtWidgets.QPlainTextEdit(self.Escribe)
        self.Escribediario.setGeometry(QtCore.QRect(30, 20, 281, 261))
        self.Escribediario.setObjectName("Escribediario")
        self.guardar = QtWidgets.QToolButton(self.centralwidget)
        self.guardar.setGeometry(QtCore.QRect(100, 670, 181, 51))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.guardar.setFont(font)
        self.guardar.setObjectName("guardar")
        self.graba = QtWidgets.QFrame(self.centralwidget)
        self.graba.setGeometry(QtCore.QRect(30, 560, 311, 61))
        self.graba.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graba.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graba.setObjectName("graba")
        self.voz = QtWidgets.QToolButton(self.graba)
        self.voz.setGeometry(QtCore.QRect(260, 20, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/voz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.voz.setIcon(icon)
        self.voz.setIconSize(QtCore.QSize(35, 35))
        self.voz.setObjectName("voz")
        self.graba_2 = QtWidgets.QLabel(self.graba)
        self.graba_2.setGeometry(QtCore.QRect(30, 20, 51, 16))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.graba_2.setFont(font)
        self.graba_2.setObjectName("graba_2")
        self.Diario_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.Diario_2.setGeometry(QtCore.QRect(10, 100, 321, 121))
        self.Diario_2.setObjectName("Diario_2")
        self.anotaciones = QtWidgets.QToolButton(self.centralwidget)
        self.anotaciones.setGeometry(QtCore.QRect(130, 750, 110, 31))
        self.anotaciones.setObjectName("anotaciones")
        self.atras = QtWidgets.QToolButton(self.centralwidget)
        self.atras.setGeometry(QtCore.QRect(10, 50, 61, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/atrás.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.atras.setIcon(icon1)
        self.atras.setIconSize(QtCore.QSize(80, 80))
        self.atras.setObjectName("atras")
        self.wifi = QtWidgets.QFrame(self.centralwidget)
        self.wifi.setGeometry(QtCore.QRect(0, 0, 371, 41))
        self.wifi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wifi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wifi.setObjectName("wifi")
        Diario_1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Diario_1)
        QtCore.QMetaObject.connectSlotsByName(Diario_1)

    def retranslateUi(self, Diario_1):
        _translate = QtCore.QCoreApplication.translate
        Diario_1.setWindowTitle(_translate("Diario_1", "Diario"))
        self.Escribediario.setPlainText(_translate("Diario_1", "Escribe"))
        self.guardar.setText(_translate("Diario_1", "Guardar"))
        self.voz.setText(_translate("Diario_1", "..."))
        self.graba_2.setText(_translate("Diario_1", "Graba"))
        self.Diario_2.setHtml(_translate("Diario_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'century gothic\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt; font-weight:600;\">Diario</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt;\">Plasma tus emociones</span></p></body></html>"))
        self.anotaciones.setText(_translate("Diario_1", "Ver anotaciones"))
        self.atras.setText(_translate("Diario_1", "..."))


class Ui_monito(object):
    def setupUi(self, monito):
        monito.setObjectName("monito")
        monito.resize(380, 812)
        monito.setFixedSize(380,812)
        monito.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"background-image: url(:/images/images/fdeca2.png);\n"
"}\n"
"\n"
"QLabel#tit{\n"
"background:transparent;\n"
"font-weight:bold;\n"
"font-size:26px;\n"
"}\n"
"\n"
"QLabel#des{\n"
"background:transparent;\n"
"}\n"
"\n"
"QFrame{\n"
"background: transparent;\n"
"}\n"
"\n"
"QFrame#hora{\n"
"image: url(:/images/images/hora sara.png);\n"
"}\n"
"\n"
"QFrame#atras{\n"
"image: url(:/images/images/atras.png);\n"
"}\n"
"\n"
"QFrame#frame{\n"
"image: url(:/images/images/blanco.png);\n"
"}\n"
"\n"
"QFrame#frame{\n"
"image: url(:/images/images/blanco.png);\n"
"}\n"
"\n"
"QFrame#frame_2{\n"
"image: url(:/images/images/blanco.png);\n"
"}\n"
"\n"
"QFrame#frame_3{\n"
"image: url(:/images/images/blanco.png);\n"
"}\n"
"\n"
"QFrame#grafi{\n"
"image: url(:/images/images/blanco.png);\n"
"}\n"
"\n"
"QFrame#grafi1{\n"
"image: url(:/images/images/barras.png);\n"
"}\n"
"\n"
"QFrame#grafi2{\n"
"image: url(:/images/images/torta.jpg);\n"
"}\n"
"\n"
"QToolButton#oct{\n"
"color: white;\n"
"background: #3F414E;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QToolButton#nov{\n"
"color: white;\n"
"background: #3F414E;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QToolButton#rep1{\n"
"background: #F49494;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QToolButton#rep2{\n"
"background: #F49494;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QToolButton#rep3{\n"
"background: #F49494;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton#but1{\n"
"border-radius:15px;\n"
"image: url(:/images/images/cuesto.jpg);\n"
"background: transparent;\n"
"}\n"
"\n"
"QPushButton#but2{\n"
"border-radius:15px;\n"
"image: url(:/images/images/pira.png);\n"
"background: transparent;\n"
"}\n"
"\n"
"QPushButton#but3{\n"
"border-radius:15px;\n"
"image: url(:/images/images/cuesto.jpg);\n"
"background: transparent;\n"
"}\n"
"\n"
"QPushButton#but4{\n"
"border-radius:15px;\n"
"image: url(:/images/images/pira.png);\n"
"background: transparent;\n"
"}\n"
"\n"
"QPushButton#but5{\n"
"border-radius:15px;\n"
"image: url(:/images/images/cuesto.jpg);\n"
"background: transparent;\n"
"}\n"
"\n"
"QPushButton#but6{\n"
"border-radius:15px;\n"
"image: url(:/images/images/pira.png);\n"
"background: transparent;\n"
"}\n"
"\n"
"QToolButton{\n"
"color: white;\n"
"background: #3F414E;\n"
"border-radius:15px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(monito)
        self.centralwidget.setObjectName("centralwidget")
        self.tit = QtWidgets.QLabel(self.centralwidget)
        self.tit.setGeometry(QtCore.QRect(130, 70, 131, 41))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.tit.setFont(font)
        self.tit.setObjectName("tit")
        self.des = QtWidgets.QLabel(self.centralwidget)
        self.des.setGeometry(QtCore.QRect(20, 110, 311, 41))
        self.des.setObjectName("des")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 170, 270, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.but1 = QtWidgets.QPushButton(self.frame)
        self.but1.setGeometry(QtCore.QRect(50, 50, 90, 55))
        self.but1.setText("")
        self.but1.setObjectName("but1")
        self.but2 = QtWidgets.QPushButton(self.frame)
        self.but2.setGeometry(QtCore.QRect(150, 50, 90, 50))
        self.but2.setText("")
        self.but2.setObjectName("but2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(60, 320, 270, 150))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.but3 = QtWidgets.QPushButton(self.frame_2)
        self.but3.setGeometry(QtCore.QRect(50, 50, 90, 55))
        self.but3.setText("")
        self.but3.setObjectName("but3")
        self.but4 = QtWidgets.QPushButton(self.frame_2)
        self.but4.setGeometry(QtCore.QRect(150, 50, 90, 50))
        self.but4.setText("")
        self.but4.setObjectName("but4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(60, 430, 270, 150))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.but5 = QtWidgets.QPushButton(self.frame_3)
        self.but5.setGeometry(QtCore.QRect(50, 50, 90, 55))
        self.but5.setText("")
        self.but5.setObjectName("but5")
        self.but6 = QtWidgets.QPushButton(self.frame_3)
        self.but6.setGeometry(QtCore.QRect(150, 50, 90, 50))
        self.but6.setText("")
        self.but6.setObjectName("but6")
        self.grafi = QtWidgets.QFrame(self.centralwidget)
        self.grafi.setGeometry(QtCore.QRect(60, 620, 270, 150))
        self.grafi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.grafi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.grafi.setObjectName("grafi")
        self.grafi2 = QtWidgets.QFrame(self.grafi)
        self.grafi2.setGeometry(QtCore.QRect(160, 20, 91, 101))
        self.grafi2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.grafi2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.grafi2.setObjectName("grafi2")
        self.grafi1 = QtWidgets.QFrame(self.grafi)
        self.grafi1.setGeometry(QtCore.QRect(20, 30, 120, 80))
        self.grafi1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.grafi1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.grafi1.setObjectName("grafi1")
        self.resu = QtWidgets.QToolButton(self.grafi)
        self.resu.setGeometry(QtCore.QRect(60, 0, 151, 20))
        self.resu.setObjectName("resu")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(190, 550, 82, 17))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 570, 82, 17))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(190, 590, 82, 17))
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.oct = QtWidgets.QToolButton(self.centralwidget)
        self.oct.setGeometry(QtCore.QRect(65, 170, 71, 19))
        self.oct.setObjectName("oct")
        self.nov = QtWidgets.QToolButton(self.centralwidget)
        self.nov.setGeometry(QtCore.QRect(65, 320, 71, 21))
        self.nov.setObjectName("nov")
        self.rep1 = QtWidgets.QToolButton(self.centralwidget)
        self.rep1.setGeometry(QtCore.QRect(70, 200, 61, 19))
        self.rep1.setObjectName("rep1")
        self.rep2 = QtWidgets.QToolButton(self.centralwidget)
        self.rep2.setGeometry(QtCore.QRect(70, 350, 61, 19))
        self.rep2.setObjectName("rep2")
        self.rep3 = QtWidgets.QToolButton(self.centralwidget)
        self.rep3.setGeometry(QtCore.QRect(70, 460, 61, 19))
        self.rep3.setObjectName("rep3")
        self.atras = QtWidgets.QFrame(self.centralwidget)
        self.atras.setGeometry(QtCore.QRect(20, 10, 81, 41))
        self.atras.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.atras.setFrameShadow(QtWidgets.QFrame.Raised)
        self.atras.setObjectName("atras")
        monito.setCentralWidget(self.centralwidget)

        self.retranslateUi(monito)
        QtCore.QMetaObject.connectSlotsByName(monito)

    def retranslateUi(self, monito):
        _translate = QtCore.QCoreApplication.translate
        monito.setWindowTitle(_translate("monito", "MainWindow"))
        self.tit.setText(_translate("monito", "Monitoreo"))
        self.des.setText(_translate("monito", "Aqui podras encontrar tus resultados de los cuestionarios"))
        self.resu.setText(_translate("monito", "Resumen de cuestionarios"))
        self.oct.setText(_translate("monito", "Octubre"))
        self.nov.setText(_translate("monito", "Noviembre"))
        self.rep1.setText(_translate("monito", "Reporte 1"))
        self.rep2.setText(_translate("monito", "Reporte 2"))
        self.rep3.setText(_translate("monito", "Reporte 3"))


class Ui_desafios(object):
    def setupUi(self, desafios):
        desafios.setObjectName("desafios")
        desafios.resize(380, 810)
        desafios.setFixedSize(380,812)
        desafios.setAutoFillBackground(True)
        desafios.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"\n"
"QWidget#centralwidget{\n"
"background-image: url(:/images/images/fondo amarillo patito.png);\n"
"}\n"
"\n"
"QFrame#jk1{\n"
"image: url(:/images/images/panel central.png);\n"
"border-radius:13px;\n"
"}\n"
"QPushButton#Atras{\n"
"background: transparent;\n"
"font-size:14px;\n"
"color:#494d49;\n"
"border-color: transparent;\n"
"}\n"
"QPushButton#Atras:hover{\n"
"background:transparent;\n"
"font-size:15px;\n"
"color:black;\n"
"border-color: transparent;\n"
"}\n"
"QLabel{\n"
"font-weight:bold;\n"
"color:black;\n"
"}\n"
"QLabel#titulo{\n"
"font-weight:bold;\n"
"color:black;\n"
"font-size:25px;\n"
"}\n"
"QLabel#descripcion{\n"
"color:black;\n"
"font-size:14px;\n"
"}\n"
"\n"
"QPushButton#ad{\n"
"background:#51C55D;\n"
"color:#494d49;\n"
"font-size:15px;\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#ad:hover{\n"
"background:#49b855;\n"
"color:white;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"border-radius:30px;\n"
"}\n"
"QPushButton{\n"
"background:transparent;\n"
"border-radius:12px;\n"
"border:1px solid;\n"
"}\n"
"QPushButton:hover{\n"
"background:transparent;\n"
"border-radius:12px;\n"
"border:3px solid;\n"
"}\n"
"QPushButton#uv_2{\n"
"background:transparent;\n"
"border-radius:13px;\n"
"border:1px solid;\n"
"}\n"
"QPushButton#uv_2:hover{\n"
"background:transparent;\n"
"border-radius:13px;\n"
"border:3px solid;\n"
"}\n"
"QFramer#hora{\n"
"image: url(:/images/images/hora.png);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(desafios)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.jk1 = QtWidgets.QFrame(self.centralwidget)
        self.jk1.setGeometry(QtCore.QRect(10, 170, 361, 471))
        self.jk1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.jk1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.jk1.setObjectName("jk1")
        self.uv = QtWidgets.QPushButton(self.jk1)
        self.uv.setGeometry(QtCore.QRect(114, 106, 24, 24))
        self.uv.setText("")
        self.uv.setObjectName("uv")
        self.uv_2 = QtWidgets.QPushButton(self.jk1)
        self.uv_2.setGeometry(QtCore.QRect(76, 6, 26, 26))
        self.uv_2.setText("")
        self.uv_2.setObjectName("uv_2")
        self.uv_3 = QtWidgets.QPushButton(self.jk1)
        self.uv_3.setGeometry(QtCore.QRect(39, 86, 24, 24))
        self.uv_3.setText("")
        self.uv_3.setObjectName("uv_3")
        self.uv_4 = QtWidgets.QPushButton(self.jk1)
        self.uv_4.setGeometry(QtCore.QRect(283, 96, 24, 24))
        self.uv_4.setText("")
        self.uv_4.setObjectName("uv_4")
        self.uv_5 = QtWidgets.QPushButton(self.jk1)
        self.uv_5.setGeometry(QtCore.QRect(239, 17, 24, 24))
        self.uv_5.setText("")
        self.uv_5.setObjectName("uv_5")
        self.uv_7 = QtWidgets.QPushButton(self.jk1)
        self.uv_7.setGeometry(QtCore.QRect(63, 219, 24, 24))
        self.uv_7.setText("")
        self.uv_7.setObjectName("uv_7")
        self.uv_6 = QtWidgets.QPushButton(self.jk1)
        self.uv_6.setGeometry(QtCore.QRect(46, 317, 24, 24))
        self.uv_6.setText("")
        self.uv_6.setObjectName("uv_6")
        self.uv_9 = QtWidgets.QPushButton(self.jk1)
        self.uv_9.setGeometry(QtCore.QRect(274, 316, 24, 24))
        self.uv_9.setText("")
        self.uv_9.setObjectName("uv_9")
        self.uv_8 = QtWidgets.QPushButton(self.jk1)
        self.uv_8.setGeometry(QtCore.QRect(160, 298, 24, 24))
        self.uv_8.setText("")
        self.uv_8.setObjectName("uv_8")
        self.uv_10 = QtWidgets.QPushButton(self.jk1)
        self.uv_10.setGeometry(QtCore.QRect(114, 401, 24, 24))
        self.uv_10.setText("")
        self.uv_10.setObjectName("uv_10")
        self.uv_11 = QtWidgets.QPushButton(self.jk1)
        self.uv_11.setGeometry(QtCore.QRect(285, 413, 24, 24))
        self.uv_11.setText("")
        self.uv_11.setObjectName("uv_11")
        self.uv_12 = QtWidgets.QPushButton(self.jk1)
        self.uv_12.setGeometry(QtCore.QRect(259, 175, 24, 24))
        self.uv_12.setText("")
        self.uv_12.setObjectName("uv_12")
        self.Atras = QtWidgets.QPushButton(self.centralwidget)
        self.Atras.setGeometry(QtCore.QRect(0, 40, 75, 23))
        self.Atras.setObjectName("Atras")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(130, 60, 111, 41))
        self.titulo.setObjectName("titulo")
        self.descripcion = QtWidgets.QLabel(self.centralwidget)
        self.descripcion.setGeometry(QtCore.QRect(35, 120, 311, 40))
        self.descripcion.setObjectName("descripcion")
        self.ad = QtWidgets.QPushButton(self.centralwidget)
        self.ad.setGeometry(QtCore.QRect(75, 690, 231, 61))
        self.ad.setObjectName("ad")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 380, 51))
        self.frame.setStyleSheet("image: url(:/images/images/hora con nuevas dimensiones.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        desafios.setCentralWidget(self.centralwidget)

        self.retranslateUi(desafios)
        QtCore.QMetaObject.connectSlotsByName(desafios)

    def retranslateUi(self, desafios):
        _translate = QtCore.QCoreApplication.translate
        desafios.setWindowTitle(_translate("desafios", "desafios"))
        self.Atras.setText(_translate("desafios", "← Atrás"))
        self.titulo.setText(_translate("desafios", "Desafíos"))
        self.descripcion.setText(_translate("desafios", "Cumple los retos y desarrolla nuevos hábitos"))
        self.ad.setText(_translate("desafios", "Guardar progreso"))


class Ui_Informacion(object):
    def setupUi(self, Informacion):
        Informacion.setObjectName("Informacion")
        Informacion.resize(380, 812)
        Informacion.setFixedSize(380,812)
        self.centralwidget = QtWidgets.QWidget(Informacion)
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setItalic(True)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("*{\n"
"    \n"
"font-family:century gothic;\n"
"}\n"
"QWidget{\n"
"\n"
"    background-image: url(:/newPrefix/Imagenes/fondo.jpeg);\n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"QLabel#salud {\n"
"font-size:24px;\n"
"font-weight:bold; \n"
" \n"
"}\n"
"QLabel#texto {\n"
"align:center;\n"
"\n"
" \n"
"}\n"
"QPushButton{\n"
"background :#51C55D;\n"
"border-radius: 15px;\n"
"}    \n"
"QPushButton:hover{\n"
"background :#3bb547;\n"
"border-radius: 15px;\n"
"font-weight:bold;\n"
"}    \n"
"QLabel#bateria{\n"
"image: url(:/newPrefix/Imagenes/Vector (4).png);\n"
"}\n"
"QLabel#senial{\n"
"    image: url(:/newPrefix/Imagenes/Vector (2).png);\n"
"}\n"
"QLabel#hora{\n"
"    image: url(:/newPrefix/Imagenes/Vector (1).png);\n"
"}\n"
"QLabel#wifi{\n"
"    \n"
"    image: url(:/newPrefix/Imagenes/Vector (3).png);\n"
"}\n"
"QLabel#contorno{\n"
"    \n"
"    image: url(:/newPrefix/Imagenes/Border.png);\n"
"}\n"
"QLabel#boton{\n"
"    \n"
"    image: url(:/newPrefix/Imagenes/Vector (5).png);\n"
"}\n"
"QLabel#boton2{\n"
"    image: url(:/newPrefix/Imagenes/Vector (6).png);\n"
"}\n"
"QLabel#flecha{\n"
"    image: url(:/newPrefix/Imagenes/shape.png);\n"
"}\n"
"QLabel#bateria{\n"
"\n"
"image:    url(:/newPrefix/Imagenes/Captura.PNG);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 550, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.gato = QtWidgets.QLabel(self.centralwidget)
        self.gato.setGeometry(QtCore.QRect(90, 230, 211, 171))
        self.gato.setStyleSheet("image: url(:/newPrefix/Imagenes/undraw_Playful_cat_rchv 1.png)")
        self.gato.setText("")
        self.gato.setObjectName("gato")
        self.texto = QtWidgets.QLabel(self.centralwidget)
        self.texto.setGeometry(QtCore.QRect(50, 420, 291, 91))
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        self.texto.setObjectName("texto")
        self.salud = QtWidgets.QLabel(self.centralwidget)
        self.salud.setGeometry(QtCore.QRect(120, 160, 161, 41))
        self.salud.setObjectName("salud")
        self.wifi = QtWidgets.QLabel(self.centralwidget)
        self.wifi.setGeometry(QtCore.QRect(280, 50, 21, 16))
        self.wifi.setText("")
        self.wifi.setObjectName("wifi")
        self.senial = QtWidgets.QLabel(self.centralwidget)
        self.senial.setGeometry(QtCore.QRect(230, 50, 31, 16))
        self.senial.setText("")
        self.senial.setObjectName("senial")
        self.hora = QtWidgets.QLabel(self.centralwidget)
        self.hora.setGeometry(QtCore.QRect(30, 50, 55, 16))
        self.hora.setText("")
        self.hora.setObjectName("hora")
        self.boton = QtWidgets.QLabel(self.centralwidget)
        self.boton.setGeometry(QtCore.QRect(200, 630, 21, 16))
        self.boton.setText("")
        self.boton.setObjectName("boton")
        self.boton2 = QtWidgets.QLabel(self.centralwidget)
        self.boton2.setGeometry(QtCore.QRect(170, 630, 16, 16))
        self.boton2.setText("")
        self.boton2.setObjectName("boton2")
        self.flecha = QtWidgets.QLabel(self.centralwidget)
        self.flecha.setGeometry(QtCore.QRect(20, 100, 55, 16))
        self.flecha.setText("")
        self.flecha.setObjectName("flecha")
        self.bateria = QtWidgets.QLabel(self.centralwidget)
        self.bateria.setGeometry(QtCore.QRect(310, 50, 55, 16))
        self.bateria.setText("")
        self.bateria.setObjectName("bateria")
        Informacion.setCentralWidget(self.centralwidget)

        self.retranslateUi(Informacion)
        QtCore.QMetaObject.connectSlotsByName(Informacion)
        self.pushButton.clicked.connect(self.link)

    def link(self):
        webbrowser.open_new("https://www.who.int/es/campaigns/connecting-the-world-to-combat-coronavirus/healthyathome/healthyathome---mental-health?gclid=Cj0KCQiAkuP9BRCkARIsAKGLE8Wh9uXm6bJRO6WIM1fjHPAE5hdoNIX-pzbL9Z8CP-VdMcPeaptBGhMaArO3EALw_wcB")


    def retranslateUi(self, Informacion):
        _translate = QtCore.QCoreApplication.translate
        Informacion.setWindowTitle(_translate("Informacion", "Informacion"))
        self.pushButton.setText(_translate("Informacion", "Más Información"))
        self.texto.setText(_translate("Informacion", "Recuerda que tu salud mental\n"
" es tan importante como tu salud física.\n"
"Si quisieras saber más , presiona el botón."))
        self.salud.setText(_translate("Informacion", "Salud Mental"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 810)
        MainWindow.setFixedSize(380,812)
        MainWindow.setStyleSheet("*{\n"
"font-style: century gothic;\n"
"}\n"
"QWidget#centralwidget{\n"
"background-image: url(:/images/images/fondo config nuevas dimensiones.png);\n"
"}\n"
"QFrame#hora{\n"
"background-image: url(:/images/images/hora nuevas dimensiones.png);\n"
"}\n"
"QPushButton#Atras{\n"
"background: transparent;\n"
"border:none;\n"
"font-size:25px;\n"
"}\n"
"QPushButton#Atras:hover{\n"
"background: transparent;\n"
"border:none;\n"
"font-size:27px;\n"
"font-weigth:bold;\n"
"}\n"
"QLabel#titulo{\n"
"font-size:25px;\n"
"background:transparent;\n"
"}\n"
"QFrame{\n"
"background:#7A0808;\n"
"border-radius:8px;\n"
"}\n"
"QPushButton{\n"
"font-size:15px;\n"
"background:transparent;\n"
"}\n"
"QPushButton:hover{\n"
"font-size:15px;\n"
"background:transparent;\n"
"font-weight:bold;\n"
"}\n"
"QFrame#tuerca{\n"
"background-image: url(:/images/images/Screenshot_1.png);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hora = QtWidgets.QFrame(self.centralwidget)
        self.hora.setGeometry(QtCore.QRect(0, 0, 379, 37))
        self.hora.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hora.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hora.setObjectName("hora")
        self.Atras = QtWidgets.QPushButton(self.centralwidget)
        self.Atras.setGeometry(QtCore.QRect(0, 50, 61, 31))
        self.Atras.setObjectName("Atras")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(90, 60, 201, 71))
        self.titulo.setObjectName("titulo")
        self.puntitos = QtWidgets.QFrame(self.centralwidget)
        self.puntitos.setGeometry(QtCore.QRect(30, 170, 16, 16))
        self.puntitos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puntitos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puntitos.setObjectName("puntitos")
        self.puntitos_2 = QtWidgets.QFrame(self.centralwidget)
        self.puntitos_2.setGeometry(QtCore.QRect(30, 240, 16, 16))
        self.puntitos_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puntitos_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puntitos_2.setObjectName("puntitos_2")
        self.puntitos_3 = QtWidgets.QFrame(self.centralwidget)
        self.puntitos_3.setGeometry(QtCore.QRect(30, 310, 16, 16))
        self.puntitos_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puntitos_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puntitos_3.setObjectName("puntitos_3")
        self.puntitos_4 = QtWidgets.QFrame(self.centralwidget)
        self.puntitos_4.setGeometry(QtCore.QRect(30, 380, 16, 16))
        self.puntitos_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puntitos_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puntitos_4.setObjectName("puntitos_4")
        self.puntitos_5 = QtWidgets.QFrame(self.centralwidget)
        self.puntitos_5.setGeometry(QtCore.QRect(30, 450, 16, 16))
        self.puntitos_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puntitos_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puntitos_5.setObjectName("puntitos_5")
        self.puntitos_6 = QtWidgets.QFrame(self.centralwidget)
        self.puntitos_6.setGeometry(QtCore.QRect(30, 520, 16, 16))
        self.puntitos_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.puntitos_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.puntitos_6.setObjectName("puntitos_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 170, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 310, 161, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 230, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 380, 171, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 450, 121, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 520, 101, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tuerca = QtWidgets.QFrame(self.centralwidget)
        self.tuerca.setGeometry(QtCore.QRect(130, 600, 120, 121))
        self.tuerca.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tuerca.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tuerca.setObjectName("tuerca")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Atras.setText(_translate("MainWindow", "←"))
        self.titulo.setText(_translate("MainWindow", "CONFIGURACIÓN"))
        self.pushButton.setText(_translate("MainWindow", "Privacidad"))
        self.pushButton_2.setText(_translate("MainWindow", "Configuración de chat"))
        self.pushButton_3.setText(_translate("MainWindow", "Seguridad"))
        self.pushButton_4.setText(_translate("MainWindow", "Términos y condiciones"))
        self.pushButton_5.setText(_translate("MainWindow", "Obetener ayuda"))
        self.pushButton_6.setText(_translate("MainWindow", "Cerrar sesión"))


class Ui_Inicio(object):
    def setupUi(self, Inicio):
        Inicio.setObjectName("Inicio")
        Inicio.resize(380, 812)
        Inicio.setFixedSize(380,812)
        Inicio.setStyleSheet("*{\n"
"font-family century gothic;\n"
"}\n"
"\n"
"QWidget{\n"
"background-image:url(:/imagenes/imagenes/29 (1).png);\n"
"}\n"
"QLabel{\n"
"background: transparent;\n"
"color: white;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton{\n"
"background: transparent;\n"
"color: white;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton#mascota{\n"
"background-image: url(:/imagenes/imagenes/fox 1.png);\n"
"border-radius: 35px;\n"
"}\n"
"QPushButton#salvavidas{\n"
"background: transparent;\n"
"background-image:url(:/imagenes/imagenes/WhatsApp Image 2020-10-14 at 2.00 1.png);\n"
"border-radius: 25px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Inicio)
        self.centralwidget.setObjectName("centralwidget")
        self.inicio = QtWidgets.QLabel(self.centralwidget)
        self.inicio.setGeometry(QtCore.QRect(50, 160, 41, 41))
        self.inicio.setObjectName("inicio")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 200, 41, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 240, 41, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 280, 41, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 320, 71, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 360, 61, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 400, 121, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 440, 101, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 70, 101, 41))
        self.label.setObjectName("label")
        self.mascota = QtWidgets.QPushButton(self.centralwidget)
        self.mascota.setGeometry(QtCore.QRect(30, 60, 71, 71))
        self.mascota.setText("")
        self.mascota.setObjectName("mascota")
        self.salvavidas = QtWidgets.QPushButton(self.centralwidget)
        self.salvavidas.setGeometry(QtCore.QRect(40, 480, 50, 50))
        self.salvavidas.setText("")
        self.salvavidas.setObjectName("salvavidas")
        Inicio.setCentralWidget(self.centralwidget)

        self.retranslateUi(Inicio)
        QtCore.QMetaObject.connectSlotsByName(Inicio)

        self.pushButton.clicked.connect(self.perfil)
        self.pushButton_3.clicked.connect(self.diario)
        self.pushButton_2.clicked.connect(self.chatbots)
        self.pushButton_4.clicked.connect(self.monitor)
        self.pushButton_5.clicked.connect(self.desafio)
        self.pushButton_6.clicked.connect(self.info)
        self.pushButton_7.clicked.connect(self.confi)

    def retranslateUi(self, Inicio):
        _translate = QtCore.QCoreApplication.translate
        Inicio.setWindowTitle(_translate("Inicio", "Inicio"))
        self.inicio.setText(_translate("Inicio", "Inicio"))
        self.pushButton.setText(_translate("Inicio", "Perfil"))
        self.pushButton_2.setText(_translate("Inicio", "Chats"))
        self.pushButton_3.setText(_translate("Inicio", "Diario"))
        self.pushButton_4.setText(_translate("Inicio", "Monitoreo"))
        self.pushButton_5.setText(_translate("Inicio", "Desafios"))
        self.pushButton_6.setText(_translate("Inicio", "Más información"))
        self.pushButton_7.setText(_translate("Inicio", "Configuración"))
        self.label.setText(_translate("Inicio", "Alvaro Sevilla"))

    def perfil(self):
        self.Perfil = QtWidgets.QMainWindow()
        self.ui = Ui_Perfil()
        self.ui.setupUi(self.Perfil)
        self.Perfil.show()

    def diario(self):
        self.Diario_1 = QtWidgets.QMainWindow()
        self.ui = Ui_Diario_1()
        self.ui.setupUi(self.Diario_1)
        self.Diario_1.show()
    
    def chatbots(self):
        self.chatbots = QtWidgets.QMainWindow()
        self.ui = Ui_chatbots()
        self.ui.setupUi(self.chatbots)
        self.chatbots.show()

    def monitor(self):
        self.monito = QtWidgets.QMainWindow()
        self.ui = Ui_monito()
        self.ui.setupUi(self.monito)
        self.monito.show()

    def desafio(self):
        self.desafios = QtWidgets.QMainWindow()
        self.ui = Ui_desafios()
        self.ui.setupUi(self.desafios)
        self.desafios.show()

    def info(self):
        self.Informacion = QtWidgets.QMainWindow()
        self.ui = Ui_Informacion()
        self.ui.setupUi(self.Informacion)
        self.Informacion.show()

    def confi(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(380, 812)
        Register.setFixedSize(380,812)
        Register.setStyleSheet("*{\n"
                               "font-family: century gothic;\n"
                               "}\n"
                               "\n"
                               "QWidget{\n"
                               "background-image: url(:/images/images/background.png);\n"
                               "}\n"
                               "\n"
                               "QFrame#rectangulo{\n"
                               "background:#EEFFF0;\n"
                               "border-radius:8px;\n"
                               "}\n"
                               "\n"
                               "QFrame#rectangulo_2{\n"
                               "background:#EEFFF0;\n"
                               "border-radius:8px;\n"
                               "}\n"
                               "\n"
                               "QFrame#rectangulo_3{\n"
                               "background:#EEFFF0;\n"
                               "border-radius:8px;\n"
                               "}\n"
                               "\n"
                               "QToolButton#icon{\n"
                               "background:#FDECA2;\n"
                               "border-radius:0px;\n"
                               "}\n"
                               "\n"
                               "QLabel{\n"
                               "font-weight:bold;\n"
                               "color:Black;\n"
                               "}\n"
                               "\n"
                               "QLabel#create{\n"
                               "font-size:18px;\n"
                               "}\n"
                               "\n"
                               "QLineEdit{\n"
                               "background:transparent;\n"
                               "border:none;\n"
                               "}\n"
                               "\n"
                               "QPushButton{\n"
                               "background:#51C55D;\n"
                               "color:white;\n"
                               "border-radius:16px;\n"
                               "}\n"
                               "\n"
                               "QPushButton:hover{\n"
                               "background:#40A04A;\n"
                               "color:white;\n"
                               "border-radius:16px;\n"
                               "font-weight:bold;\n"
                               "}")
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setObjectName("centralwidget")
        self.rectangulo = QtWidgets.QFrame(self.centralwidget)
        self.rectangulo.setGeometry(QtCore.QRect(50, 340, 281, 41))
        self.rectangulo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rectangulo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rectangulo.setObjectName("rectangulo")
        self.nombre = QtWidgets.QLineEdit(self.rectangulo)
        self.nombre.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.nombre.setMaxLength(20)
        self.nombre.setObjectName("nombre")
        self.rectangulo_2 = QtWidgets.QFrame(self.centralwidget)
        self.rectangulo_2.setGeometry(QtCore.QRect(50, 400, 281, 41))
        self.rectangulo_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rectangulo_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rectangulo_2.setObjectName("rectangulo_2")
        self.correo = QtWidgets.QLineEdit(self.rectangulo_2)
        self.correo.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.correo.setMaxLength(50)
        self.correo.setObjectName("correo")
        self.rectangulo_3 = QtWidgets.QFrame(self.centralwidget)
        self.rectangulo_3.setGeometry(QtCore.QRect(50, 460, 281, 41))
        self.rectangulo_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rectangulo_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rectangulo_3.setObjectName("rectangulo_3")
        self.contrasena = QtWidgets.QLineEdit(self.rectangulo_3)
        self.contrasena.setGeometry(QtCore.QRect(10, 10, 261, 22))
        self.contrasena.setMaxLength(18)
        self.contrasena.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasena.setObjectName("contrasena")
        self.icon = QtWidgets.QToolButton(self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(140, 90, 111, 111))
        self.icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/logotipo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon.setIcon(icon)
        self.icon.setIconSize(QtCore.QSize(111, 111))
        self.icon.setAutoExclusive(False)
        self.icon.setObjectName("icon")
        self.create = QtWidgets.QLabel(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(100, 250, 181, 21))
        self.create.setObjectName("create")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 630, 279, 50))
        self.pushButton.setObjectName("pushButton")
        Register.setCentralWidget(self.centralwidget)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

        self.pushButton.clicked.connect(self.insert_data)
        self.pushButton.clicked.connect(self.principal)

    def insert_data(self):
        conexion1 = mysql.connector.connect(host="localhost",
                                            user="root",
                                            passwd="",
                                            database="usuarios")
        cursor1 = conexion1.cursor()
        sql = "insert into registro(nombre, correo, password) values (%s,%s,%s)"
        datos = (self.nombre.text(), self.correo.text(), self.contrasena.text())
        cursor1.execute(sql, datos)
        conexion1.commit()
        conexion1.close()

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Register"))
        self.nombre.setPlaceholderText(_translate("Register", "Nombre"))
        self.correo.setPlaceholderText(_translate("Register", "Correo"))
        self.contrasena.setPlaceholderText(_translate("Register", "Contraseña"))
        self.create.setText(_translate("Register", "Créate una cuenta"))
        self.pushButton.setText(_translate("Register", "Regístrate"))

    def principal(self):
        self.Inicio = QtWidgets.QMainWindow()
        self.ui = Ui_Inicio()
        self.ui.setupUi(self.Inicio)
        self.Inicio.show()


class Ui_Chatbot(object):
    def setupUi(self, Chatbot):
        Chatbot.setObjectName("Chatbot")
        Chatbot.resize(380, 812)
        Chatbot.setFixedSize(380,812)
        Chatbot.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"\n"
"QWidget{\n"
"background-image: url(:/imagesini/imagesini/background.png);\n"
"}\n"
"\n"
"QPushButton{\n"
"background:#51C55D;\n"
"color:white;\n"
"border-radius:16px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#40A04A;\n"
"color:white;\n"
"border-radius:16px;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton#ingresa{\n"
"background:#FDECA2;\n"
"color:black;\n"
"border-radius:0px;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Chatbot)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QToolButton(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(100, 170, 181, 191))
        self.logo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/imagesini/imagesini/logotipo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo.setIcon(icon)
        self.logo.setIconSize(QtCore.QSize(200, 220))
        self.logo.setObjectName("logo")
        self.descubre = QtWidgets.QPushButton(self.centralwidget)
        self.descubre.setGeometry(QtCore.QRect(50, 630, 279, 50))
        self.descubre.setObjectName("descubre")
        self.quest = QtWidgets.QLabel(self.centralwidget)
        self.quest.setGeometry(QtCore.QRect(80, 720, 161, 21))
        self.quest.setObjectName("quest")
        self.ingresa = QtWidgets.QPushButton(self.centralwidget)
        self.ingresa.setGeometry(QtCore.QRect(240, 720, 61, 21))
        self.ingresa.setObjectName("ingresa")
        Chatbot.setCentralWidget(self.centralwidget)

        self.retranslateUi(Chatbot)
        QtCore.QMetaObject.connectSlotsByName(Chatbot)
        self.descubre.clicked.connect(self.registersc)



    def retranslateUi(self, Chatbot):
        _translate = QtCore.QCoreApplication.translate
        Chatbot.setWindowTitle(_translate("Chatbot", "Chatbot"))
        self.descubre.setText(_translate("Chatbot", "Descubre chatwith"))
        self.quest.setText(_translate("Chatbot", "¿Ya tienes una cuenta?"))
        self.ingresa.setText(_translate("Chatbot", "Ingresa"))


    def registersc(self):
        self.Register = QtWidgets.QMainWindow()
        self.ui = Ui_Register()
        self.ui.setupUi(self.Register)
        self.Register.show()


import sourceini

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Chatbot = QtWidgets.QMainWindow()
    ui = Ui_Chatbot()
    ui.setupUi(Chatbot)
    Chatbot.show()
    sys.exit(app.exec_())
