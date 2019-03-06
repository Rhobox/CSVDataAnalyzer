from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd

if __name__ == "__main__":
    from PyQt5 import QtCore, QtGui, QtWidgets


def fileOpenFunctionality():
    open_file_names = QtWidgets.QFileDialog.getOpenFileNames(filter="*.csv")
    return open_file_names


def open_csv_file(file_name, header_line):
    try:
        return pd.read_csv(file_name, header=header_line)
    except UnicodeDecodeError:
        return pd.read_csv(file_name, encoding='CP1252', header=header_line)

