# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QCheckBox, QComboBox, QLabel, QLineEdit, QMenuBar, QProgressBar, QPushButton, QRadioButton, QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.down_from_sayo = QRadioButton(self.centralwidget)
        self.down_from_sayo.setObjectName(u"down_from_sayo")
        self.down_from_sayo.setGeometry(QRect(630, 490, 131, 20))
        self.down_from_offical = QRadioButton(self.centralwidget)
        self.down_from_offical.setObjectName(u"down_from_offical")
        self.down_from_offical.setEnabled(False)
        self.down_from_offical.setGeometry(QRect(630, 520, 171, 20))
        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 6):
            self.table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.table.rowCount() < 100):
            self.table.setRowCount(100)
        self.table.setObjectName(u"table")
        self.table.setEnabled(True)
        self.table.setGeometry(QRect(60, 70, 651, 231))
        self.table.setRowCount(100)
        self.table.setColumnCount(6)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.osu_id = QLineEdit(self.centralwidget)
        self.osu_id.setObjectName(u"osu_id")
        self.osu_id.setGeometry(QRect(110, 30, 113, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 53, 16))
        self.get_bp_button = QPushButton(self.centralwidget)
        self.get_bp_button.setObjectName(u"get_bp_button")
        self.get_bp_button.setGeometry(QRect(540, 30, 75, 24))
        self.download_all_button = QPushButton(self.centralwidget)
        self.download_all_button.setObjectName(u"download_all_button")
        self.download_all_button.setGeometry(QRect(540, 320, 75, 24))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(140, 390, 541, 23))
        self.progressBar.setValue(24)
        self.game_mode = QComboBox(self.centralwidget)
        self.game_mode.addItem("")
        self.game_mode.addItem("")
        self.game_mode.addItem("")
        self.game_mode.addItem("")
        self.game_mode.addItem("")
        self.game_mode.setObjectName(u"game_mode")
        self.game_mode.setGeometry(QRect(380, 30, 69, 22))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 30, 53, 16))
        self.down_status_label = QLabel(self.centralwidget)
        self.down_status_label.setObjectName(u"down_status_label")
        self.down_status_label.setGeometry(QRect(300, 370, 200, 20))
        self.save_as_osz_checkbox = QCheckBox(self.centralwidget)
        self.save_as_osz_checkbox.setObjectName(u"save_as_osz_checkbox")
        self.save_as_osz_checkbox.setGeometry(QRect(40, 490, 101, 20))
        self.save_as_osz_textedit = QLineEdit(self.centralwidget)
        self.save_as_osz_textedit.setObjectName(u"save_as_osz_textedit")
        self.save_as_osz_textedit.setGeometry(QRect(132, 490, 211, 21))
        self.save_to_osu_checkbox = QCheckBox(self.centralwidget)
        self.save_to_osu_checkbox.setObjectName(u"save_to_osu_checkbox")
        self.save_to_osu_checkbox.setGeometry(QRect(40, 520, 141, 20))
        self.save_to_osu_textedit = QLineEdit(self.centralwidget)
        self.save_to_osu_textedit.setObjectName(u"save_to_osu_textedit")
        self.save_to_osu_textedit.setGeometry(QRect(182, 520, 161, 21))
        self.btn_save_as_osz = QPushButton(self.centralwidget)
        self.btn_save_as_osz.setObjectName(u"btn_save_as_osz")
        self.btn_save_as_osz.setGeometry(QRect(350, 490, 41, 24))
        self.btn_save_to_osu = QPushButton(self.centralwidget)
        self.btn_save_to_osu.setObjectName(u"btn_save_to_osu")
        self.btn_save_to_osu.setGeometry(QRect(350, 520, 41, 24))
        self.oauth_config_btn = QPushButton(self.centralwidget)
        self.oauth_config_btn.setObjectName(u"oauth_config_btn")
        self.oauth_config_btn.setGeometry(QRect(650, 30, 75, 24))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(630, 540, 181, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.down_from_sayo.setText(QCoreApplication.translate("MainWindow", u"\u4eceSayobot\u955c\u50cf\u4e0b\u8f7d", None))
        self.down_from_offical.setText(QCoreApplication.translate("MainWindow", u"\u4ece\u5b98\u7f51\u4e0b\u8f7d(\u5728\u6446\uff0c\u8fd8\u6ca1\u505a)", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u66f2\u540d", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u96be\u5ea6\u540d", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Mod", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u96be\u5ea6\u661f\u7ea7", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u8c31\u5e08", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u8c31\u9762id", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"osu id:", None))
        self.get_bp_button.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6BP", None))
        self.download_all_button.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u4e0b\u8f7d", None))
        self.game_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4", None))
        self.game_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"standard", None))
        self.game_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"mania", None))
        self.game_mode.setItemText(3, QCoreApplication.translate("MainWindow", u"catch", None))
        self.game_mode.setItemText(4, QCoreApplication.translate("MainWindow", u"taiko", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u6a21\u5f0f:", None))
        self.down_status_label.setText("")
        self.save_as_osz_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u4ee5.osz\u4fdd\u5b58\u5230", None))
        self.save_to_osu_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u5230osu songs\u76ee\u5f55", None))
        self.btn_save_as_osz.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.btn_save_to_osu.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.oauth_config_btn.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6eOAuth", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"by \u5343\u91cc\u626f\u6de1 2023.3 v0.0.2", None))
    # retranslateUi

