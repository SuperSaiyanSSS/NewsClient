# -*- coding: utf-8 -*-

"""
Module implementing Firstlogin.
"""
import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QTabWidget
import hashlib
from Ui_pyui import Ui_TabWidget
from PyQt4.QtGui import *
sys.setdefaultencoding=('utf-8')
reload(sys)
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
from Ui_pyfirstlogin import Ui_Dialog
from pytab3 import TabWidget3
from pyloginerror import Error
from pyquestion import Loginqustion


# 对用户信息文档进行快速排序
def partition(L, low, high):
    pivotkey = L[low]
    while low < high:
        print high
        while low < high and L[high] > pivotkey:
            high -= 1
        temp = L[high]
        L[high] = L[low]
        L[low] = temp
        while low < high and L[low] < pivotkey:
            low += 1
        temp = L[high]
        L[high] = L[low]
        L[low] = temp
    # 返回枢纽所在位置
    return low


# 递归进行快排
def QSort(L, low, high):
    if low < high:
        pivotloc = partition(L, low, high)
        QSort(L, low, pivotloc-1)
        QSort(L, pivotloc+1, high)
    return L


class myLabel(QLabel):
    def __init__(self, parent = None):
        super(myLabel, self).__init__(parent)

    def mousePressEvent(self, e):##重载一下鼠标点击事件
        import pyquestion
        import pyss
        global f1
        if f1 < 5:
            a = pyquestion.Loginqustion()
          #  mainDialog.setDocumentMode(False)
            a.show()
            a.exec_()
            f1 += 1

    def mouseReleaseEvent(self, QMouseEvent):
        print 'you have release the mouse'


class myLabel2(QLabel):
    def __init__(self, parent = None):
        super(myLabel2, self).__init__(parent)

    # 重载一下鼠标点击事件
    def mousePressEvent(self, e):
        global f2
        global dig
        global salt
        global close
        if f2 == 0:
            f2 = 1
            # 对用户名加盐并加密
            username = str(dig.lineEdit.text())
            print 1111111
            print username
            if username == "":
                errorDialog = Error()
                errorDialog.show()
                errorDialog.exec_()
                f2 = 0
                return False
            username = username + salt
            username = hashlib.md5(username).hexdigest()
            password = str(dig.lineEdit_2.text())
            if password == "":
                errorDialog = Error()
                errorDialog.show()
                errorDialog.exec_()
                f2 = 0
                return False
            password = password + salt
            password = hashlib.md5(password).hexdigest()

            with open('userdata.txt', 'r') as f:
                userlist = f.readlines()
                userlist = QSort(userlist, 0, len(userlist)-1)
                for index, user in enumerate(userlist):
                    userlist[index] = userlist[index].strip().strip('\n')
            print userlist
            pos = self.binarySearch(userlist, username)
            print "the password is "+password
            print userlist[pos].split("---")[1].strip("\n")
            if pos == -1:
                print "Unable to find the user"
                errorDialog = Error()
                errorDialog.show()
                errorDialog.exec_()
            elif userlist[pos].split("---")[1].strip("\n") == password:
                close = 1
                mainDialog = TabWidget3()
                mainDialog.setUserData(userlist[pos])
                mainDialog.setDocumentMode(False)
                mainDialog.show()
                mainDialog.exec_()
            else:
                print "The password is error"
                errorDialog = Error()
                errorDialog.show()
                errorDialog.exec_()
            f2 = 0

    def mouseReleaseEvent(self, QMouseEvent):
        print 'you have release the mouse'
        global dig
        if close == 1:
            dig.hide()

    def binarySearch(self, userlist, username):
        low = 0
        high = len(userlist)-1
        print username
        while low <= high:
            mid = (low + high)/2
            print "mid"
            print userlist[mid].split("---")[0]
            if userlist[mid].split("---")[0] > username:
                high = mid - 1
            elif userlist[mid].split("---")[0] < username:
                low = mid + 1
            else:
                return mid
                print "find it"
        return -1


class Firstlogin(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        172
        29
        144
        59
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(u"登录界面")
        global f1
        global f2
        global close
        close = 0
        f1 = 0
        f2 = 0
        # 设置用户名 密码显示窗口
        self.lineEdit.setPlaceholderText(u'用户名')
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setPlaceholderText(u'密码')
        # 需要传入self才能使布局有效！！！不然怎么知道坐标
        self.mylabel_loginup = myLabel(self)
        self.mylabel_loginup.setGeometry(270, 260, 115, 40)
       # self.mylabel_loginup.setText("6666666666666666666666666666")

        self.mylabel2_go = myLabel2(self)
        self.mylabel2_go.setGeometry(535, 335, 50, 60)
       # self.mylabel2_go.setText("6666666666666666666666666666")

    def paintEvent(self, event):
        palette1 = QtGui.QPalette()
        #palette1.setColor(self.backgroundRole(), QColor(192, 253, 123))   # 设置背景颜色
        palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('login.jpg')))   # 设置背景图片
        self.setPalette(palette1)








if __name__ == '__main__':
    global dig
    global salt
    salt = "addlength"
    app = QtGui.QApplication(sys.argv)
    dig = Firstlogin()
    dig.show()
    sys.exit(app.exec_())