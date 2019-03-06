# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CSVDataAnalyzer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import UIProcesses as uip
import CSVPlotData as csvp
import OptionsWidget as ow


class UiMainWindow(object):
    def __init__(self):
        super().__init__()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.graphicsView = PlotWidget(self.centralwidget)
        self.reset_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.fileSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.fileList = QtWidgets.QListWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.fileHeaderXAxis = QtWidgets.QListWidget(self.centralwidget)
        self.fileHeaderYAxis = QtWidgets.QListWidget(self.centralwidget)

        self.plotData = {}
        self.currentFile = None
        self.x_axis = None
        self.y_axis = None
        self.open_file = None
        self.header_line = 0
        self.options_dialog = None
        self.clearing_signal = False

        self.options = ow.OptionsWindow()
        self.options.setupUi(self.options)
        self.options.return_options.connect(self.update_options)

    def connectSignals(self):
        self.actionClose.triggered.connect(self.close)
        self.actionOptions.triggered.connect(self.open_options_dialog)
        self.fileSelectButton.clicked.connect(self.file_open)
        self.reset_data_button.clicked.connect(self.clear_list)
        self.fileList.currentItemChanged.connect(self.file_list_item_activated)
        self.fileHeaderXAxis.currentItemChanged.connect(self.file_x_header_changed)
        self.fileHeaderYAxis.currentItemChanged.connect(self.file_y_header_changed)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)

        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView.setGeometry(QtCore.QRect(355, 10, 431, 431))
        self.graphicsView.setObjectName("graphicsView")

        self.reset_data_button.setGeometry(QtCore.QRect(100, 10, 81, 23))
        self.reset_data_button.setObjectName("fileLocationLineEdit")

        self.fileSelectButton.setGeometry(QtCore.QRect(10, 10, 81, 23))
        self.fileSelectButton.setObjectName("fileSelectButton")

        self.fileList.setGeometry(QtCore.QRect(10, 40, 331, 281))
        self.fileList.setObjectName("fileList")

        self.fileHeaderXAxis.setGeometry(QtCore.QRect(20, 340, 131, 111))
        self.fileHeaderXAxis.setObjectName("listWidget")

        self.fileHeaderYAxis.setGeometry(QtCore.QRect(200, 340, 131, 111))
        self.fileHeaderYAxis.setObjectName("listWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menuFile.setObjectName("menuFile")

        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionClose.setObjectName("actionClose")

        self.actionOptions.setObjectName("actionThese_dont_exist_yet")
        self.menuFile.addAction(self.actionClose)
        self.menuOptions.addAction(self.actionOptions)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.connectSignals()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CSV Data Analyzer"))
        self.fileSelectButton.setText(_translate("MainWindow", "Open Files..."))
        self.reset_data_button.setText(_translate("MainWindow", "Clear List"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionClose.setText(_translate("MainWindow", "Close..."))
        self.actionOptions.setText(_translate("MainWindow", "Options..."))

    def open_options_dialog(self):
        self.options.populate_options()
        self.options.show()

    def update_options(self, header_line):
        if header_line < 0:
            self.header_line = None
        else:
            self.header_line = header_line

    @staticmethod
    def close():
        QtCore.QCoreApplication.instance().quit()

    def clear_list(self):
        self.graphicsView.plotItem.clear()
        self.plotData = {}
        self.currentFile = None
        self.clearing_signal = True
        self.fileList.clear()
        self.fileHeaderXAxis.clear()
        self.fileHeaderYAxis.clear()

    def file_open(self):
        file_name_list = uip.fileOpenFunctionality()[0]
        self.add_file_names_to_file_list(file_name_list)

    def add_file_names_to_file_list(self, file_name_list):
        for name in file_name_list:
            if self.check_file_list_for_duplicates(name):
                self.fileList.addItem(name)

    def check_file_list_for_duplicates(self, file_name):
        if self.fileList.findItems(file_name, QtCore.Qt.MatchExactly):
            return False
        return True

    def file_list_item_activated(self):
        if not self.clearing_signal:
            current_file_name = self.fileList.currentItem().text()
            self.add_missing_plot_data_dict_item(current_file_name)
            self.currentFile = self.plotData[current_file_name]
            self.currentFile.initialize_plot_data()
            self.populate_header_list_boxes()
            self.plot_data()
        else:
            self.clearing_signal = False

    def add_missing_plot_data_dict_item(self, current_file_name):
        if current_file_name not in self.plotData.keys():
            self.plotData[current_file_name] = csvp.PlotData(uip.open_csv_file(self.fileList.currentItem().text(),
                                                                               self.header_line), current_file_name)

    def file_x_header_changed(self):
        if self.fileHeaderXAxis.currentItem() is not None:
            self.currentFile.update_x_axis(self.fileHeaderXAxis.currentItem().text())
            self.plot_data()

    def file_y_header_changed(self):
        if self.fileHeaderYAxis.currentItem() is not None:
            self.currentFile.update_y_axis(self.fileHeaderYAxis.currentItem().text())
            self.plot_data()

    def populate_header_list_boxes(self):
        self.fileHeaderXAxis.clear()
        self.fileHeaderYAxis.clear()
        self.fileHeaderXAxis.addItems(self.currentFile.headers)
        self.fileHeaderYAxis.addItems(self.currentFile.headers)

    def plot_data(self):
        self.graphicsView.plotItem.clear()
        self.graphicsView.plotItem.plot(self.currentFile.x_data, self.currentFile.y_data)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

