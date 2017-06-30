# -*- coding: utf-8 -*-

"""
Module implementing PyReview.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
import PyQt4.QtGui
import sys

from Ui_pyreview import Ui_Dialog


class PyReview(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.stackedWidget.setCurrentIndex(1)

    @pyqtSignature("")
    def on_pushButton_3_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
if __name__ == '__main__':
    app = PyQt4.QtGui.QApplication(sys.argv)
    dig = PyReview()
    dig.show()
    sys.exit(app.exec_())