# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HeaderLineOptions.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MainWindow as mw


class OptionsWindow(QtWidgets.QWidget):

    return_options = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(OptionsWindow, self).__init__(parent=parent)
        self.header_line = 0

    def connect_signals(self):
        self.pushButton.clicked.connect(self.confirm_options)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(156, 80)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label.setObjectName("label")
        self.header_line_edit = QtWidgets.QLineEdit(Dialog)
        self.header_line_edit.setGeometry(QtCore.QRect(80, 10, 61, 20))
        self.header_line_edit.setObjectName("header_line_edit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.connect_signals()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Header Line:"))
        self.pushButton.setText(_translate("Dialog", "Confirm"))

    def populate_options(self):
        self.header_line_edit.setText(str(self.header_line))

    def confirm_options(self):
        try:
            if str(self.header_line_edit.text()).lower() == "none":
                self.header_line = -1
            else:
                self.header_line = int(self.header_line_edit.text())
        except ValueError:
            self.header_line = 0
            print("It all burns")
        self.return_options.emit(self.header_line)
        self.hide()


