from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import threading as th

class InputLabel(QtWidgets.QLabel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def setMainParent(self):
        while self.parent.parent() is not None:
            self.parent = self.parent.parent()

    def mousePressEvent(self, event):
        self.setMainParent()
        index = self.objectName()[-1]
        index = int(index)-1
        thread = th.Thread(target=lambda: self.parent.downloadVideo(index))
        thread.start()

    def enterEvent(self, event):
        self.setMainParent()
        index = self.objectName()[-1]
        index = int(index)-1
        self.parent.titles[index].setStyleSheet("color: greenyellow;")
    
    def leaveEvent(self, event):
        self.setMainParent()
        index = self.objectName()[-1]
        index = int(index)-1
        self.parent.titles[index].setStyleSheet("color: #FF0066;")
