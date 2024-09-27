import os
from PyQt5.QtCore import QThread, pyqtSignal, QDir
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QMainWindow
import pandas as pd
from datetime import datetime
from UI.merge import Ui_MergeWindow
from UI.report import Ui_ReportWindow
from UI.menu import Ui_MenuWindow
from app.errors import instruction_not_found
from app.logger import Logger

logger = Logger()

class WorkerThread(QThread):
    finished = pyqtSignal()
    error = pyqtSignal(str, str)
    warning = pyqtSignal(str, str)

    def __init__(self, target_function):
        super().__init__()
        self.target_function = target_function
        logger.log_messages(f'WorkerThread initialized with function: {self.target_function.__name__}')

    def run(self):
        logger.log_messages(f'WorkerThread started: {self.target_function.__name__}')
        try:
            if self.target_function():
                self.finished.emit()
                logger.log_messages(f'WorkerThread finished successfully: {self.target_function.__name__}')
        except Exception as e:
            self.error.emit('Ошибка', 'Произошла неизвестная ошибка')
            logger.log_messages(f'An unknown error occurred: {e}', level='error')

class MenuWindow(QMainWindow, Ui_MenuWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.report_window = None
        self.merge_window = None

        self.report_button.clicked.connect(self.open_report_window)
        self.merge_button.clicked.connect(self.open_merge_window)
        self.instruction_button.clicked.connect(self.open_instruction_file)
        logger.log_messages('MenuWindow initialized and UI set up.')

    def open_report_window(self):
        logger.log_messages('Opening ReportWindow.')
        self.report_window = ReportWindow(self)
        self.hide()
        self.report_window.show()

    def open_merge_window(self):
        logger.log_messages('Opening MergeWindow.')
        self.merge_window = MergeWindow(self)
        self.hide()
        self.merge_window.show()

    def open_instruction_file(self):
        logger.log_messages('Attempting to open instruction file.')
        try:
            os.startfile(r'manual.docx')
            logger.log_messages('Instruction file opened successfully.')
        except Exception as e:
            instruction_not_found()
            logger.log_messages(f'Failed to open instruction file: {e}', level='error')

class Processing(QWidget):
    def __init__(self, browse_file_path=None, browse_template_path=None, browse_data_paths=[]):
        super().__init__()
        self.browse_file_path = browse_file_path
        self.browse_template_path = browse_template_path
        self.browse_data_paths = browse_data_paths
        self.worker_thread = None
        logger.log_messages('Processing initialized.')

    def start_thread(self, target_function):
        logger.log_messages(f'Starting thread for function: {target_function.__name__}')
        self.worker_thread = WorkerThread(target_function)
        self.worker_thread.finished.connect(self.thread_finished)
        self.worker_thread.error.connect(self.thread_error)
        self.worker_thread.warning.connect(self.thread_warning)
        self.worker_thread.start()

    def thread_warning(self, title: str = 'Предупреждение', text: str = 'Неизвестное предупреждение'):
        logger.log_messages(f'{title}: {text}', level='warning')
        QMessageBox.warning(self, title, text)

    def thread_finished(self, title: str = 'Успешно!', text: str = 'Операция завершена!'):
        logger.log_messages(f'{title}: {text}')
        QMessageBox.information(self, title, text)

    def thread_error(self, title: str = 'Сбой программы', text: str = "Возможно структура файла(ов) составлена неправильно!"):
        logger.log_messages(f'{title}: {text}', level='error')
        QMessageBox.critical(self, title, text)

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ВЫБОР ФАЙЛА >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    

    def browse_file(self):
        dialog = QFileDialog()
        desktop_path = QDir.homePath() + "/Desktop"
        dialog.setDirectory(desktop_path)
        self.browse_file_path, _ = dialog.getOpenFileName(None, "Выберите файл", "", "Excel Files (*.xlsx *.xls)")
        if self.browse_file_path:
            logger.log_messages(f'File selected: {self.browse_file_path}')
            return self.browse_file_path
        else:
            logger.log_messages('No file selected.', level='warning')
            self.thread_warning(text='Вы не выбрали файл')

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ----------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Более 1000кВт >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def process_large1000(self):
        if self.browse_file_path:
            self.start_thread(self._process_large1000)
        else:
            logger.log_messages('No file selected before request!', level='warning')
            self.thread_warning(text='Выберите файл перед запросом!')

    def _process_large1000(self):
        try:
            dialog = QFileDialog()
            desktop_path = QDir.homePath() + "/Desktop"
            dialog.setDirectory(desktop_path)
            result_path , _ = dialog.getSaveFileName(None, 'Сохраните файл', '', 'Excel files (*.xlsx *.xls)')
            if not result_path:
                logger.log_messages('Save operation canceled!', level='warning')
                return self.worker_thread.warning.emit('Внимание', 'Сохранение отменено!')
            df = pd.read_excel(self.browse_file_path, header=0).copy()
            df['НАЧАЛЬНЫЕ'] = pd.to_numeric(df['НАЧАЛЬНЫЕ'], errors='coerce')
            df['КОНЕЧНЫЕ'] = pd.to_numeric(df['КОНЕЧНЫЕ'], errors='coerce')
            df['РАЗНИЦА'] = df['КОНЕЧНЫЕ'] - df['НАЧАЛЬНЫЕ']
            df = df[df['РАЗНИЦА'] >= 1000]
            df.to_excel(result_path, index=False)
            logger.log_messages(f'File saved at: {result_path}')
            return True
        except Exception as e:
            logger.log_messages(f'Error reading file: {e}', level='error')
            self.worker_thread.error.emit('Ошибка при чтении файла', f'Произошла ошибка при чтении файла.\nОшибка {e}')

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< --------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< БОЛЕЕ 3500 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def process_large3500(self):
        if self.browse_file_path:
            self.start_thread(self._process_large3500)
        else:
            logger.log_messages('No file selected before request!', level='warning')
            self.thread_warning(text='Выберите файл перед запросом!')

    def _process_large3500(self):
        try:  
            dialog = QFileDialog()
            desktop_path = QDir.homePath() + "/Desktop"
            dialog.setDirectory(desktop_path)
            result_path , _ = dialog.getSaveFileName(None, 'Сохраните файл', '', 'Excel files (*.xlsx *.xls)')
            if not result_path:
                logger.log_messages('Save operation canceled!', level='warning')
                return self.worker_thread.warning.emit('Внимание', 'Сохранение отменено!')
            df = pd.read_excel(self.browse_file_path, header=0).copy()
            df['КОНЕЧНЫЕ'] = pd.to_numeric(df["КОНЕЧНЫЕ"], errors='coerce')
            df['НАЧАЛЬНЫЕ'] = pd.to_numeric(df["НАЧАЛЬНЫЕ"], errors='coerce')
            df['РАЗНИЦА'] = df['КОНЕЧНЫЕ'] - df['НАЧАЛЬНЫЕ']
            df = df[df['РАЗНИЦА'] >= 3500]
            df.to_excel(result_path, index=False)
            logger.log_messages(f'File saved at: {result_path}')
            return True
        except Exception as e:
            logger.log_messages(f'Error reading file: {e}', level='error')
            self.worker_thread.error.emit('Ошибка при чтении файла', f'Произошла ошибка при чтении файла.\nОшибка {e}')

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ---------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ОШИБКИ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def process_mistakes(self):
        if self.browse_file_path:
            self.start_thread(self._process_mistakes)
        else:
            logger.log_messages('No file selected before request!', level='warning')
            self.thread_warning(text='Выберите файл перед запросом!')

    def _process_mistakes(self):
        try:
            dialog = QFileDialog()
            desktop_path = QDir.homePath() + "/Desktop"
            dialog.setDirectory(desktop_path)
            result_path , _ = dialog.getSaveFileName(None, 'Сохраните файл', '', 'Excel files (*.xlsx *.xls)')
            if not result_path:
                logger.log_messages('Save operation canceled!', level='warning')
                return self.worker_thread.warning.emit('Внимание', 'Сохранение отменено!')
            df = pd.read_excel(self.browse_file_path).copy()
            df = df[df.duplicated(subset='ЛС', keep=False)]
            df.to_excel(result_path, index=False)
            logger.log_messages(f'Error file saved at: {result_path}')
            return True
        except Exception as e:
            logger.log_messages(f'Error reading file: {e}', level='error')
            self.worker_thread.error.emit('Ошибка при чтении файла', f'Произошла ошибка при чтении файла.\nОшибка {e}')

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< --------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ПУСТЫЕ АДРЕСа >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def process_empty(self):
        if self.browse_file_path:
            self.start_thread(self._process_empty)
        else:
            logger.log_messages('No file selected before request!', level='warning')
            self.thread_warning(text='Выберите файл перед запросом!')

    def _process_empty(self):
        try: 
            dialog = QFileDialog()
            desktop_path = QDir.homePath() + "/Desktop"
            dialog.setDirectory(desktop_path)
            result_path , _ = dialog.getSaveFileName(None, 'Сохраните файл', '', 'Excel files (*.xlsx *.xls)')
            if not result_path:
                logger.log_messages('Save operation canceled!', level='warning')
                return self.worker_thread.warning.emit('Внимание', 'Сохранение отменено!')
            df = pd.read_excel(self.browse_file_path, header=0).copy()
            df = df[df['КОНЕЧНЫЕ'].isna()]
            df.to_excel(result_path, index=False)
            logger.log_messages(f'Empty addresses file saved at: {result_path}')
            return True
        except Exception as e:
            logger.log_messages(f'Error reading file: {e}', level='error')
            self.worker_thread.error.emit('Ошибка при чтении файла', f'Произошла ошибка при чтении файла.\nОшибка {e}')

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< --------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< МИНУСЫ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def process_negative(self):
        if self.browse_file_path:
            self.start_thread(self._process_negative)
        else:
            logger.log_messages('No file selected before request!', level='warning')
            self.thread_warning(text='Выберите файл перед запросом!')

    def _process_negative(self):
        try:
            dialog = QFileDialog()
            desktop_path = QDir.homePath() + "/Desktop"
            dialog.setDirectory(desktop_path)
            result_path , _ = dialog.getSaveFileName(None, 'Сохраните файл', '', 'Excel files (*.xlsx *.xls)')
            if not result_path:
                logger.log_messages('Save operation canceled!', level='warning')
                return self.worker_thread.warning.emit('Внимание', 'Сохранение отменено!')
            df = pd.read_excel(self.browse_file_path, header=0).copy()
            df['КОНЕЧНЫЕ'] = pd.to_numeric(df["КОНЕЧНЫЕ"], errors='coerce')
            df['НАЧАЛЬНЫЕ'] = pd.to_numeric(df["НАЧАЛЬНЫЕ"], errors='coerce')
            df['РАЗНИЦА'] = df['КОНЕЧНЫЕ'] - df['НАЧАЛЬНЫЕ']
            df = df[df['РАЗНИЦА'] < 0]
            df.to_excel(result_path, index=False)
            logger.log_messages(f'Negative values file saved at: {result_path}')
            return True
        except Exception as e:
            logger.log_messages(f'Error reading file: {e}', level='error')
            self.worker_thread.error.emit('Ошибка при чтении файла', f'Произошла ошибка при чтении файла.\nОшибка {e}')

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< --------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ОТЧЕТ для BILLING >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def process_report(self):
        if self.browse_file_path:
            self.start_thread(self._process_report)
        else:
            logger.log_messages('No file selected before request!', level='warning')
            self.thread_warning(text='Выберите файл перед запросом!')

    def _process_report(self):
        try:
            dialog = QFileDialog()
            desktop_path = QDir.homePath() + "/Desktop"
            dialog.setDirectory(desktop_path)
            result_path , _ = dialog.getSaveFileName(None, 'Сохраните файл', '', 'Excel files (*.xlsx *.xls)')
            if not result_path:
                logger.log_messages('Save operation canceled!', level='warning')
                return self.worker_thread.warning.emit('Внимание', 'Сохранение отменено!')
            df = pd.read_excel(self.browse_file_path, header=0).copy()
            df['КОНЕЧНЫЕ'] = pd.to_numeric(df["КОНЕЧНЫЕ"], errors='coerce')
            df['НАЧАЛЬНЫЕ'] = pd.to_numeric(df["НАЧАЛЬНЫЕ"], errors='coerce')
            df['РАЗНИЦА'] = df['КОНЕЧНЫЕ'] - df['НАЧАЛЬНЫЕ']
            df = df[~df.duplicated(subset='ЛС', keep=False)]
            df.dropna(subset=['КОНЕЧНЫЕ'], inplace=True)
            df = df[(df['РАЗНИЦА'] >= 0) & (df['РАЗНИЦА'] < 3500)]
            if df['ДАТА'].isna().any():
                date_today= datetime.now().strftime("%d.%m.%Y")
                df.loc[df['ДАТА'].isna(), 'ДАТА'] = date_today
                logger.log_messages(f'Found addresses without date! Set to current date {date_today}', level='warning')
                self.worker_thread.warning.emit('Внимание', f'Найдены адреса без даты!\nУстановлена текущая {date_today}')
            else:
                df['ДАТА'] = df['ДАТА'].dt.strftime("%d.%m.%Y")
            df.to_excel(result_path, index=False)
            logger.log_messages(f'Report saved at: {result_path}')
            return True
        except Exception as e:
            logger.log_messages(f'Error reading file: {e}', level='error')
            self.worker_thread.error.emit('Ошибка при чтении файла', f'Произошла ошибка при чтении файла.\nОшибка {e}')

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< --------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ВЫБОР ФАЙЛА BILLING >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def browse_template_file(self):
        dialog = QFileDialog()
        desktop_path = QDir.homePath() + "/Desktop"
        dialog.setDirectory(desktop_path)
        self.browse_template_path, _ = dialog.getOpenFileName(None, "Выберите файл", "", "Excel Files (*.xlsx *.xls)")
        if self.browse_template_path:
            logger.log_messages(f'Template selected: {self.browse_template_path}')
            return self.browse_template_path
        else:
            logger.log_messages('No template selected.', level='warning')
            self.thread_warning(text='Вы не выбрали файл')

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< --------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ВЫБОР ФАЙЛА С ДАННЫМИ>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def browse_data_files(self):
        self.browse_data_paths, _ = QFileDialog.getOpenFileNames(None, "Выберите файлы", "", "Excel Files (*.xlsx *.xls)")
        if self.browse_data_paths:
            logger.log_messages(f'Data files selected: {self.browse_data_paths}')
            return self.browse_data_paths
        else:
            logger.log_messages('No data files selected.', level='warning')
            self.thread_warning(text='Вы не выбрали файлы')

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< --------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< РАЗНИЦА для ПЕРЕНОСА ДАННЫХ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def calculate_difference(self, row):
        start_value = row['НАЧАЛЬНЫЕ']
        final_value = row['КОНЕЧНЫЕ']

        if pd.notnull(start_value) and pd.notnull(final_value):
            try:
                start_numeric = pd.to_numeric(start_value, errors='coerce')
                final_numeric = pd.to_numeric(final_value, errors='coerce')
                difference = final_numeric - start_numeric
                return difference
            except Exception as e:
                logger.log_messages(f'Error calculating difference: {e}', level='error')
                return pd.NaT

        return pd.NaT

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< --------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< ПЕРЕНОС ВСЕХ ДАННЫХ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def process_switching_data(self):
        if self.browse_template_path and self.browse_data_paths:
            self.start_thread(self._process_switching_data)
        else:
            logger.log_messages('Select Template and data files before requesting!', level='warning')
            self.thread_warning(text='Выберите Шаблон и файлы с данными перед запросом!')

    def _process_switching_data(self):
        result_path, _ = QFileDialog.getSaveFileName(None, 'Сохраните файл', '', 'Excel files (*.xlsx *.xls)')
        if not result_path:
            logger.log_messages('Save operation canceled!', level='warning')
            return self.worker_thread.warning.emit('Внимание', 'Сохранение отменено!')

        template_df = pd.read_excel(self.browse_template_path)
        data_dfs = [pd.read_excel(data_path) for data_path in self.browse_data_paths]

        try:
            result_df = template_df.copy()
            result_df['ДАТА'] = ""
            logger.log_messages('Data switching started.')

            n = 0
            for data_df in data_dfs:
                FILE_PROCESSING_NOW = os.path.basename(self.browse_data_paths[n])
                PROCESSING_FROM_FILE = os.path.basename(self.browse_template_path)
                logger.log_messages(f'Processing file {FILE_PROCESSING_NOW}')
                n += 1
                for index, row in data_df.iterrows():
                    template_index = result_df.index[result_df['ЛС'] == row['ЛС']]
                    if not template_index.empty:
                        template_index = template_index[0]
                        if not pd.isna(row['КОНЕЧНЫЕ']):
                            current_value = pd.to_numeric(result_df.loc[template_index, 'КОНЕЧНЫЕ'], errors='coerce')
                            new_value = pd.to_numeric(row['КОНЕЧНЫЕ'], errors='coerce')
                            if pd.isna(current_value) or new_value > current_value:
                                result_df.loc[template_index, 'КОНЕЧНЫЕ'] = new_value
                                try:
                                    result_df.loc[template_index, 'ДАТА'] = row['ДАТА'].strftime("%d.%m.%Y")
                                except:
                                    pass
            result_df['РАЗНИЦА'] = result_df.apply(self.calculate_difference, axis=1)
            result_df.to_excel(result_path, index=False)
            logger.log_messages(f'Data switched and saved at: {result_path}')
            return True
        except Exception as e:
            error_message_ru = (f'Ошибка чтения файла: "{FILE_PROCESSING_NOW}".\n'
                                f'Приблизительно ошибка в {e}.\n'
                                'Убедитесь, что ЛС, НАЧАЛЬНЫЕ, КОНЕЧНЫЕ, РАЗНИЦА, ДАТА находятся в строке №1.\n'
                                f'Возможно, ошибка в файле: {os.path.basename(PROCESSING_FROM_FILE)}')
            logger.log_messages(error_message_ru, level='error')
            self.worker_thread.error.emit('Ошибка чтения файла', error_message_ru)

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< --------------- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class MergeWindow(QMainWindow, Ui_MergeWindow, Processing):
    def __init__(self, menu_window):
        super().__init__()
        self.setupUi(self)
        self.processing = Processing()
        self.menu_window = menu_window

        self.back_button.clicked.connect(self.process_back)
        self.instruction_button.clicked.connect(self.open_instruction_file)
        self.choose_template_button.clicked.connect(self.processing.browse_template_file)
        self.choose_data_button.clicked.connect(self.processing.browse_data_files)
        self.switch_data_button.clicked.connect(self.processing.process_switching_data)
        logger.log_messages('MergeWindow initialized and UI set up.')

    def process_back(self):
        logger.log_messages('Returning to MenuWindow.')
        self.close()
        self.menu_window.show()

    def open_instruction_file(self):
        logger.log_messages('Attempting to open instruction file from MergeWindow.')
        try:
            os.startfile(r'manual.docx')
            logger.log_messages('Instruction file opened successfully from MergeWindow.')
        except Exception as e:
            instruction_not_found()
            logger.log_messages(f'Failed to open instruction file from MergeWindow: {e}', level='error')

class ReportWindow(QMainWindow, Ui_ReportWindow, Processing):
    def __init__(self, menu_window):
        super().__init__()
        self.setupUi(self)
        self.processing = Processing()
        self.menu_window = menu_window

        self.browse_file_button.clicked.connect(self.processing.browse_file)
        self.large3500_button.clicked.connect(self.processing.process_large3500)
        self.back_button.clicked.connect(self.process_back)
        self.mistakes_button.clicked.connect(self.processing.process_mistakes)
        self.large1000_button.clicked.connect(self.processing.process_large1000)
        self.emty_button.clicked.connect(self.processing.process_empty)
        self.minus_button.clicked.connect(self.processing.process_negative)
        self.report_button.clicked.connect(self.processing.process_report)
        self.instruction_button.clicked.connect(self.open_instruction_file)
        logger.log_messages('ReportWindow initialized and UI set up.')

    def process_back(self):
        logger.log_messages('Returning to MenuWindow from ReportWindow.')
        self.close()
        self.menu_window.show()

    def open_instruction_file(self):
        logger.log_messages('Attempting to open instruction file from ReportWindow.')
        try:
            os.startfile(r'manual.docx')
            logger.log_messages('Instruction file opened successfully from ReportWindow.')
        except Exception as e:
            instruction_not_found()
            logger.log_messages(f'Failed to open instruction file from ReportWindow: {e}', level='error')
