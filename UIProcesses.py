from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    from PyQt5 import QtCore, QtGui, QtWidgets


def fileOpenFunctionality():
    openFileNames = QtWidgets.QFileDialog.getOpenFileNames(filter="*.csv")
    return openFileNames