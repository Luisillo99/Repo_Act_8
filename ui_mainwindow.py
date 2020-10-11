# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(245, 468)
        self.label_13 = QLabel(Dialog)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 200, 53, 20))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(31, 40, 53, 20))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 120, 53, 20))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(31, 80, 53, 20))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(31, 160, 53, 20))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 430, 191, 23))
        self.label_24 = QLabel(Dialog)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(30, 240, 53, 20))
        self.label_25 = QLabel(Dialog)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(29, 280, 61, 20))
        self.label_26 = QLabel(Dialog)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(70, 310, 61, 20))
        self.label_27 = QLabel(Dialog)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(60, 350, 61, 20))
        self.label_28 = QLabel(Dialog)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(70, 390, 61, 20))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 10, 81, 16))
        font = QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.spinBox_2 = QSpinBox(Dialog)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(90, 80, 131, 20))
        self.spinBox_3 = QSpinBox(Dialog)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(90, 120, 131, 20))
        self.spinBox_4 = QSpinBox(Dialog)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(90, 160, 131, 20))
        self.spinBox_6 = QSpinBox(Dialog)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setGeometry(QRect(90, 200, 131, 20))
        self.spinBox_7 = QSpinBox(Dialog)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setGeometry(QRect(90, 240, 131, 20))
        self.spinBox_8 = QSpinBox(Dialog)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setGeometry(QRect(100, 310, 121, 21))
        self.spinBox_9 = QSpinBox(Dialog)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setGeometry(QRect(100, 350, 121, 21))
        self.spinBox_10 = QSpinBox(Dialog)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setGeometry(QRect(100, 390, 121, 21))
        self.spinBox_10.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox_10.setSingleStep(1)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 40, 131, 21))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Destino (Y)", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Origen (Y)", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Origen (X)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Destino (X)", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Agregar", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Velocidad", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Color (RGB):", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Red", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Green", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Blue", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Part\u00edculas", None))
    # retranslateUi

