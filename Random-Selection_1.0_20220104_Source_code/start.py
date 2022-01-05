# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# 导入模块 #
from data.info_ui import Ui_Form
from data.selection import Selection

# 导入模块 #


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 275)
        MainWindow.setMinimumSize(QSize(640, 275))
        MainWindow.setMaximumSize(QSize(640, 275))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"data/img/WindowIcon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setInputMethodHints(Qt.ImhNone)
        self.label = QLabel(MainWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 641, 191))
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(100)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setTextInteractionFlags(
            Qt.LinksAccessibleByMouse
            | Qt.TextEditable
            | Qt.TextEditorInteraction
            | Qt.TextSelectableByKeyboard
            | Qt.TextSelectableByMouse
        )
        self.pushButton_Clear = QPushButton(MainWindow)
        self.pushButton_Clear.setObjectName(u"pushButton_Clear")
        self.pushButton_Clear.setGeometry(QRect(10, 215, 306, 51))
        font2 = QFont()
        font2.setFamily(u"\u6977\u4f53")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.pushButton_Clear.setFont(font2)
        self.pushButton_Clear.setStyleSheet(
            u"border-radius:16px;\n" "background:rgb(255, 170, 127)"
        )
        self.pushButton_Clear.setCheckable(False)
        self.pushButton_Start = QPushButton(MainWindow)
        self.pushButton_Start.setObjectName(u"pushButton_Start")
        self.pushButton_Start.setGeometry(QRect(325, 215, 306, 51))
        self.pushButton_Start.setFont(font2)
        self.pushButton_Start.setStyleSheet(
            u"border-radius:16px;\n" "background:rgb(64, 248, 162);"
        )
        self.pushButton_info = QPushButton(MainWindow)
        self.pushButton_info.setObjectName(u"pushButton_info")
        self.pushButton_info.setGeometry(QRect(313, 200, 16, 16))
        self.pushButton_info.setStyleSheet(
            u"color:rgb(255, 255, 255);\n"
            "border-radius:8px;\n"
            "background:rgb(0, 170, 255);"
        )

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # 绑定槽函数#
        self.pushButton_info.clicked.connect(self.Open_Info)
        self.pushButton_Start.clicked.connect(self.Start_Selection)
        self.pushButton_Clear.clicked.connect(self.Clear_Selection)
        # 绑定槽函数#

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow",
                u"\u968f\u673a\u9009\u62e9 - Random Selection - V1.0",
                None,
            )
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"-  -  -  -", None)
        )
        self.pushButton_Clear.setText(
            QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a - Clear", None)
        )
        self.pushButton_Start.setText(
            QCoreApplication.translate("MainWindow", u"\u5f00\u59cb - Start", None)
        )
        self.pushButton_info.setText(
            QCoreApplication.translate("MainWindow", u"i", None)
        )

    # retranslateUi

    # 清除文本框
    def Clear_Selection(self):
        self.label.setText("-  -  -  -")

    # 打开info窗口
    def Open_Info(self):
        self.form2 = QWidget()
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.form2)
        self.form2.show()

    # 执行完整的随机选取动态效果
    def Start_Selection(self):
        for TEMP0 in range(16):
            QThread.msleep(75)
            self.label.setText(Selection.Random_Selection())  # 随机选择一个文本并显示
            QApplication.processEvents()  # 实时刷新页面


# 启动窗口 #
if __name__ == "__main__":
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # DPI自适应
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
