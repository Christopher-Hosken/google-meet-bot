import sys
import time
import platform
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import *
from gui.google_meet_bot_ui import *
import read
import listen
from login import login_google, login_meet
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' + platform.release())

        self.enable_chat = True
        self.enable_call = True

        self.email = self.ui.input_email.text()
        self.password = self.ui.input_password.text()
        self.code = self.ui.input_code.text()

        self.browser = None
        self.last_text_msg = " "
        self.last_user = "N/A"
        self.out_text_msg = " "
        self.out_call_msg = " "
        self.last_conf = 0.0
        self.last_cat = " "


        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)

        self.ui.btn_minimize.setIcon(QtGui.QIcon(
            'gui/icons/16x16/cil-window-minimize.png'))
        self.ui.btn_maximize_restore.setIcon(
            QtGui.QIcon('gui/icons/16x16/cil-window-maximize.png'))
        self.ui.btn_close.setIcon(QtGui.QIcon('gui/icons/16x16/cil-x.png'))

        self.ui.btn_logo.setIcon(QtGui.QIcon('gui/icons/16x16/cil-speech.png'))

        ########################################################################
        # START - WINDOW ATTRIBUTES
        ########################################################################
        flags = QtCore.Qt.WindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        self.ui.frame_top.mouseMoveEvent = self.moveWindow

        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.btn_maximize_restore.clicked.connect(self.resize(780, 610))
        self.ui.btn_close.clicked.connect(sys.exit)

        self.threshold = (self.ui.threshold_slider.value()) / 100

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
        call_input = None
        call_output = None
        text_input = None
        text_output = None
        user = "you"
        confidence = None
        group = None
        category = None

        try:
            if (not self.enable_call):
                text_input, text_output, category, confidence = listen.run(self.browser, self.threshold)
            if (not self.enable_chat):
                text_input, text_output, user, category, confidence = read.run(self.browser, self.threshold)
        except Exception as e:
                print(e)

        if user == "you":
            text_input = self.last_text_msg
            user = self.last_user
        else:
            self.last_text_msg = text_input
            self.last_user = user

        if text_output == None:
            text_output = self.out_text_msg
        else:
            self.out_text_msg = text_output

        if call_output == None:
            call_output = self.out_call_msg
        else:
            self.out_call_msg = call_output

        if (category == "" or category == None):
            category = self.last_cat
        else:
            self.last_cat = category

        if (confidence == None):
            confidence = self.last_conf
        else:
            self.last_conf = confidence

        self.ui.label_call_input.setText(call_input)
        self.ui.label_call_output.setText(call_output)
        self.ui.label_chat_input.setText(f'{text_input} ({user})')
        self.ui.label_chat_output.setText(text_output)

        self.ui.confidence_label.setText(str(confidence))
        self.ui.catergory_label.setText(category)
        
    def update_graph(self):
        pass

    def run(self):
        if self.browser is not None:
            self.ui.btn_run.setText("Run")
            self.ui.btn_run.setStyleSheet(
            u"QPushButton {\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n")
            self.timer.stop()
            self.browser.quit()
            self.browser = None
            return

        else:
            self.ui.btn_run.setText("Stop")
            self.ui.btn_run.setStyleSheet(
                u"QPushButton {\n"
                "	border: 2px solid rgb(32, 36, 44);\n"
                "	border-radius: 5px;	\n"
                "	background-color: rgb(32, 36, 44);\n"
                "}\n")
            time.sleep(1)
            opt = Options()
            opt.add_experimental_option("prefs", {
                "profile.default_content_setting_values.media_stream_mic": 1,
                "profile.default_content_setting_values.media_stream_camera": 1,
                "profile.default_content_setting_values.notifications" : 1})
            self.browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)
            try:
                login_google(self.browser, self.ui.input_email.text(), self.ui.input_password.text())
                login_meet(self.browser, self.ui.input_code.text())
            except Exception as e:
                print(e)

            self.timer.start(500)