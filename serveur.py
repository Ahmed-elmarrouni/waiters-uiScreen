# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serveur.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ServeurMainWindow(object):
    def setupUi(self, ServeurMainWindow):
        ServeurMainWindow.setObjectName("ServeurMainWindow")
        ServeurMainWindow.resize(492, 618)
        ServeurMainWindow.setStyleSheet("background-color: rgb(170, 85, 255);")
        self.centralwidget = QtWidgets.QWidget(ServeurMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.prenom = QtWidgets.QLineEdit(self.centralwidget)
        self.prenom.setGeometry(QtCore.QRect(260, 230, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.prenom.setFont(font)
        self.prenom.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.prenom.setObjectName("prenom")
        self.Delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_btn.setGeometry(QtCore.QRect(40, 470, 121, 71))
        self.Delete_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Delete_btn.setFont(font)
        self.Delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Delete_btn.setStyleSheet("#Delete_btn{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"background-color: rgb(255, 2, 14);\n"
"border: 3px Solid rgb(175, 34, 15);\n"
"}\n"
"#Delete_btn:hover:pressed{\n"
"background-color: rgb(255, 167, 43);\n"
"}\n"
"")
        self.Delete_btn.setObjectName("Delete_btn")
        self.nom = QtWidgets.QLineEdit(self.centralwidget)
        self.nom.setGeometry(QtCore.QRect(40, 230, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nom.setFont(font)
        self.nom.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.nom.setObjectName("nom")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.matricule = QtWidgets.QLineEdit(self.centralwidget)
        self.matricule.setGeometry(QtCore.QRect(40, 110, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.matricule.setFont(font)
        self.matricule.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.matricule.setText("")
        self.matricule.setObjectName("matricule")
        self.Search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(190, 470, 121, 71))
        self.Search_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Search_btn.setFont(font)
        self.Search_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Search_btn.setStyleSheet("#Search_btn{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 255, 39);\n"
"border-radius: 18px;\n"
"border: 3px Solid rgb(3, 168, 17);\n"
"}\n"
"#Search_btn:hover:pressed{\n"
"background-color: rgb(126, 255, 103);\n"
"}")
        self.Search_btn.setObjectName("Search_btn")
        self.Add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Add_btn.setGeometry(QtCore.QRect(340, 470, 121, 71))
        self.Add_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Add_btn.setFont(font)
        self.Add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Add_btn.setStyleSheet("#Add_btn{\n"
"background-color: rgb(112, 162, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"border: 3px Solid rgb(17, 21, 255);\n"
"}\n"
"#Add_btn:hover:pressed{\n"
"background-color: rgb(190, 164, 255);\n"
"}")
        self.Add_btn.setObjectName("Add_btn")
        self.tel = QtWidgets.QLineEdit(self.centralwidget)
        self.tel.setGeometry(QtCore.QRect(40, 350, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tel.setFont(font)
        self.tel.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.tel.setText("")
        self.tel.setObjectName("tel")
        ServeurMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ServeurMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 29))
        self.menubar.setObjectName("menubar")
        ServeurMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ServeurMainWindow)
        self.statusbar.setObjectName("statusbar")
        ServeurMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ServeurMainWindow)
        QtCore.QMetaObject.connectSlotsByName(ServeurMainWindow)

    def retranslateUi(self, ServeurMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ServeurMainWindow.setWindowTitle(_translate("ServeurMainWindow", "MainWindow"))
        self.prenom.setPlaceholderText(_translate("ServeurMainWindow", "Prénom"))
        self.Delete_btn.setText(_translate("ServeurMainWindow", "Delete "))
        self.nom.setPlaceholderText(_translate("ServeurMainWindow", "nom"))
        self.label_2.setText(_translate("ServeurMainWindow", "Écran Serveur"))
        self.matricule.setPlaceholderText(_translate("ServeurMainWindow", "Matricule"))
        self.Search_btn.setText(_translate("ServeurMainWindow", "Search "))
        self.Add_btn.setText(_translate("ServeurMainWindow", "Add "))
        self.tel.setPlaceholderText(_translate("ServeurMainWindow", "Tel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ServeurMainWindow = QtWidgets.QMainWindow()
    ui = Ui_ServeurMainWindow()
    ui.setupUi(ServeurMainWindow)
    ServeurMainWindow.show()
    sys.exit(app.exec_())
