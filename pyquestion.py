# -*- coding: utf-8 -*-

"""
Module implementing LoginQustion.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
import PyQt4
from Ui_pyquestion import Ui_Dialog
import sys
from pyloginerror import Error
import hashlib


class Loginqustion(QDialog, Ui_Dialog):
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
        # 和MFC中把单选框设为一个组的方式差别很大
        # 必须用QButtonGroup这个类
        self.a = PyQt4.QtGui.QButtonGroup()
        self.a.addButton(self.radioButton_man, 1)
        self.a.addButton(self.radioButton_woman, 2)
        self.b = PyQt4.QtGui.QButtonGroup()
        self.b.addButton(self.radioButton_tooyoung, 1)
        self.b.addButton(self.radioButton_young, 2)
        self.b.addButton(self.radioButton_old, 3)


    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        username = unicode(str(self.lineEdit_username.text()))
        password = unicode(str(self.lineEdit_password.text()))
        if not username or not password:
            return False
        sex = self.a.checkedId()
        age = self.b.checkedId()
        junshi = caijing  = dongman = tiyu = yule = 0
        if self.checkBox_junshi.isChecked():
            junshi = 1
        if self.checkBox_caijing.isChecked():
            caijing = 1
        if self.checkBox_dongman.isChecked():
            dongman = 1
        if self.checkBox_tiyu.isChecked():
            tiyu = 1
        if self.checkBox_yule.isChecked():
            yule = 1
        if sex == 1:
            tiyu = 1
        else:
            yule = 1
        if age == 1:
            dongman = 1
        if age == 2:
            dongman = 1
        salt = "addlength"
        username = username + salt
        username = hashlib.md5(username).hexdigest()
        password = password + salt
        password = hashlib.md5(password).hexdigest()

        with open('userdata.txt', 'r') as f:
            lines = map(lambda line: line.split("---")[0], f.readlines())
            if username in lines:
                return
        with open('userdata.txt', 'a') as f:
            f.write(username+"---"+password+"---"+str(junshi)+"---"+str(caijing)+"---"+str(dongman)
                    +"---"+str(tiyu)+"---"+str(yule)+"\n")

        self.close()




if __name__ == '__main__':
    global dig
    global salt
    salt = "addlength"
    app = PyQt4.QtGui.QApplication(sys.argv)
    dig = Loginqustion()
    dig.show()
    sys.exit(app.exec_())
