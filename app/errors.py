from PyQt5.QtWidgets import QMessageBox

def run_critical_error():
    return QMessageBox.critical(None, 'Ошибка использования', 'Приложение не доступно!')

def instruction_not_found():
    return QMessageBox.critical(None, 'Ошибка', 'Инструкция отсутствует, или была удалена!')