from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.setMinimumSize(QtCore.QSize(475, 475))
        MenuWindow.setMaximumSize(QtCore.QSize(475, 475))
        MenuWindow.setMouseTracking(False)
        MenuWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"panda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MenuWindow.setWindowIcon(icon)
        MenuWindow.setStyleSheet("")
        self.menu = QtWidgets.QWidget(MenuWindow)
        self.menu.setStyleSheet("background-color: #22222e;")
        self.menu.setObjectName("menu")
        self.merge_button = QtWidgets.QPushButton(self.menu)
        self.merge_button.setGeometry(QtCore.QRect(50, 80, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.merge_button.setFont(font)
        self.merge_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.merge_button.setStyleSheet("QPushButton {\n"
"background-color: #3f3f55;\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #8827ff;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(102, 41, 255);\n"
"\n"
"}")
        self.merge_button.setObjectName("merge_button")
        self.choose_text = QtWidgets.QLabel(self.menu)
        self.choose_text.setGeometry(QtCore.QRect(80, 20, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.choose_text.setFont(font)
        self.choose_text.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.choose_text.setStyleSheet("color: white;")
        self.choose_text.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_text.setObjectName("choose_text")
        self.report_button = QtWidgets.QPushButton(self.menu)
        self.report_button.setGeometry(QtCore.QRect(50, 200, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.report_button.setFont(font)
        self.report_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.report_button.setStyleSheet("QPushButton {\n"
"background-color: #3f3f55;\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #8827ff;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(102, 41, 255);\n"
"\n"
"}")
        self.report_button.setObjectName("report_button")
        self.instruction_button = QtWidgets.QPushButton(self.menu)
        self.instruction_button.setGeometry(QtCore.QRect(50, 390, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.instruction_button.setFont(font)
        self.instruction_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.instruction_button.setStyleSheet("QPushButton {\n"
"background-color: rgb(81, 52, 85);\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #8827ff;\n"
"\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(102, 41, 255);\n"
"\n"
"}")
        self.instruction_button.setObjectName("instruction_button")
        self.merge_text = QtWidgets.QLabel(self.menu)
        self.merge_text.setGeometry(QtCore.QRect(140, 140, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.merge_text.setFont(font)
        self.merge_text.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.merge_text.setStyleSheet("color: white;")
        self.merge_text.setAlignment(QtCore.Qt.AlignCenter)
        self.merge_text.setObjectName("merge_text")
        self.report_text = QtWidgets.QLabel(self.menu)
        self.report_text.setGeometry(QtCore.QRect(130, 260, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.report_text.setFont(font)
        self.report_text.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.report_text.setStyleSheet("color: white;")
        self.report_text.setAlignment(QtCore.Qt.AlignCenter)
        self.report_text.setObjectName("report_text")
        self.img_panda = QtWidgets.QLabel(self.menu)
        self.img_panda.setGeometry(QtCore.QRect(380, 240, 221, 161))
        self.img_panda.setText("")
        self.img_panda.setPixmap(QtGui.QPixmap(r"panda_window.jpg"))
        self.img_panda.setObjectName("img_panda")
        self.img_panda.raise_()
        self.merge_text.raise_()
        self.choose_text.raise_()
        self.report_button.raise_()
        self.instruction_button.raise_()
        self.report_text.raise_()
        self.merge_button.raise_()
        MenuWindow.setCentralWidget(self.menu)

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "Pandas ©️Юра"))
        self.merge_button.setText(_translate("MenuWindow", "Объединить таблицы"))
        self.choose_text.setText(_translate("MenuWindow", "Выберите действие"))
        self.report_button.setText(_translate("MenuWindow", "Работа над отчетом"))
        self.instruction_button.setText(_translate("MenuWindow", "Инструкция"))
        self.merge_text.setText(_translate("MenuWindow", "Перенесите данные"))
        self.report_text.setText(_translate("MenuWindow", "Сформировать отчет"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuWindow()
    ui.setupUi(MenuWindow)
    MenuWindow.show()
    sys.exit(app.exec_())
