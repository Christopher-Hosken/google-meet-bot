# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'google_meet_bot.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 610)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setGeometry(QRect(0, 0, 780, 610))
        self.frame_main.setLayoutDirection(Qt.LeftToRight)
        self.frame_main.setAutoFillBackground(True)
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setGeometry(QRect(0, 0, 780, 50))
        self.frame_top.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.frame_btns_top = QFrame(self.frame_top)
        self.frame_btns_top.setObjectName(u"frame_btns_top")
        self.frame_btns_top.setGeometry(QRect(630, 0, 150, 50))
        self.frame_btns_top.setFrameShape(QFrame.NoFrame)
        self.frame_btns_top.setFrameShadow(QFrame.Raised)
        self.btn_maximize_restore = QPushButton(self.frame_btns_top)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        self.btn_maximize_restore.setGeometry(QRect(50, 0, 50, 50))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon)
        self.btn_minimize = QPushButton(self.frame_btns_top)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(0, 0, 50, 50))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)
        self.btn_close = QPushButton(self.frame_btns_top)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(100, 0, 50, 50))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.frame_label_top = QFrame(self.frame_top)
        self.frame_label_top.setObjectName(u"frame_label_top")
        self.frame_label_top.setGeometry(QRect(0, 0, 630, 50))
        self.frame_label_top.setStyleSheet(u"")
        self.frame_label_top.setFrameShape(QFrame.NoFrame)
        self.frame_label_top.setFrameShadow(QFrame.Raised)
        self.label_title_top_bar = QLabel(self.frame_label_top)
        self.label_title_top_bar.setObjectName(u"label_title_top_bar")
        self.label_title_top_bar.setGeometry(QRect(50, 0, 580, 50))
        palette = QPalette()
        brush = QBrush(QColor(210, 210, 210, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(210, 210, 210, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(190, 190, 190, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.label_title_top_bar.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        self.label_title_top_bar.setFont(font)
        self.label_title_top_bar.setStyleSheet(u"background: transparent;\n"
"")
        self.label_title_top_bar.setFrameShadow(QFrame.Plain)
        self.frame_icon_top_bar = QFrame(self.frame_label_top)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setGeometry(QRect(10, 10, 30, 30))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.frame_icon_top_bar.setPalette(palette1)
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(\"../gui/icons/16x16/cli-fingerprint.png\");\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)
        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setGeometry(QRect(0, 50, 780, 530))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.frame_right = QFrame(self.frame_center)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setGeometry(QRect(540, 0, 240, 530))
        self.frame_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_right.setFrameShape(QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.frame_settings = QFrame(self.frame_right)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setGeometry(QRect(0, 130, 240, 310))
        self.frame_settings.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.frame_settings_title_bar = QFrame(self.frame_settings)
        self.frame_settings_title_bar.setObjectName(u"frame_settings_title_bar")
        self.frame_settings_title_bar.setGeometry(QRect(0, 0, 240, 50))
        self.frame_settings_title_bar.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_settings_title_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_settings_title_bar.setFrameShadow(QFrame.Raised)
        self.label_settings_title = QLabel(self.frame_settings_title_bar)
        self.label_settings_title.setObjectName(u"label_settings_title")
        self.label_settings_title.setGeometry(QRect(10, 10, 220, 30))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush5 = QBrush(QColor(41, 45, 56, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.label_settings_title.setPalette(palette2)
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setBold(True)
        self.label_settings_title.setFont(font1)
        self.frame_settings_bar = QFrame(self.frame_settings)
        self.frame_settings_bar.setObjectName(u"frame_settings_bar")
        self.frame_settings_bar.setGeometry(QRect(0, 50, 240, 260))
        self.frame_settings_bar.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_settings_bar.setFrameShape(QFrame.NoFrame)
        self.frame_settings_bar.setFrameShadow(QFrame.Raised)
        self.frame_email_input_bar = QFrame(self.frame_settings_bar)
        self.frame_email_input_bar.setObjectName(u"frame_email_input_bar")
        self.frame_email_input_bar.setGeometry(QRect(10, 10, 220, 30))
        self.frame_email_input_bar.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.frame_email_input_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_email_input_bar.setFrameShadow(QFrame.Raised)
        self.input_email = QLineEdit(self.frame_email_input_bar)
        self.input_email.setObjectName(u"input_email")
        self.input_email.setGeometry(QRect(10, 5, 200, 25))
        palette3 = QPalette()
        brush6 = QBrush(QColor(98, 103, 111, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush7 = QBrush(QColor(27, 29, 35, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush7)
        brush8 = QBrush(QColor(98, 103, 111, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        brush9 = QBrush(QColor(98, 103, 111, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        brush10 = QBrush(QColor(98, 103, 111, 128))
        brush10.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        self.input_email.setPalette(palette3)
        self.input_email.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.frame_password_input_bar = QFrame(self.frame_settings_bar)
        self.frame_password_input_bar.setObjectName(u"frame_password_input_bar")
        self.frame_password_input_bar.setGeometry(QRect(10, 50, 220, 30))
        self.frame_password_input_bar.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.frame_password_input_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_password_input_bar.setFrameShadow(QFrame.Raised)
        self.input_password = QLineEdit(self.frame_password_input_bar)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setGeometry(QRect(10, 5, 200, 25))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush7)
        brush11 = QBrush(QColor(98, 103, 111, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        brush12 = QBrush(QColor(98, 103, 111, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        brush13 = QBrush(QColor(98, 103, 111, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.input_password.setPalette(palette4)
        self.input_password.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.input_password.setEchoMode(QLineEdit.Password)
        self.frame_btn_bar = QFrame(self.frame_settings_bar)
        self.frame_btn_bar.setObjectName(u"frame_btn_bar")
        self.frame_btn_bar.setGeometry(QRect(10, 90, 220, 160))
        self.frame_btn_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_bar.setFrameShadow(QFrame.Raised)
        self.frame_chat_bar = QFrame(self.frame_btn_bar)
        self.frame_chat_bar.setObjectName(u"frame_chat_bar")
        self.frame_chat_bar.setGeometry(QRect(10, 10, 200, 60))
        self.frame_chat_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_chat_bar.setFrameShadow(QFrame.Raised)
        self.btn_chat = QPushButton(self.frame_chat_bar)
        self.btn_chat.setObjectName(u"btn_chat")
        self.btn_chat.setGeometry(QRect(0, 0, 200, 60))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush14 = QBrush(QColor(52, 59, 72, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush14)
        brush15 = QBrush(QColor(203, 203, 203, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush15)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush14)
        brush16 = QBrush(QColor(203, 203, 203, 128))
        brush16.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush15)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush16)
#endif
        self.btn_chat.setPalette(palette5)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        self.btn_chat.setFont(font2)
        self.btn_chat.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.frame_call_bar = QFrame(self.frame_btn_bar)
        self.frame_call_bar.setObjectName(u"frame_call_bar")
        self.frame_call_bar.setGeometry(QRect(10, 90, 200, 60))
        self.frame_call_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_call_bar.setFrameShadow(QFrame.Raised)
        self.btn_call = QPushButton(self.frame_call_bar)
        self.btn_call.setObjectName(u"btn_call")
        self.btn_call.setGeometry(QRect(0, 0, 200, 60))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush15)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush15)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush16)
#endif
        self.btn_call.setPalette(palette6)
        self.btn_call.setFont(font2)
        self.btn_call.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.frame_run_bar = QFrame(self.frame_right)
        self.frame_run_bar.setObjectName(u"frame_run_bar")
        self.frame_run_bar.setGeometry(QRect(0, 440, 240, 90))
        self.frame_run_bar.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_run_bar.setFrameShape(QFrame.NoFrame)
        self.frame_run_bar.setFrameShadow(QFrame.Raised)
        self.btn_run = QPushButton(self.frame_run_bar)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setGeometry(QRect(10, 20, 220, 50))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush15)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush14)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush15)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush14)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush15)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush14)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush16)
#endif
        self.btn_run.setPalette(palette7)
        self.btn_run.setFont(font2)
        self.btn_run.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.btn_run.setCheckable(False)
        self.btn_run.setAutoDefault(False)
        self.btn_run.setFlat(False)
        self.frame_meet = QFrame(self.frame_right)
        self.frame_meet.setObjectName(u"frame_meet")
        self.frame_meet.setGeometry(QRect(0, 0, 240, 130))
        self.frame_meet.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_meet.setFrameShape(QFrame.StyledPanel)
        self.frame_meet.setFrameShadow(QFrame.Raised)
        self.frame_code_title_bar = QFrame(self.frame_meet)
        self.frame_code_title_bar.setObjectName(u"frame_code_title_bar")
        self.frame_code_title_bar.setGeometry(QRect(0, 0, 240, 50))
        self.frame_code_title_bar.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_code_title_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_code_title_bar.setFrameShadow(QFrame.Raised)
        self.label_code_title = QLabel(self.frame_code_title_bar)
        self.label_code_title.setObjectName(u"label_code_title")
        self.label_code_title.setGeometry(QRect(10, 10, 220, 30))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.label_code_title.setPalette(palette8)
        self.label_code_title.setFont(font1)
        self.frame_code_input_bar = QFrame(self.frame_meet)
        self.frame_code_input_bar.setObjectName(u"frame_code_input_bar")
        self.frame_code_input_bar.setGeometry(QRect(0, 50, 240, 80))
        self.frame_code_input_bar.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_code_input_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_code_input_bar.setFrameShadow(QFrame.Sunken)
        self.input_code = QLineEdit(self.frame_code_input_bar)
        self.input_code.setObjectName(u"input_code")
        self.input_code.setGeometry(QRect(10, 10, 220, 60))
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush7)
        brush17 = QBrush(QColor(190, 190, 190, 128))
        brush17.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Active, QPalette.PlaceholderText, brush17)
#endif
        palette9.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette9.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.input_code.setPalette(palette9)
        self.input_code.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.frame_left = QFrame(self.frame_center)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setGeometry(QRect(10, 20, 520, 500))
        self.frame_left.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.frame_left_title_bar = QFrame(self.frame_left)
        self.frame_left_title_bar.setObjectName(u"frame_left_title_bar")
        self.frame_left_title_bar.setGeometry(QRect(0, 0, 520, 40))
        self.frame_left_title_bar.setAutoFillBackground(False)
        self.frame_left_title_bar.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_left_title_bar.setFrameShape(QFrame.NoFrame)
        self.frame_left_title_bar.setFrameShadow(QFrame.Raised)
        self.label_panel_title = QLabel(self.frame_left_title_bar)
        self.label_panel_title.setObjectName(u"label_panel_title")
        self.label_panel_title.setGeometry(QRect(10, 10, 501, 20))
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.WindowText, brush15)
        palette10.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.WindowText, brush15)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_panel_title.setPalette(palette10)
        self.label_panel_title.setFont(font1)
        self.label_panel_title.setStyleSheet(u"background: transparent;\n"
"")
        self.frame_confidence = QFrame(self.frame_left)
        self.frame_confidence.setObjectName(u"frame_confidence")
        self.frame_confidence.setGeometry(QRect(9, 359, 501, 131))
        self.frame_confidence.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_confidence.setFrameShape(QFrame.StyledPanel)
        self.frame_confidence.setFrameShadow(QFrame.Raised)
        self.frame_confidence_graph_bar = QFrame(self.frame_confidence)
        self.frame_confidence_graph_bar.setObjectName(u"frame_confidence_graph_bar")
        self.frame_confidence_graph_bar.setGeometry(QRect(0, 50, 501, 81))
        self.frame_confidence_graph_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_confidence_graph_bar.setFrameShadow(QFrame.Raised)
        self.graph_confidence = QWidget(self.frame_confidence_graph_bar)
        self.graph_confidence.setObjectName(u"graph_confidence")
        self.graph_confidence.setGeometry(QRect(-1, 0, 251, 80))
        self.frame_category_bar = QFrame(self.frame_confidence_graph_bar)
        self.frame_category_bar.setObjectName(u"frame_category_bar")
        self.frame_category_bar.setGeometry(QRect(249, 0, 251, 80))
        self.frame_category_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_category_bar.setFrameShadow(QFrame.Raised)
        self.confidence_title = QLabel(self.frame_category_bar)
        self.confidence_title.setObjectName(u"confidence_title")
        self.confidence_title.setGeometry(QRect(10, 10, 100, 20))
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.confidence_title.setPalette(palette11)
        self.confidence_title.setFont(font)
        self.group_title = QLabel(self.frame_category_bar)
        self.group_title.setObjectName(u"group_title")
        self.group_title.setGeometry(QRect(10, 30, 100, 20))
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.group_title.setPalette(palette12)
        self.group_title.setFont(font)
        self.catergory_title = QLabel(self.frame_category_bar)
        self.catergory_title.setObjectName(u"catergory_title")
        self.catergory_title.setGeometry(QRect(10, 50, 100, 20))
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.catergory_title.setPalette(palette13)
        self.catergory_title.setFont(font)
        self.confidence_label = QLabel(self.frame_category_bar)
        self.confidence_label.setObjectName(u"confidence_label")
        self.confidence_label.setGeometry(QRect(120, 10, 120, 20))
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.confidence_label.setPalette(palette14)
        self.confidence_label.setFont(font2)
        self.group_label = QLabel(self.frame_category_bar)
        self.group_label.setObjectName(u"group_label")
        self.group_label.setGeometry(QRect(120, 30, 120, 20))
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.group_label.setPalette(palette15)
        self.group_label.setFont(font2)
        self.catergory_label = QLabel(self.frame_category_bar)
        self.catergory_label.setObjectName(u"catergory_label")
        self.catergory_label.setGeometry(QRect(120, 50, 120, 20))
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.catergory_label.setPalette(palette16)
        self.catergory_label.setFont(font2)
        self.frame_confidence_title_bar = QFrame(self.frame_confidence)
        self.frame_confidence_title_bar.setObjectName(u"frame_confidence_title_bar")
        self.frame_confidence_title_bar.setGeometry(QRect(0, 0, 500, 50))
        self.frame_confidence_title_bar.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_confidence_title_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_confidence_title_bar.setFrameShadow(QFrame.Raised)
        self.label_confidence_title = QLabel(self.frame_confidence_title_bar)
        self.label_confidence_title.setObjectName(u"label_confidence_title")
        self.label_confidence_title.setGeometry(QRect(10, 10, 480, 30))
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.WindowText, brush15)
        palette17.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.WindowText, brush15)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_confidence_title.setPalette(palette17)
        self.label_confidence_title.setFont(font1)
        self.label_confidence_title.setStyleSheet(u"background: transparent;\n"
"")
        self.frame_chat = QFrame(self.frame_left)
        self.frame_chat.setObjectName(u"frame_chat")
        self.frame_chat.setGeometry(QRect(10, 50, 500, 151))
        self.frame_chat.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_chat.setFrameShape(QFrame.StyledPanel)
        self.frame_chat.setFrameShadow(QFrame.Raised)
        self.frame_chat_title_bar = QFrame(self.frame_chat)
        self.frame_chat_title_bar.setObjectName(u"frame_chat_title_bar")
        self.frame_chat_title_bar.setGeometry(QRect(0, 0, 500, 50))
        self.frame_chat_title_bar.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_chat_title_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_chat_title_bar.setFrameShadow(QFrame.Raised)
        self.label_chat_title = QLabel(self.frame_chat_title_bar)
        self.label_chat_title.setObjectName(u"label_chat_title")
        self.label_chat_title.setGeometry(QRect(10, 10, 481, 30))
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.WindowText, brush15)
        palette18.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.WindowText, brush15)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_chat_title.setPalette(palette18)
        self.label_chat_title.setFont(font1)
        self.label_chat_title.setStyleSheet(u"background: transparent;\n"
"")
        self.frame_chat_input_bar = QFrame(self.frame_chat)
        self.frame_chat_input_bar.setObjectName(u"frame_chat_input_bar")
        self.frame_chat_input_bar.setGeometry(QRect(70, 50, 470, 50))
        self.frame_chat_input_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_chat_input_bar.setFrameShadow(QFrame.Raised)
        self.label_chat_input = QLabel(self.frame_chat_input_bar)
        self.label_chat_input.setObjectName(u"label_chat_input")
        self.label_chat_input.setGeometry(QRect(10, 10, 440, 30))
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette19.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette19.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.label_chat_input.setPalette(palette19)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(9)
        font3.setBold(False)
        self.label_chat_input.setFont(font3)
        self.label_chat_input.setFrameShadow(QFrame.Sunken)
        self.frame_chat_output_bar = QFrame(self.frame_chat)
        self.frame_chat_output_bar.setObjectName(u"frame_chat_output_bar")
        self.frame_chat_output_bar.setGeometry(QRect(70, 100, 470, 50))
        font4 = QFont()
        font4.setFamily(u"Ubuntu")
        font4.setPointSize(11)
        self.frame_chat_output_bar.setFont(font4)
        self.frame_chat_output_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_chat_output_bar.setFrameShadow(QFrame.Raised)
        self.label_chat_output = QLabel(self.frame_chat_output_bar)
        self.label_chat_output.setObjectName(u"label_chat_output")
        self.label_chat_output.setGeometry(QRect(10, 10, 440, 30))
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette20.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette20.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette20.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.label_chat_output.setPalette(palette20)
        self.label_chat_output.setFont(font2)
        self.label_chat_output.setFrameShape(QFrame.NoFrame)
        self.label_chat_output.setFrameShadow(QFrame.Sunken)
        self.label_chat_out_title = QLabel(self.frame_chat)
        self.label_chat_out_title.setObjectName(u"label_chat_out_title")
        self.label_chat_out_title.setGeometry(QRect(10, 110, 50, 30))
        palette21 = QPalette()
        palette21.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette21.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette21.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette21.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette21.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette21.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette21.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette21.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette21.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette21.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.label_chat_out_title.setPalette(palette21)
        self.label_chat_out_title.setFont(font)
        self.label_chat_in_title = QLabel(self.frame_chat)
        self.label_chat_in_title.setObjectName(u"label_chat_in_title")
        self.label_chat_in_title.setGeometry(QRect(10, 60, 50, 30))
        palette22 = QPalette()
        palette22.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette22.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette22.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette22.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette22.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette22.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette22.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette22.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette22.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette22.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette22.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette22.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.label_chat_in_title.setPalette(palette22)
        self.label_chat_in_title.setFont(font)
        self.frame_call = QFrame(self.frame_left)
        self.frame_call.setObjectName(u"frame_call")
        self.frame_call.setGeometry(QRect(10, 200, 500, 150))
        self.frame_call.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_call.setFrameShape(QFrame.StyledPanel)
        self.frame_call.setFrameShadow(QFrame.Raised)
        self.frame_call_output_bar = QFrame(self.frame_call)
        self.frame_call_output_bar.setObjectName(u"frame_call_output_bar")
        self.frame_call_output_bar.setGeometry(QRect(70, 100, 470, 50))
        self.frame_call_output_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_call_output_bar.setFrameShadow(QFrame.Raised)
        self.label_call_output = QLabel(self.frame_call_output_bar)
        self.label_call_output.setObjectName(u"label_call_output")
        self.label_call_output.setGeometry(QRect(10, 10, 440, 30))
        palette23 = QPalette()
        palette23.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette23.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette23.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette23.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette23.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette23.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.label_call_output.setPalette(palette23)
        self.label_call_output.setFont(font2)
        self.frame_call_input_bar = QFrame(self.frame_call)
        self.frame_call_input_bar.setObjectName(u"frame_call_input_bar")
        self.frame_call_input_bar.setGeometry(QRect(70, 50, 470, 50))
        self.frame_call_input_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_call_input_bar.setFrameShadow(QFrame.Raised)
        self.label_call_input = QLabel(self.frame_call_input_bar)
        self.label_call_input.setObjectName(u"label_call_input")
        self.label_call_input.setGeometry(QRect(10, 10, 440, 30))
        palette24 = QPalette()
        palette24.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette24.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette24.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette24.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette24.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette24.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette24.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette24.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette24.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette24.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.label_call_input.setPalette(palette24)
        self.label_call_input.setFont(font2)
        self.frame_call_title_bar = QFrame(self.frame_call)
        self.frame_call_title_bar.setObjectName(u"frame_call_title_bar")
        self.frame_call_title_bar.setGeometry(QRect(0, 0, 500, 50))
        self.frame_call_title_bar.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_call_title_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_call_title_bar.setFrameShadow(QFrame.Raised)
        self.label_call_title = QLabel(self.frame_call_title_bar)
        self.label_call_title.setObjectName(u"label_call_title")
        self.label_call_title.setGeometry(QRect(10, 10, 480, 30))
        palette25 = QPalette()
        palette25.setBrush(QPalette.Active, QPalette.WindowText, brush15)
        palette25.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette25.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette25.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.WindowText, brush15)
        palette25.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette25.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette25.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette25.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette25.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette25.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_call_title.setPalette(palette25)
        self.label_call_title.setFont(font1)
        self.label_call_title.setStyleSheet(u"background: transparent;\n"
"")
        self.label_call_in_title = QLabel(self.frame_call)
        self.label_call_in_title.setObjectName(u"label_call_in_title")
        self.label_call_in_title.setGeometry(QRect(10, 60, 50, 30))
        palette26 = QPalette()
        palette26.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette26.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette26.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette26.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette26.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette26.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette26.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette26.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette26.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette26.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette26.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette26.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.label_call_in_title.setPalette(palette26)
        self.label_call_in_title.setFont(font)
        self.label_call_out_title = QLabel(self.frame_call)
        self.label_call_out_title.setObjectName(u"label_call_out_title")
        self.label_call_out_title.setGeometry(QRect(10, 110, 50, 30))
        palette27 = QPalette()
        palette27.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette27.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette27.setBrush(QPalette.Active, QPalette.Window, brush5)
        palette27.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette27.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette27.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette27.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette27.setBrush(QPalette.Disabled, QPalette.Button, brush5)
        palette27.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette27.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        self.label_call_out_title.setPalette(palette27)
        self.label_call_out_title.setFont(font)
        self.frame_footer_bar = QFrame(self.frame_main)
        self.frame_footer_bar.setObjectName(u"frame_footer_bar")
        self.frame_footer_bar.setGeometry(QRect(0, 580, 780, 30))
        font5 = QFont()
        font5.setBold(True)
        font5.setItalic(True)
        self.frame_footer_bar.setFont(font5)
        self.frame_footer_bar.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_footer_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_footer_bar.setFrameShadow(QFrame.Raised)
        self.footer_name_title = QLabel(self.frame_footer_bar)
        self.footer_name_title.setObjectName(u"footer_name_title")
        self.footer_name_title.setGeometry(QRect(10, 5, 490, 20))
        palette28 = QPalette()
        palette28.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush18 = QBrush(QColor(33, 37, 43, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette28.setBrush(QPalette.Active, QPalette.Button, brush18)
        palette28.setBrush(QPalette.Active, QPalette.Base, brush18)
        palette28.setBrush(QPalette.Active, QPalette.Window, brush18)
        palette28.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette28.setBrush(QPalette.Inactive, QPalette.Button, brush18)
        palette28.setBrush(QPalette.Inactive, QPalette.Base, brush18)
        palette28.setBrush(QPalette.Inactive, QPalette.Window, brush18)
        palette28.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette28.setBrush(QPalette.Disabled, QPalette.Button, brush18)
        palette28.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        palette28.setBrush(QPalette.Disabled, QPalette.Window, brush18)
        self.footer_name_title.setPalette(palette28)
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setBold(True)
        font6.setItalic(True)
        self.footer_name_title.setFont(font6)
        self.footer_version_title = QLabel(self.frame_footer_bar)
        self.footer_version_title.setObjectName(u"footer_version_title")
        self.footer_version_title.setGeometry(QRect(700, 5, 70, 20))
        palette29 = QPalette()
        palette29.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette29.setBrush(QPalette.Active, QPalette.Button, brush18)
        palette29.setBrush(QPalette.Active, QPalette.Base, brush18)
        palette29.setBrush(QPalette.Active, QPalette.Window, brush18)
        palette29.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette29.setBrush(QPalette.Inactive, QPalette.Button, brush18)
        palette29.setBrush(QPalette.Inactive, QPalette.Base, brush18)
        palette29.setBrush(QPalette.Inactive, QPalette.Window, brush18)
        palette29.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette29.setBrush(QPalette.Disabled, QPalette.Button, brush18)
        palette29.setBrush(QPalette.Disabled, QPalette.Base, brush18)
        palette29.setBrush(QPalette.Disabled, QPalette.Window, brush18)
        self.footer_version_title.setPalette(palette29)
        self.footer_version_title.setFont(font6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btn_run.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_maximize_restore.setText("")
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.label_title_top_bar.setText(QCoreApplication.translate("MainWindow", u"Google Meet Bot - UI", None))
        self.label_settings_title.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.input_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.input_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_chat.setText(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.btn_call.setText(QCoreApplication.translate("MainWindow", u"Call", None))
        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.label_code_title.setText(QCoreApplication.translate("MainWindow", u"MEET CODE", None))
        self.input_code.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Code", None))
        self.label_panel_title.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.confidence_title.setText(QCoreApplication.translate("MainWindow", u"CONFIDENCE", None))
        self.group_title.setText(QCoreApplication.translate("MainWindow", u"GROUP", None))
        self.catergory_title.setText(QCoreApplication.translate("MainWindow", u"CATEGORY", None))
        self.confidence_label.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.group_label.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.catergory_label.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_confidence_title.setText(QCoreApplication.translate("MainWindow", u"CONFIDENCE", None))
        self.label_chat_title.setText(QCoreApplication.translate("MainWindow", u"MEET CHAT", None))
        self.label_chat_input.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_chat_output.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_chat_out_title.setText(QCoreApplication.translate("MainWindow", u"OUT", None))
        self.label_chat_in_title.setText(QCoreApplication.translate("MainWindow", u"IN", None))
        self.label_call_output.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_call_input.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.label_call_title.setText(QCoreApplication.translate("MainWindow", u"MEET CALL", None))
        self.label_call_in_title.setText(QCoreApplication.translate("MainWindow", u"IN", None))
        self.label_call_out_title.setText(QCoreApplication.translate("MainWindow", u"OUT", None))
        self.footer_name_title.setText(QCoreApplication.translate("MainWindow", u"Christopher Hosken", None))
        self.footer_version_title.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

