import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
#import vtk
#from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
#import cv2
import numpy as np
import json
import copy
import math

from UI_template import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ### User param
        self.clicked_radius_threshold = 5

        # self.butCalibration.clicked.connect(self.push_butCalibration)
        # self.butShowFinalResult.clicked.connect(self.push_butShowFinalResult)
        # self.imgWebcamColor.mousePressEvent = self.click_imgWebCamColor
        # self.imgWebcamColor.mouseMoveEvent = self.move_imgWebCamColor
        # self.imgWebcamColor.keyPressEvent = self.press_imgWebCamColor

        #print(self.width(), self.height())
    def keypress_lblImage(self, e):
        print("keypress lblImage", e.key())

    def pushButOpen(self):
        print("pushButOpen")

    # close event 처리
    def closeEvent(self, QCloseEvent):
        print("Enter CloseEvent")        
        self.saveFilelist()
        self.deleteLater()
        QCloseEvent.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
