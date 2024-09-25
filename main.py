import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox
from process import MenuWindow

app = QApplication(sys.argv)
app.setWindowIcon(QIcon('img\panda.png'))

is_open = True

if is_open:
    if __name__ == "__main__":
        menu_window = MenuWindow()
        menu_window.show()
        sys.exit(app.exec_())
else:
    QMessageBox.critical(None, 'Ошибка использования', 'Приложение не доступно!')