# -*- coding: utf-8 -*-

"""
Module implementing zhihu_login_dialog.
"""
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog

from Ui_pyzhihu_login import Ui_Dialog


class zhihu_login_dialog(QDialog, Ui_Dialog):
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
        self.username = ""
        self.password = ""
        self.u_p = []
        self.flag = 0
    
    @pyqtSignature("")
    def on_pushButton_login_clicked(self):
        """
        Slot documentation goes here.
        """
        self.username = unicode(str(self.textEdit_userbane.toPlainText()))
        self.password = unicode(str(self.textEdit_password.toPlainText()))
        self.u_p = [self.username, self.password]
        self.flag = 1
        self.close()

    def getUsernamePassword(self):
        return self.u_p
