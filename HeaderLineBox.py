# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HeaderLineOptions.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(171, 83)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.header_line_label = QtWidgets.QLabel(Form)
        self.header_line_label.setGeometry(QtCore.QRect(10, 0, 61, 16))
        self.header_line_label.setObjectName("header_line_label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Confirm"))
        self.header_line_label.setText(_translate("Form", "Header Line:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
