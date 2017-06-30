# -*- coding: utf-8 -*-

"""
Module implementing ZhihuReply.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QDialog
import threads
from Ui_pyzhihu_reply import Ui_Dialog


class ZhihuReply(QDialog, Ui_Dialog):
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

    def setZhihuClientPid(self, me, pid):
        self.me = me
        self.pid = pid
    
    @pyqtSignature("")
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        import sys
        sys.setdefaultencoding = ('utf-8')
        reload(sys)
        from zhihu_oauth import zhcls
        reply_text = str(self.zhihu_textEdit.toPlainText())
        self.me.comment(self.pid, reply_text)
        self.close()


