from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MergeWindow(object):
    def setupUi(self, MergeWindow):
        MergeWindow.setObjectName("MergeWindow")
        MergeWindow.setMinimumSize(QtCore.QSize(475, 475))
        MergeWindow.setMaximumSize(QtCore.QSize(475, 475))
        MergeWindow.setMouseTracking(False)
        MergeWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"panda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MergeWindow.setWindowIcon(icon)
        MergeWindow.setStyleSheet("")
        self.merge = QtWidgets.QWidget(MergeWindow)
        self.merge.setStyleSheet("background-color: #22222e;")
        self.merge.setObjectName("merge")
        self.choose_template_button = QtWidgets.QPushButton(self.merge)
        self.choose_template_button.setGeometry(QtCore.QRect(50, 80, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.choose_template_button.setFont(font)
        self.choose_template_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.choose_template_button.setStyleSheet("QPushButton {\n"
"background-color: #3f3f55;\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a62aff;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(138, 43, 255);\n"
"}")
        self.choose_template_button.setObjectName("choose_template_button")
        self.choose_text = QtWidgets.QLabel(self.merge)
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
        self.choose_data_button = QtWidgets.QPushButton(self.merge)
        self.choose_data_button.setGeometry(QtCore.QRect(50, 180, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.choose_data_button.setFont(font)
        self.choose_data_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.choose_data_button.setStyleSheet("QPushButton {\n"
"background-color: #3f3f55;\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a62aff;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(138, 43, 255);\n"
"}")
        self.choose_data_button.setObjectName("choose_data_button")
        self.switch_data_button = QtWidgets.QPushButton(self.merge)
        self.switch_data_button.setGeometry(QtCore.QRect(130, 390, 201, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.switch_data_button.setFont(font)
        self.switch_data_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.switch_data_button.setStyleSheet("QPushButton {\n"
"background-color: #3f3f55;\n"
"background-color: rgb(141, 0, 0);\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #ff0004\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #ff656f;\n"
"}")
        self.switch_data_button.setObjectName("switch_data_button")
        self.img_panda = QtWidgets.QLabel(self.merge)
        self.img_panda.setGeometry(QtCore.QRect(380, 240, 221, 161))
        self.img_panda.setText("")
        self.img_panda.setPixmap(QtGui.QPixmap("img/panda_window.jpg"))
        self.img_panda.setObjectName("img_panda")
        self.template_text = QtWidgets.QLabel(self.merge)
        self.template_text.setGeometry(QtCore.QRect(130, 140, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.template_text.setFont(font)
        self.template_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.template_text.setObjectName("template_text")
        self.data_text = QtWidgets.QLabel(self.merge)
        self.data_text.setGeometry(QtCore.QRect(110, 240, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.data_text.setFont(font)
        self.data_text.setStyleSheet("color: rgb(255, 255, 255);")
        self.data_text.setObjectName("data_text")
        self.back_button = QtWidgets.QPushButton(self.merge)
        self.back_button.setGeometry(QtCore.QRect(10, 390, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.back_button.setFont(font)
        self.back_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.back_button.setStyleSheet("QPushButton {\n"
"background-color: #77e364;\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #00ff2a\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #fdff81;\n"
"}")
        self.back_button.setObjectName("back_button")
        self.instruction_button = QtWidgets.QPushButton(self.merge)
        self.instruction_button.setGeometry(QtCore.QRect(100, 280, 281, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.instruction_button.setFont(font)
        self.instruction_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.instruction_button.setStyleSheet("QPushButton {\n"
"background-color: #3f3f55;\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #a62aff;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(138, 43, 255);\n"
"}")
        self.instruction_button.setObjectName("instruction_button")
        self.back_button.raise_()
        self.template_text.raise_()
        self.choose_text.raise_()
        self.choose_data_button.raise_()
        self.switch_data_button.raise_()
        self.choose_template_button.raise_()
        self.data_text.raise_()
        self.instruction_button.raise_()
        self.img_panda.raise_()
        MergeWindow.setCentralWidget(self.merge)

        self.retranslateUi(MergeWindow)
        QtCore.QMetaObject.connectSlotsByName(MergeWindow)

    def retranslateUi(self, MergeWindow):
        _translate = QtCore.QCoreApplication.translate
        MergeWindow.setWindowTitle(_translate("MergeWindow", "Pandas ©️Юра"))
        self.choose_template_button.setText(_translate("MergeWindow", "Выберите файл от BILLING-362"))
        self.choose_text.setText(_translate("MergeWindow", "Выберите действие"))
        self.choose_data_button.setText(_translate("MergeWindow", "Выберите файлы со всеми данными"))
        self.switch_data_button.setText(_translate("MergeWindow", "Перенести данные"))
        self.template_text.setText(_translate("MergeWindow", "Новый сформированный файл"))
        self.data_text.setText(_translate("MergeWindow", "Файлы в которые заносили показания"))
        self.back_button.setText(_translate("MergeWindow", "Назад"))
        self.instruction_button.setText(_translate("MergeWindow", "Инструкция"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MergeWindow = QtWidgets.QMainWindow()
    ui = Ui_MergeWindow()
    ui.setupUi(MergeWindow)
    MergeWindow.show()
    sys.exit(app.exec_())
