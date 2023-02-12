# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'oauth_config.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QLabel, QLineEdit, QMenuBar, QProgressBar, QPushButton, QRadioButton, QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 61, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 71, 16))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(110, 30, 251, 21))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(110, 60, 251, 21))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 141, 16))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 71, 16))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 160, 75, 21))
        self.apply = QPushButton(Dialog)
        self.apply.setObjectName(u"apply")
        self.apply.setGeometry(QRect(310, 260, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u5ba2\u6237\u7aef ID:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5ba2\u6237\u7aef\u5bc6\u94a5:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"*\u4ec5\u7528\u4e8e\u83b7\u53d6BP\u4fe1\u606f", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"**\u5982\u4f55\u83b7\u53d6\uff1f", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u8df3\u8f6c\u81f3\u6559\u7a0b", None))
        self.apply.setText(QCoreApplication.translate("Dialog", u"\u5e94\u7528\u8bbe\u7f6e", None))
    # retranslateUi

