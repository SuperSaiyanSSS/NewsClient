# -*- coding: utf-8 -*-

"""
Module implementing Error.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog

from Ui_pyloginerror import Ui_dialog


class Error(QDialog, Ui_dialog):
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
