# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(360, 280)
        Form.setMinimumSize(QSize(360, 280))
        Form.setMaximumSize(QSize(360, 280))
        icon = QIcon()
        icon.addFile(u"data/img/WindowIcon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 201, 21))
        font = QFont()
        font.setFamily(u"\u6977\u4f53")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 212, 91, 20))
        self.label_2.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 281, 16))
        font1 = QFont()
        font1.setFamily(u"\u6977\u4f53")
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 50, 241, 21))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 90, 281, 21))
        self.label_5.setFont(font1)
        self.label_5.setTextFormat(Qt.MarkdownText)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 70, 281, 21))
        self.label_6.setFont(font1)
        self.label_6.setTextFormat(Qt.MarkdownText)
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 110, 291, 21))
        self.label_7.setFont(font)
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 130, 281, 16))
        self.label_8.setFont(font1)
        self.label_8.setTextFormat(Qt.MarkdownText)
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 170, 281, 16))
        self.label_9.setFont(font1)
        self.label_9.setTextFormat(Qt.MarkdownText)
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 150, 281, 16))
        self.label_10.setFont(font1)
        self.label_10.setTextFormat(Qt.MarkdownText)
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 190, 321, 21))
        font2 = QFont()
        font2.setFamily(u"\u6977\u4f53")
        font2.setPointSize(10)
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(110, 213, 181, 21))
        self.label_12.setFont(font1)
        self.label_12.setTextFormat(Qt.MarkdownText)
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 230, 291, 21))
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 250, 361, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5173\u4e8e\u6211\u4eec - About us - V1.0", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5236\u4f5c\u4eba\u5458(Producter)\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6781\u5ba2\u8857\u793e\u533a\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u7a3d\u672f\u5b85(funny-geek)", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u9879\u76ee\u5730\u5740(Project Address)\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"[Github](http://github.com/funny-geek/Random-Selection)", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"[Gitee](http://gitee.com/funny-geek/Random-Selection)", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u4ea4\u6d41\u7fa4\u804a(Exchange Group Chat)\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"[QQ\u7fa4\uff1a\u6781\u5ba2\u8857\u793e\u533a](https://jq.qq.com/?_wv=1027&k=vZK4aoHo)", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"[QQ\u7fa4\uff1aWindows/Linux/Mac\u7cfb\u7edf\u4ea4\u6d41](\u70b9\u51fb\u94fe\u63a5\u52a0\u5165\u7fa4\u804a\u3010Windows/Linux/Mac\u7cfb\u7edf\u4ea4\u6d41\u3011\uff1ahttps://jq.qq.com/?_wv=1027&k=tB7IJR04)", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"[QQ\u9891\u9053\uff1a\u6781\u5ba2\u8857\u6280\u672f\u4ea4\u6d41\u793e\u533a](https://qun.qq.com/qqweb/qunpro/share?_wv=3&_wwv=128&inviteCode=29YJNG&from=181074&biz=ka)", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"This is probably the first and last version", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"[http://geekjie.com](http://geekjie.com)", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u63d0\u793a\uff1aWindows\u7cfb\u7edf\u53f3\u952e\u70b9\u51fb\u6587\u672c\u4ee5\u590d\u5236\u94fe\u63a5", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Tip: Windows system right-click the text to copy the link", None))
    # retranslateUi

