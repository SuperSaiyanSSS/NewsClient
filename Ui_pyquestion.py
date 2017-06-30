# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\py\workplace\xm3\pyquestion.ui'
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
        Dialog.resize(512, 531)
        Dialog.setSizeGripEnabled(True)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 140, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 220, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 310, 72, 15))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.checkBox_junshi = QtGui.QCheckBox(Dialog)
        self.checkBox_junshi.setGeometry(QtCore.QRect(130, 310, 91, 19))
        self.checkBox_junshi.setObjectName(_fromUtf8("checkBox_junshi"))
        self.checkBox_tiyu = QtGui.QCheckBox(Dialog)
        self.checkBox_tiyu.setGeometry(QtCore.QRect(250, 310, 91, 19))
        self.checkBox_tiyu.setObjectName(_fromUtf8("checkBox_tiyu"))
        self.checkBox_yule = QtGui.QCheckBox(Dialog)
        self.checkBox_yule.setGeometry(QtCore.QRect(380, 310, 91, 19))
        self.checkBox_yule.setObjectName(_fromUtf8("checkBox_yule"))
        self.checkBox_caijing = QtGui.QCheckBox(Dialog)
        self.checkBox_caijing.setGeometry(QtCore.QRect(130, 380, 91, 19))
        self.checkBox_caijing.setObjectName(_fromUtf8("checkBox_caijing"))
        self.checkBox_dongman = QtGui.QCheckBox(Dialog)
        self.checkBox_dongman.setGeometry(QtCore.QRect(250, 380, 91, 19))
        self.checkBox_dongman.setObjectName(_fromUtf8("checkBox_dongman"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 72, 15))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_username = QtGui.QLineEdit(Dialog)
        self.lineEdit_username.setGeometry(QtCore.QRect(130, 30, 171, 31))
        self.lineEdit_username.setObjectName(_fromUtf8("lineEdit_username"))
        self.lineEdit_password = QtGui.QLineEdit(Dialog)
        self.lineEdit_password.setGeometry(QtCore.QRect(130, 80, 171, 31))
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 72, 15))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 450, 151, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.radioButton_man = QtGui.QRadioButton(Dialog)
        self.radioButton_man.setGeometry(QtCore.QRect(130, 140, 115, 19))
        self.radioButton_man.setObjectName(_fromUtf8("radioButton_man"))
        self.radioButton_woman = QtGui.QRadioButton(Dialog)
        self.radioButton_woman.setGeometry(QtCore.QRect(250, 140, 237, 19))
        self.radioButton_woman.setObjectName(_fromUtf8("radioButton_woman"))
        self.radioButton_tooyoung = QtGui.QRadioButton(Dialog)
        self.radioButton_tooyoung.setGeometry(QtCore.QRect(130, 220, 113, 19))
        self.radioButton_tooyoung.setObjectName(_fromUtf8("radioButton_tooyoung"))
        self.radioButton_young = QtGui.QRadioButton(Dialog)
        self.radioButton_young.setGeometry(QtCore.QRect(250, 220, 176, 19))
        self.radioButton_young.setObjectName(_fromUtf8("radioButton_young"))
        self.radioButton_old = QtGui.QRadioButton(Dialog)
        self.radioButton_old.setGeometry(QtCore.QRect(380, 220, 359, 19))
        self.radioButton_old.setObjectName(_fromUtf8("radioButton_old"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "性别", None))
        self.label_2.setText(_translate("Dialog", "年龄", None))
        self.label_3.setText(_translate("Dialog", "爱好", None))
        self.checkBox_junshi.setText(_translate("Dialog", "军事", None))
        self.checkBox_tiyu.setText(_translate("Dialog", "体育", None))
        self.checkBox_yule.setText(_translate("Dialog", "娱乐", None))
        self.checkBox_caijing.setText(_translate("Dialog", "财经", None))
        self.checkBox_dongman.setText(_translate("Dialog", "动漫", None))
        self.label_4.setText(_translate("Dialog", "用户名", None))
        self.label_5.setText(_translate("Dialog", "密码", None))
        self.pushButton.setText(_translate("Dialog", "确认注册", None))
        self.radioButton_man.setText(_translate("Dialog", "男", None))
        self.radioButton_woman.setText(_translate("Dialog", "女", None))
        self.radioButton_tooyoung.setText(_translate("Dialog", "16岁以下", None))
        self.radioButton_young.setText(_translate("Dialog", "16岁——30岁", None))
        self.radioButton_old.setText(_translate("Dialog", "30岁以上", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

