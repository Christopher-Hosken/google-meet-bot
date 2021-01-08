import sys
import threading
import platform
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import *
from gui.google_meet_bot_ui import *
import read, listen
from login import login_google, login_meet
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class Worker(QObject):
    finished = QtCore.Signal()

    def run(self, window):
        print("run!")
        opt = Options()
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.notifications" : 1})
        browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)
        try:
            login_google(browser, window.ui.input_email.text(), window.ui.input_password.text())
            login_meet(browser, window.ui.input_code.text())
        except Exception as e:
            print(e)
        while window.running:
            try:
                if (not window.enable_call):
                    window.text_input, window.text_output = listen.run(browser)
                if (not window.enable_chat):
                    window.text_input, window.text_output, window.user = read.run(browser)
                else:
                    pass
                window.update_data()
            except Exception as e:
                print(e)
                window.running = False
                self.finished.emit()
        self.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' + platform.release())

        self.enable_chat = True
        self.enable_call = True

        self.email = self.ui.input_email.text()
        self.password = self.ui.input_password.text()
        self.code = self.ui.input_code.text()

        self.text_input = None
        self.text_output = None
        self.call_input = None
        self.call_output = None
        self.user = None
        self.running = False

        self.confidence = None
        self.group = None
        self.category = None

        self.thread = None

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        self.ui.frame_top.mouseMoveEvent = self.moveWindow

        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.btn_maximize_restore.clicked.connect(self.resize(780, 610))
        self.ui.btn_close.clicked.connect(sys.exit)

        self.ui.btn_chat.clicked.connect(self.toggle_chat)
    
        self.ui.btn_call.clicked.connect(self.toggle_call)

        self.ui.btn_run.clicked.connect(self.run)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

    def moveWindow(self, event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

    def toggle_chat(self):
        self.enable_chat = not self.enable_chat
        if (self.enable_chat):
            self.ui.btn_chat.setStyleSheet(
            u"QPushButton {\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n")
        else:
            self.ui.btn_chat.setStyleSheet(
            u"QPushButton {\n"
            "	border: 2px solid rgb(32, 36, 44);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(32, 36, 44);\n"
            "}\n")

    def toggle_call(self):
        self.enable_call = not self.enable_call
        if (self.enable_call):
            self.ui.btn_call.setStyleSheet(
            u"QPushButton {\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n")

        else:
            self.ui.btn_call.setStyleSheet(
            u"QPushButton {\n"
            "	border: 2px solid rgb(32, 36, 44);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(32, 36, 44);\n"
            "}\n")

    def update_data(self):
        self.ui.label_call_input.setText(self.call_input)
        self.ui.label_call_output.setText(self.call_output)
        self.ui.label_chat_output.setText(f'{self.text_input} ({self.user})')
        self.ui.label_chat_input.setText(self.text_output)

        self.ui.confidence_label.setText(self.confidence)
        self.ui.group_label.setText(self.group)
        self.ui.catergory_label.setText(self.category)
        
    def update_graph(self):
        pass

    def run(self):
        self.running = not self.running

        if (self.thread is not None) and (self.thread.is_alive()):
            self.thread.join()

        self.worker = Worker()
        self.thread = threading.Thread(target=self.worker.run(self))
        self.thread.daemon = True
        self.thread.start()
        self.worker.finished.connect(self.thread.join())