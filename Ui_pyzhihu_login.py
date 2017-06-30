# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\py\workplace\xm3\pyzhihu_login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(407, 397)
        Dialog.setSizeGripEnabled(True)
        self.pushButton_login = QtGui.QPushButton(Dialog)
        self.pushButton_login.setGeometry(QtCore.QRect(120, 260, 151, 51))
        self.pushButton_login.setObjectName(_fromUtf8("pushButton_login"))
        self.label_username = QtGui.QLabel(Dialog)
        self.label_username.setGeometry(QtCore.QRect(10, 40, 381, 21))
        self.label_username.setObjectName(_fromUtf8("label_username"))
        self.textEdit_userbane = QtGui.QTextEdit(Dialog)
        self.textEdit_userbane.setGeometry(QtCore.QRect(10, 70, 371, 31))
        self.textEdit_userbane.setObjectName(_fromUtf8("textEdit_userbane"))
        self.textEdit_password = QtGui.QTextEdit(Dialog)
        self.textEdit_password.setGeometry(QtCore.QRect(10, 180, 371, 31))
        self.textEdit_password.setObjectName(_fromUtf8("textEdit_password"))
        self.label_password = QtGui.QLabel(Dialog)
        self.label_password.setGeometry(QtCore.QRect(10, 140, 371, 21))
        self.label_password.setObjectName(_fromUtf8("label_password"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "登录知乎", None))
        self.pushButton_login.setText(_translate("Dialog", "确认登录", None))
        self.label_username.setText(_translate("Dialog", "请输入知乎邮箱账号或手机账号（手机号前加“+86”！）", None))
        self.label_password.setText(_translate("Dialog", "请输入您知乎账号的密码", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

