from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReportWindow(object):
    def setupUi(self, ReportWindow):
        ReportWindow.setObjectName("ReportWindow")
        ReportWindow.setMinimumSize(QtCore.QSize(800, 550))
        ReportWindow.setMaximumSize(QtCore.QSize(800, 550))
        ReportWindow.setMouseTracking(False)
        ReportWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"panda.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ReportWindow.setWindowIcon(icon)
        ReportWindow.setStyleSheet("")
        self.report = QtWidgets.QWidget(ReportWindow)
        self.report.setStyleSheet("background-color: #22222e;")
        self.report.setObjectName("report")
        self.browse_file_button = QtWidgets.QPushButton(self.report)
        self.browse_file_button.setGeometry(QtCore.QRect(280, 40, 221, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.browse_file_button.setFont(font)
        self.browse_file_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.browse_file_button.setStyleSheet("QPushButton {\n"
"background-color: #3f3f55;\n"
"background-color: rgb(141, 0, 0);\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover {background-color: #ff0004}"
"QPushButton:pressed {\n"
"background-color: #ff656f;\n"
"\n"
"}")
        self.browse_file_button.setObjectName("browse_file_button")
        self.report_button = QtWidgets.QPushButton(self.report)
        self.report_button.setGeometry(QtCore.QRect(10, 140, 380, 60))
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
"QPushButton:hover {background-color: #a62aff}"
"QPushButton:pressed {\n"
"background-color: #7700ff;\n"
"\n"
"}")
        self.report_button.setObjectName("report_button")
        self.instruction_button = QtWidgets.QPushButton(self.report)
        self.instruction_button.setGeometry(QtCore.QRect(290, 410, 231, 60))
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
"QPushButton:hover {background-color: #a62aff}"
"QPushButton:pressed {\n"
"background-color: #7700ff;\n"
"\n"
"}")
        self.instruction_button.setObjectName("instruction_button")
        self.img_panda = QtWidgets.QLabel(self.report)
        self.img_panda.setGeometry(QtCore.QRect(20, 360, 221, 161))
        self.img_panda.setText("")
        self.img_panda.setPixmap(QtGui.QPixmap(r"panda_window.jpg"))
        self.img_panda.setObjectName("img_panda")
        self.large3500_button = QtWidgets.QPushButton(self.report)
        self.large3500_button.setGeometry(QtCore.QRect(10, 230, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.large3500_button.setFont(font)
        self.large3500_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.large3500_button.setStyleSheet("QPushButton {\n"
"background-color: #3f3f55;\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover {background-color: #a62aff}"
"QPushButton:pressed {\n"
"background-color: #7700ff;\n"
"\n"
"}")
        self.large3500_button.setObjectName("large3500_button")
        self.mistakes_button = QtWidgets.QPushButton(self.report)
        self.mistakes_button.setGeometry(QtCore.QRect(10, 320, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.mistakes_button.setFont(font)
        self.mistakes_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.mistakes_button.setStyleSheet("QPushButton {\n"
"background-color: #3f3f55;\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover {background-color: #a62aff}"
"QPushButton:pressed {\n"
"background-color: #7700ff;\n"
"\n"
"}")
        self.mistakes_button.setObjectName("mistakes_button")
        self.emty_button = QtWidgets.QPushButton(self.report)
        self.emty_button.setGeometry(QtCore.QRect(410, 140, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.emty_button.setFont(font)
        self.emty_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.emty_button.setStyleSheet("QPushButton {\n"
"background-color: #3f3f55;\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover {background-color: #a62aff}"
"QPushButton:pressed {\n"
"background-color: #7700ff;\n"
"\n"
"}")
        self.emty_button.setObjectName("emty_button")
        self.minus_button = QtWidgets.QPushButton(self.report)
        self.minus_button.setGeometry(QtCore.QRect(410, 320, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.minus_button.setFont(font)
        self.minus_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.minus_button.setStyleSheet("QPushButton {\n"
"background-color: #3f3f55;\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover {background-color: #a62aff}"
"QPushButton:pressed {\n"
"background-color: #7700ff;\n"
"\n"
"}")
        self.minus_button.setObjectName("minus_button")
        self.large1000_button = QtWidgets.QPushButton(self.report)
        self.large1000_button.setGeometry(QtCore.QRect(410, 230, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.large1000_button.setFont(font)
        self.large1000_button.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.large1000_button.setStyleSheet("QPushButton {\n"
"background-color: #3f3f55;\n"
"border: 2px solid f66867;\n"
"border-radius: 30;\n"
"color: white\n"
"}\n"
"\n"
"QPushButton:hover {background-color: #a62aff}"
"QPushButton:pressed {\n"
"background-color: #7700ff;\n"
"\n"
"}")
        self.large1000_button.setObjectName("large1000_button")
        self.back_button = QtWidgets.QPushButton(self.report)
        self.back_button.setGeometry(QtCore.QRect(160, 40, 161, 60))
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
"\n"
"QPushButton:hover {background-color: #00ff2a}"
"QPushButton:pressed {\n"
"background-color: #fdff81;\n"
"\n"
"}")
        self.back_button.setObjectName("back_button")
        self.back_button.raise_()
        self.img_panda.raise_()
        self.report_button.raise_()
        self.browse_file_button.raise_()
        self.large3500_button.raise_()
        self.mistakes_button.raise_()
        self.emty_button.raise_()
        self.minus_button.raise_()
        self.large1000_button.raise_()
        self.instruction_button.raise_()
        ReportWindow.setCentralWidget(self.report)

        self.retranslateUi(ReportWindow)
        QtCore.QMetaObject.connectSlotsByName(ReportWindow)

    def retranslateUi(self, ReportWindow):
        _translate = QtCore.QCoreApplication.translate
        ReportWindow.setWindowTitle(_translate("ReportWindow", "Pandas ©️Юра"))
        self.browse_file_button.setText(_translate("ReportWindow", "ВЫБРАТЬ ФАЙЛ"))
        self.report_button.setText(_translate("ReportWindow", "Сформировать итог для BILLING-362"))
        self.instruction_button.setText(_translate("ReportWindow", "Инструкция"))
        self.large3500_button.setText(_translate("ReportWindow", "Сформировать более 3500кВт"))
        self.mistakes_button.setText(_translate("ReportWindow", "Сформировать ошибки"))
        self.emty_button.setText(_translate("ReportWindow", "Сформировать пустые адреса"))
        self.minus_button.setText(_translate("ReportWindow", "Сформировать минусы"))
        self.large1000_button.setText(_translate("ReportWindow", "Сформировать более 1000кВт"))
        self.back_button.setText(_translate("ReportWindow", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReportWindow = QtWidgets.QMainWindow()
    ui = Ui_ReportWindow()
    ui.setupUi(ReportWindow)
    ReportWindow.show()
    sys.exit(app.exec_())
