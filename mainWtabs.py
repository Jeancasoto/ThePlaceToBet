# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWtabs.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 636)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Log_in_admin = QtGui.QTabWidget(self.centralwidget)
        self.Log_in_admin.setGeometry(QtCore.QRect(10, 10, 781, 601))
        self.Log_in_admin.setDocumentMode(False)
        self.Log_in_admin.setTabsClosable(False)
        self.Log_in_admin.setObjectName(_fromUtf8("Log_in_admin"))
        self.widget = QtGui.QWidget()
        self.widget.setObjectName(_fromUtf8("widget"))
        self.boton_login = QtGui.QPushButton(self.widget)
        self.boton_login.setGeometry(QtCore.QRect(338, 440, 121, 31))
        self.boton_login.setObjectName(_fromUtf8("boton_login"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(258, 330, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(258, 380, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(258, 20, 261, 261))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setAutoFillBackground(False)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("Imagenes/businessman-3.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.username = QtGui.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(348, 320, 161, 29))
        self.username.setObjectName(_fromUtf8("username"))
        self.password = QtGui.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(350, 370, 161, 29))
        self.password.setObjectName(_fromUtf8("password"))
        self.Log_in_admin.addTab(self.widget, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.numero_dentidad = QtGui.QLineEdit(self.tab_5)
        self.numero_dentidad.setGeometry(QtCore.QRect(320, 150, 171, 29))
        self.numero_dentidad.setObjectName(_fromUtf8("numero_dentidad"))
        self.label_10 = QtGui.QLabel(self.tab_5)
        self.label_10.setGeometry(QtCore.QRect(120, 100, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.fecha_nacimiento = QtGui.QDateEdit(self.tab_5)
        self.fecha_nacimiento.setGeometry(QtCore.QRect(320, 200, 151, 29))
        self.fecha_nacimiento.setObjectName(_fromUtf8("fecha_nacimiento"))
        self.primer_apellido = QtGui.QLineEdit(self.tab_5)
        self.primer_apellido.setGeometry(QtCore.QRect(320, 300, 161, 29))
        self.primer_apellido.setObjectName(_fromUtf8("primer_apellido"))
        self.label_4 = QtGui.QLabel(self.tab_5)
        self.label_4.setGeometry(QtCore.QRect(120, 150, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.combo_box_desempeno = QtGui.QComboBox(self.tab_5)
        self.combo_box_desempeno.setGeometry(QtCore.QRect(320, 100, 251, 27))
        self.combo_box_desempeno.setEditable(False)
        self.combo_box_desempeno.setModelColumn(0)
        self.combo_box_desempeno.setObjectName(_fromUtf8("combo_box_desempeno"))
        self.combo_box_desempeno.addItem(_fromUtf8(""))
        self.combo_box_desempeno.addItem(_fromUtf8(""))
        self.combo_box_desempeno.addItem(_fromUtf8(""))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.tab_5)
        self.doubleSpinBox.setGeometry(QtCore.QRect(320, 350, 161, 29))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label_5 = QtGui.QLabel(self.tab_5)
        self.label_5.setGeometry(QtCore.QRect(120, 200, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.boton_confirmar = QtGui.QPushButton(self.tab_5)
        self.boton_confirmar.setGeometry(QtCore.QRect(570, 420, 85, 27))
        self.boton_confirmar.setObjectName(_fromUtf8("boton_confirmar"))
        self.label_11 = QtGui.QLabel(self.tab_5)
        self.label_11.setGeometry(QtCore.QRect(120, 350, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_6 = QtGui.QLabel(self.tab_5)
        self.label_6.setGeometry(QtCore.QRect(120, 300, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(120, 300, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_7 = QtGui.QLabel(self.tab_5)
        self.label_7.setGeometry(QtCore.QRect(120, 250, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSerif"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.primer_nombre = QtGui.QLineEdit(self.tab_5)
        self.primer_nombre.setGeometry(QtCore.QRect(320, 250, 161, 29))
        self.primer_nombre.setObjectName(_fromUtf8("primer_nombre"))
        self.boton_cancelar = QtGui.QPushButton(self.tab_5)
        self.boton_cancelar.setGeometry(QtCore.QRect(470, 420, 85, 27))
        self.boton_cancelar.setObjectName(_fromUtf8("boton_cancelar"))
        self.Log_in_admin.addTab(self.tab_5, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.botonCancelar = QtGui.QPushButton(self.tab_2)
        self.botonCancelar.setGeometry(QtCore.QRect(450, 510, 97, 29))
        self.botonCancelar.setObjectName(_fromUtf8("botonCancelar"))
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(260, 10, 241, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.botonEliminarEquipo = QtGui.QPushButton(self.tab_2)
        self.botonEliminarEquipo.setGeometry(QtCore.QRect(320, 310, 91, 29))
        self.botonEliminarEquipo.setObjectName(_fromUtf8("botonEliminarEquipo"))
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(480, 110, 151, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.botonAceptar = QtGui.QPushButton(self.tab_2)
        self.botonAceptar.setGeometry(QtCore.QRect(580, 510, 97, 29))
        self.botonAceptar.setObjectName(_fromUtf8("botonAceptar"))
        self.listaEquiposSel = QtGui.QListView(self.tab_2)
        self.listaEquiposSel.setGeometry(QtCore.QRect(420, 130, 271, 361))
        self.listaEquiposSel.setObjectName(_fromUtf8("listaEquiposSel"))
        self.listaEquiposDisp = QtGui.QListView(self.tab_2)
        self.listaEquiposDisp.setGeometry(QtCore.QRect(40, 130, 271, 361))
        self.listaEquiposDisp.setObjectName(_fromUtf8("listaEquiposDisp"))
        self.botonAgregarEquipo = QtGui.QPushButton(self.tab_2)
        self.botonAgregarEquipo.setGeometry(QtCore.QRect(320, 260, 91, 29))
        self.botonAgregarEquipo.setObjectName(_fromUtf8("botonAgregarEquipo"))
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(100, 110, 141, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.textNomClub = QtGui.QLineEdit(self.tab_2)
        self.textNomClub.setGeometry(QtCore.QRect(110, 50, 511, 29))
        self.textNomClub.setObjectName(_fromUtf8("textNomClub"))
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(50, 60, 61, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.Log_in_admin.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_15 = QtGui.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(210, 10, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setGeometry(QtCore.QRect(120, 70, 71, 17))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.tablaJugLocal = QtGui.QTableWidget(self.tab)
        self.tablaJugLocal.setGeometry(QtCore.QRect(405, 90, 341, 351))
        self.tablaJugLocal.setObjectName(_fromUtf8("tablaJugLocal"))
        self.tablaJugLocal.setColumnCount(4)
        self.tablaJugLocal.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaJugLocal.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaJugLocal.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaJugLocal.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaJugLocal.setHorizontalHeaderItem(3, item)
        self.tablaJugVis = QtGui.QTableWidget(self.tab)
        self.tablaJugVis.setGeometry(QtCore.QRect(40, 90, 341, 351))
        self.tablaJugVis.setColumnCount(4)
        self.tablaJugVis.setObjectName(_fromUtf8("tablaJugVis"))
        self.tablaJugVis.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaJugVis.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaJugVis.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaJugVis.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaJugVis.setHorizontalHeaderItem(3, item)
        self.labelPromBRLocal = QtGui.QLabel(self.tab)
        self.labelPromBRLocal.setGeometry(QtCore.QRect(690, 460, 64, 17))
        self.labelPromBRLocal.setText(_fromUtf8(""))
        self.labelPromBRLocal.setObjectName(_fromUtf8("labelPromBRLocal"))
        self.label_17 = QtGui.QLabel(self.tab)
        self.label_17.setGeometry(QtCore.QRect(500, 460, 141, 17))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.botonAceptar_2 = QtGui.QPushButton(self.tab)
        self.botonAceptar_2.setGeometry(QtCore.QRect(650, 530, 97, 29))
        self.botonAceptar_2.setObjectName(_fromUtf8("botonAceptar_2"))
        self.label_18 = QtGui.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(40, 460, 141, 17))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.botonCancelar_2 = QtGui.QPushButton(self.tab)
        self.botonCancelar_2.setGeometry(QtCore.QRect(530, 530, 97, 29))
        self.botonCancelar_2.setObjectName(_fromUtf8("botonCancelar_2"))
        self.labelPromBRVis = QtGui.QLabel(self.tab)
        self.labelPromBRVis.setGeometry(QtCore.QRect(230, 460, 64, 17))
        self.labelPromBRVis.setText(_fromUtf8(""))
        self.labelPromBRVis.setObjectName(_fromUtf8("labelPromBRVis"))
        self.label_19 = QtGui.QLabel(self.tab)
        self.label_19.setGeometry(QtCore.QRect(570, 70, 41, 17))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.Log_in_admin.addTab(self.tab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Log_in_admin.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.boton_login.setText(_translate("MainWindow", "Log In", None))
        self.label_2.setText(_translate("MainWindow", "Usuario", None))
        self.label_3.setText(_translate("MainWindow", "Password", None))
        self.Log_in_admin.setTabText(self.Log_in_admin.indexOf(self.widget), _translate("MainWindow", "Administrador", None))
        self.label_10.setText(_translate("MainWindow", "Se desempenara como ::", None))
        self.fecha_nacimiento.setDisplayFormat(_translate("MainWindow", "dd/mm/yyyy", None))
        self.label_4.setText(_translate("MainWindow", "Numero de identidad ", None))
        self.combo_box_desempeno.setItemText(0, _translate("MainWindow", "Arbitro", None))
        self.combo_box_desempeno.setItemText(1, _translate("MainWindow", "Jugador", None))
        self.combo_box_desempeno.setItemText(2, _translate("MainWindow", "Entrenador", None))
        self.label_5.setText(_translate("MainWindow", "Fecha de nacimiento ", None))
        self.boton_confirmar.setText(_translate("MainWindow", "Confirmar", None))
        self.label_11.setText(_translate("MainWindow", "Peso", None))
        self.label_8.setText(_translate("MainWindow", "Primer Apellido", None))
        self.label_7.setText(_translate("MainWindow", "Primer Nombre", None))
        self.boton_cancelar.setText(_translate("MainWindow", "Cancelar", None))
        self.Log_in_admin.setTabText(self.Log_in_admin.indexOf(self.tab_5), _translate("MainWindow", "Crear persona", None))
        self.botonCancelar.setText(_translate("MainWindow", "Cancelar", None))
        self.label_9.setText(_translate("MainWindow", "Nuevo Club Deportivo", None))
        self.botonEliminarEquipo.setText(_translate("MainWindow", "<-Eliminar", None))
        self.label_12.setText(_translate("MainWindow", "Equipos Seleccionados", None))
        self.botonAceptar.setText(_translate("MainWindow", "Aceptar", None))
        self.botonAgregarEquipo.setText(_translate("MainWindow", "Agegar ->", None))
        self.label_13.setText(_translate("MainWindow", "Equipos Disponibles", None))
        self.label_14.setText(_translate("MainWindow", "Nombre:", None))
        self.Log_in_admin.setTabText(self.Log_in_admin.indexOf(self.tab_2), _translate("MainWindow", "Crear equipo", None))
        self.label_15.setText(_translate("MainWindow", "Jugadores en el Partido", None))
        self.label_16.setText(_translate("MainWindow", "Visitante", None))
        item = self.tablaJugLocal.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre", None))
        item = self.tablaJugLocal.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Peso", None))
        item = self.tablaJugLocal.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Bioritmo", None))
        item = self.tablaJugLocal.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Posicion", None))
        item = self.tablaJugVis.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre", None))
        item = self.tablaJugVis.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Peso", None))
        item = self.tablaJugVis.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Bioritmo", None))
        item = self.tablaJugVis.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Posicion", None))
        self.label_17.setText(_translate("MainWindow", "Promedio Bioritmos:", None))
        self.botonAceptar_2.setText(_translate("MainWindow", "Aceptar", None))
        self.label_18.setText(_translate("MainWindow", "Promedio Bioritmos:", None))
        self.botonCancelar_2.setText(_translate("MainWindow", "Cancelar", None))
        self.label_19.setText(_translate("MainWindow", "Local", None))
        self.Log_in_admin.setTabText(self.Log_in_admin.indexOf(self.tab), _translate("MainWindow", "Pre-Partido", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
