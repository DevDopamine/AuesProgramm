import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from app.logger import Logger
from app.process import MenuWindow
from app.errors import run_critical_error

logger = Logger()

app = QApplication(sys.argv)
app.setWindowIcon(QIcon(r'panda.png'))

is_open = True

if __name__ == "__main__":
    if is_open:
        logger.log_messages('Application is running')
        menu_window = MenuWindow()
        menu_window.show()
        sys.exit(app.exec_())
    
    else:
        run_critical_error()