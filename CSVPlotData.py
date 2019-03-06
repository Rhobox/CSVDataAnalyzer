from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import pandas as pd


class PlotData:
    def __init__(self, data, file_name):
        self.x_axis = None
        self.y_axis = None
        self.x_data = None
        self.y_data = None
        self.data = data
        headers = self.parse_headers(data.columns.values.tolist())
        self.headers = ["Index"] + headers

    def parse_headers(self, headers):
        allowable_types = ['float', 'int']
        for header in headers:
            if len([i for i in allowable_types if i in str(type(self.data[header][0]))]) < 1:
                headers.remove(header)
        return headers

    def initialize_plot_data(self):
        self.x_axis = self.headers[0]
        self.y_axis = self.headers[1]
        self.populate_plot_data()

    def update_x_axis(self, axis_name):
        self.x_axis = axis_name
        self.populate_plot_data()

    def update_y_axis(self, axis_name):
        self.y_axis = axis_name
        self.populate_plot_data()

    def populate_plot_data(self):
        self.populate_x()
        self.populate_y()

    def populate_x(self):
        if self.x_axis is not None:
            if self.x_axis == "Index":
                self.x_data = list(self.data.index.values)
            else:
                self.x_data = list(self.data[self.x_axis].astype(float))

    def populate_y(self):
        if self.y_axis is not None:
            if self.y_axis == "Index":
                self.y_data = list(self.data.index.values)
            else:
                self.y_data = list(self.data[self.y_axis].astype(float))
