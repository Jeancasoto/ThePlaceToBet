# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginAdmin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(353, 491)
        self.boton_login = QtGui.QPushButton(Dialog)
        self.boton_login.setGeometry(QtCore.QRect(130, 440, 121, 31))
        self.boton_login.setObjectName(_fromUtf8("boton_login"))
        self.username = QtGui.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(140, 320, 161, 29))
        self.username.setObjectName(_fromUtf8("username"))
        self.password = QtGui.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(142, 370, 161, 29))
        self.password.setObjectName(_fromUtf8("password"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 330, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 380, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 20, 261, 261))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setAutoFillBackground(False)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Imagenes/businessman-3.png")))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #Boton que desbloquea las opciones de admin
        self.boton_login.clicked.connect(self.button_login)
    
    #Metodo que desbloquea las opciones del admin
    def button_login(self):
        input_username = str(self.username.text())
        input_password = str(self.password.text())
        print 'username=', input_username
        if input_username == ("admin"):
            print 'Username coincide'
            if input_password == ("admin"):
                print 'password coincide'
                self.menu_crear_persona.setEnabled
                self.menu_manage_team.setEnabled
                print 'deberia haberlos desbloqueado'
            else:
                print 'No coincide password'
        else:
            print'No coincide username'

        print 'Fin del metodo'

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.boton_login.setText(_translate("Dialog", "Log In", None))
        self.label_2.setText(_translate("Dialog", "Usuario", None))
        self.label_3.setText(_translate("Dialog", "Password", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

