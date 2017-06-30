# -*- coding: utf-8 -*-

"""
Module implementing TabWidget3.
"""

from PyQt4.QtCore import pyqtSignature
from PyQt4.QtGui import QTabWidget
from Ui_pyui import Ui_TabWidget
import sys
from PyQt4.QtGui import *
sys.setdefaultencoding=('utf-8')
reload(sys)
import ghtt
import csv
from data_structure import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from pyzhihu_login import zhihu_login_dialog
from pyquestion import Loginqustion


class TabWidget3(QTabWidget, Ui_TabWidget):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        初始化
        
        @param parent reference to the parent widget
        @type QWidget
        """
        QTabWidget.__init__(self, parent)
        self.setupUi(self)
        self.test = 0
        self.tabBar().setStyleSheet("QTabBar{font-size:20px;height:40;border:none}")
        self.tab_2.setStyleSheet("QTabWidget{color:#ffffff;font-size:20px;}")
        # 初始化背景图片选择
        self.background_color_flag = 1
        #self.printColor()
        # 图片加载
        self.sina_pic.setPixmap(QPixmap('sina.png').scaled(self.label.width(), self.label.height()))
        self.ghtt_pic.setPixmap(QPixmap('ghtt.png').scaled(self.label.width(), self.label.height()))
        # 初始化省份
        self.BSTree = BSTree()
        for i in self.BSTree.findProvince():
            self.fz_sheng.addItem(i)

    # 传入用户信息
    def setUserData(self, line_list):
        self.bool_junshi = line_list.split("---")[2]
        self.bool_caijing = line_list.split("---")[3]
        self.bool_dongman = line_list.split("---")[4]
        self.bool_tiyu = line_list.split("---")[5]
        self.bool_yule = line_list.split("---")[6]
        self.setHobbyNews()

    def setHobbyNews(self):
        self.label_hobby.setWordWrap(True)
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        if int(self.bool_junshi) == 1:
            with open('hobby_junshi.txt', 'r') as f:
                junshi = f.readlines()
                junshi = ''.join(junshi)
               # junshi = QtCore.QString(junshi)
                print junshi
            self.label_hobby.setText(unicode(junshi))
        elif int(self.bool_caijing) == 1:
            with open('hobby_caijing.txt', 'r') as f:
                caijing = f.readlines()
                caijing = ''.join(caijing)
            self.label_hobby.setText(unicode(caijing))
        elif int(self.bool_dongman) == 1:
            with open('hobby_dongman.txt', 'r') as f:
                dongman = f.readlines()
                dongman = ''.join(dongman)
            self.label_hobby.setText(unicode(dongman))
        elif int(self.bool_yule) == 1:
            with open('hobby_dongman.txt', 'r') as f:
                dongman = f.readlines()
                dongman = ''.join(dongman)
            self.label_hobby.setText(unicode(dongman))
        else:
            with open('hobby_tiyu.txt', 'r') as f:
                caijing = f.readlines()
                caijing = ''.join(caijing)
            self.label_hobby.setText(unicode(caijing))

    def on_pushButton_clicked(self):
        #self.label_3.setWordWrap(True)
        aaa = self.textEdit.toPlainText()
        target_list = []
        allcontent_list = []
        with open('fenci.txt', 'r') as f:
            ci_lines = f.readlines()
            for i in ci_lines:
                if str(i.split("---")[0]) == str(aaa):
                    target_list.append(i.split("---")[1].strip('\n'))
        with open('ghtt_save.csv', 'r') as f:
            reader = csv.reader(f)
            # 去除csv第一行的内容
            i_count = 0
            for i in reader:
                # print i
                if i_count != 0:
                    allcontent_list.append(i)
                i_count += 1
        print target_list
        if not target_list:
            self.textEdit_ha.setText(u"没有发现标题含有该关键词的帖子！")
        else:
            self.textEdit_ha.setText(unicode(allcontent_list[int(target_list[0])][4]))
        self.hobby_link = TwoWayLinkedList()
        for i in target_list:
            self.hobby_link.append(allcontent_list[int(i)][4])
            self.hobby_p0 = self.hobby_link.head

    def on_pushButton_3_clicked(self):
        if self.hobby_p0 != self.hobby_link.tail:
            self.hobby_p0 = self.hobby_p0.next
            self.textEdit_ha.setText(unicode(self.hobby_p0.data))

    def on_pushButton_2_clicked(self):
        if self.hobby_p0 != self.hobby_link.head:
            self.hobby_p0 = self.hobby_p0.pre
            self.textEdit_ha.setText(unicode(self.hobby_p0.data))



    def printColor(self):
        self.p1.setStyleSheet("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}"
                               "QPushButton:hover{background-color:#333333;}")
        self.p2.setStyleSheet("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}"
                               "QPushButton:hover{background-color:#333333;}")
        self.n1.setStyleSheet("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}"
                               "QPushButton:hover{background-color:#333333;}")
        self.n2.setStyleSheet("QPushButton{background-color:#16A085;border:none;color:#ffffff;font-size:20px;}"
                               "QPushButton:hover{background-color:#333333;}")
        self.getweibo.setStyleSheet("QPushButton{background-color:#16A095;border:none;color:#ffffff;font-size:20px;}"
                               "QPushButton:hover{background-color:#333333;}")
        self.getzhihu.setStyleSheet("QPushButton{background-color:#16A095;border:none;color:#ffffff;font-size:20px;}"
                               "QPushButton:hover{background-color:#333333;}")
        self.zhihu_relogin.setStyleSheet("QPushButton{background-color:#D35400;border:none;color:#ffffff;font-size:20px;}"
                                 "QPushButton:hover{background-color:#333333;}")
        self.sina_gn.setStyleSheet("QPushButton{background-color:#16A095;border:none;color:#ffffff;font-size:20px;}"
                                 "QPushButton:hover{background-color:#333333;}")
        self.sina_gj.setStyleSheet("QPushButton{background-color:#16A095;border:none;color:#ffffff;font-size:20px;}"
                                 "QPushButton:hover{background-color:#333333;}")
        self.sina_sh.setStyleSheet("QPushButton{background-color:#16A095;border:none;color:#ffffff;font-size:20px;}"
                                 "QPushButton:hover{background-color:#333333;}")
        self.sina_next.setStyleSheet("QPushButton{background-color:#16A095;border:none;color:#ffffff;font-size:20px;}"
                                 "QPushButton:hover{background-color:#333333;}")
        self.sina_pre.setStyleSheet("QPushButton{background-color:#D35400;border:none;color:#ffffff;font-size:20px;}"
                                 "QPushButton:hover{background-color:#333333;}")
        self.ghtt_crawl_button.setStyleSheet("QPushButton{background-color:#16A095;border:none;color:#ffffff;font-size:20px;}"
                                 "QPushButton:hover{background-color:#333333;}")
        self.ghtt_reset.setStyleSheet("QPushButton{background-color:#16A095;border:none;color:#ffffff;font-size:20px;}"
                                 "QPushButton:hover{background-color:#333333;}")
        self.ghtt_send.setStyleSheet("QPushButton{background-color:#16A095;border:none;color:#ffffff;font-size:20px;}"
                                 "QPushButton:hover{background-color:#333333;}")
        self.label_2.setStyleSheet("QLabel{border:none;color:#ffffff;font-size:16px;}")
        self.textEdit1.setStyleSheet("QTextEdit{border:none;color:#ffffff;font-size:18px;}")
        self.textEdit2.setStyleSheet("QTextEdit{border:none;color:#ffffff;font-size:18px;}")
        self.sina_textBrowser.setStyleSheet("QTextBrowser{color:#ffffff;font-size:18px;}")
        self.ghtt_textbrowser1.setStyleSheet("QTextBrowser{color:#ffffff;font-size:18px;}")
        self.ghtt_postedit.setStyleSheet("QTextEdit{color:#ffffff;font-size:18px;}")
        self.label.setStyleSheet("QLabel{border:none;color:#ffffff;font-size:16px;}")

    def paintEvent(self, event):
        palette1 = QtGui.QPalette()
        #palette1.setColor(self.backgroundRole(), QColor(192, 253, 123))   # 设置背景颜色
        if self.background_color_flag == 1:
            palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('lbye.jpg')))   # 设置背景图片
        self.setPalette(palette1)


    @pyqtSignature("QString")
    def on_fz_sheng_activated(self, p0):
        """
        获取受到点击的省份
        展示该省份下的市区列表
        
        @param p0 DESCRIPTION
        @type QString
        """
        self.fz_zhong.clear()
        for i in self.BSTree.findCity(p0):
            self.fz_zhong.addItem(i)
    
    @pyqtSignature("QString")
    def on_fz_zhong_activated(self, p0):
        """
        获取受到点击的市区
        展示该市区下的新闻网址列表
        
        @param p0 DESCRIPTION
        @type QString
        """
        self.fz_name.clear()
        for i in self.BSTree.findWebsite(p0):
            self.fz_name.addItem(i)
    
    @pyqtSignature("QString")
    def on_fz_name_activated(self, p0):
        """
        在文本框中展示选中的网站地址
        
        @param p0 DESCRIPTION
        @type QString
        """
        self.fz_textEdit1.clear()
        self.fz_textEdit1.setText(u"新闻网站地址： "+p0)
        p0 = p0.split('---')[1]
        global url
        url = QUrl(p0)
        self.webView = WebView()
        self.webView.show()
        #self.webView.load(QUrl(p0))

    
    @pyqtSignature("")
    def on_sina_gn_clicked(self):
        """
        获取新浪国内新闻
        """
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.sina_gn_content_list = []
        with open('sina_guonei.csv', 'r') as f:
            reader = csv.reader(f)
            # 去除csv第一行的内容
            i_count = 0
            for i in reader:
                # print i
                if i_count != 0:
                    self.sina_gn_content_list.append(i)
                i_count += 1
            sina_gn_list = []
            for i in self.sina_gn_content_list:
                # print i
                # 转化为heapnode
                sina_gn_node = HeapNode(i[1], i[0])
                sina_gn_list.append(sina_gn_node)

        # 定义新浪国内新闻的最大根堆
        self.sina_gn_heap = MaxHeap(i_count, sina_gn_list)
        # 建立最大根堆
        self.sina_gn_heap.buildHeap()
        # 取出时间最大(最新)的结点
        sina_gn_first = self.sina_gn_heap.deleteMax()
        self.sina_textBrowser.setText(unicode('+'+sina_gn_first.text))

        # 开一子线程，获取最新新闻
        from threads import SinaGnThread
        self.sina_gnThread = SinaGnThread()
        self.sina_gnThread.start()
        print u"现在开始抓取新浪国内新闻！"

    @pyqtSignature("")
    def on_sina_gj_clicked(self):
        """
        获取新浪国际新闻
        """
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.sina_gj_content_list = []
        with open('sina_guoji.csv', 'r') as f:
            reader = csv.reader(f)
            # 去除csv第一行的内容
            i_count = 0
            for i in reader:
                if i_count != 0:
                    self.sina_gj_content_list.append(i)
                i_count += 1
            sina_gj_list = []
            for i in self.sina_gj_content_list:
                # 转化为heapnode
                sina_gj_node = HeapNode(i[1], i[0])
                sina_gj_list.append(sina_gj_node)

        # 定义新浪国际新闻的最大根堆
        self.sina_gj_heap = MaxHeap(i_count, sina_gj_list)
        # 建立最大根堆
        self.sina_gj_heap.buildHeap()
        # 取出时间最大(最新)的结点
        sina_gj_first = self.sina_gj_heap.deleteMax()
        self.sina_textBrowser.setText(unicode('-'+sina_gj_first.text))

        from threads import SinaGjThread
        self.sina_gjThread = SinaGjThread()
        self.sina_gjThread.start()
        print u"现在开始抓取新浪国际新闻！"

    @pyqtSignature("")
    def on_sina_sh_clicked(self):
        """
        获取新浪社会新闻
        """
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.sina_sh_content_list = []
        with open('sina_shehui.csv', 'r') as f:
            reader = csv.reader(f)
            # 去除csv第一行的内容
            i_count = 0
            for i in reader:
                if i_count != 0:
                    self.sina_sh_content_list.append(i)
                i_count += 1
            sina_sh_list = []
            for i in self.sina_sh_content_list:
                # 转化为heapnode
                print i
                sina_sh_node = HeapNode(i[1], i[0])
                sina_sh_list.append(sina_sh_node)

        # 定义新浪社会新闻的最大根堆
        self.sina_sh_heap = MaxHeap(i_count, sina_sh_list)
        # 建立最大根堆
        self.sina_sh_heap.buildHeap()
        # 取出时间最大(最新)的结点
        sina_sh_first = self.sina_sh_heap.deleteMax()
        self.sina_textBrowser.setText(unicode('*'+sina_sh_first.text))

        from threads import SinaShThread
        self.sina_shThread = SinaShThread()
        self.sina_shThread.start()
        print u"现在开始抓取新浪社会新闻！"
    
    @pyqtSignature("")
    def on_sina_pre_clicked(self):
        """
        保存感兴趣的新闻到桌面
        """
        with open('C:/Users/Administrator/Desktop/Note.txt', 'a') as f:
            f.write(self.sina_textBrowser.toPlainText())
    
    @pyqtSignature("")
    def on_sina_next_clicked(self):
        """
        获取当前主题的下一条新闻
        """
        print self.sina_textBrowser.toPlainText()
        if str(self.sina_textBrowser.toPlainText())[0] == '+':
            sina_next_node = self.sina_gn_heap.deleteMax()
            self.sina_textBrowser.setText('+'+unicode(sina_next_node.text))
            print "______________________________________________"
        if str(self.sina_textBrowser.toPlainText())[0] == '-':
            sina_next_node = self.sina_gj_heap.deleteMax()
            self.sina_textBrowser.setText('-'+unicode(sina_next_node.text))
            print "______________________________________________"
        if str(self.sina_textBrowser.toPlainText())[0] == '*':
            sina_next_node = self.sina_sh_heap.deleteMax()
            self.sina_textBrowser.setText('*' + unicode(sina_next_node.text))
            print "______________________________________________"

    @pyqtSignature("")
    def on_ghtt_send_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: 查找下一条评论
        p = self.ghtt_now_p
        if self.if_have_reply == True:
            if p.next != None:
                p = p.next
                self.ghtt_now_p = p
                replyList = p.data.split("!!wxw!!")
                self.ghtt_postedit.setText(unicode(replyList[0]) + "\n\n" + unicode(replyList[2]))
        else:
            pass
            # self.ghtt_postedit.setText(p.brother.next.next
            # raise NotImplementedError

    @pyqtSignature("")
    def on_ghtt_reset_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: 查找上一条评论
        p = self.ghtt_now_p
        if self.if_have_reply == True:
            if p != self.ghtt_now_h:
                p = p.pre
                self.ghtt_now_p = p
                replyList = p.data.split("!!wxw!!")
                self.ghtt_postedit.setText(unicode(replyList[0]) + "\n\n" + unicode(replyList[2]))
        else:
            pass

    @pyqtSignature("QString")
    def on_ghtt_combox1_activated(self, p0):
        """
        Slot documentation goes here.

        @param p0 DESCRIPTION
        @type QString
        """
        # TODO: not implemented yet
        self.ghtt_textbrowser1.setText(u"请检查网络是否通畅！")

    @pyqtSignature("")
    def on_ghtt_crawl_button_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        # 增量爬取观海听涛帖子
        ghclient = ghtt.AfterFirstCrawl()
        if 1:
            ghclient.crawlMore()
        else:
            pass
        with open('ghtt.csv', 'r') as f:
            reader_o = csv.reader(f)
            self.reader = map(lambda x: x, reader_o)
            # 将帖子读取并存入广义链表
            self.generalList = GeneralLinkedList()
            for i in self.reader:
                self.generalList.append(i[0])
                p = self.generalList.tail
                ph = TwoWayLinkedList()
                ph.append(p)
                p.brother = ph.head
                for j in i[1:]:
                    ph.append(j)
        p = self.generalList.tail
        for i in range(20):
            self.ghtt_combox1.addItem(unicode(str(p.brother.next.data)))
            p = p.pre

        self.connect(self.ghtt_combox1, QtCore.SIGNAL('activated(QString)'), self.onActivated)

    def onActivated(self, text):
        p = self.generalList.tail
        # 将标题对应的帖子文本找出并显示
        for i in range(20):
            if (unicode(str(p.brother.next.data)) == text):
                self.ghtt_textbrowser1.setText(
                    unicode(p.brother.next.next.data) + "\n" + unicode(p.brother.next.next.next.data +
                                                                       "\n\n" + unicode(
                        p.brother.next.next.next.next.data)))
                try:
                    self.ghtt_now_p = p.brother.next.next.next.next.next.next
                    self.ghtt_now_h = self.ghtt_now_p
                    replylist = p.brother.next.next.next.next.next.next.data.split("!!wxw!!")
                    self.ghtt_postedit.setText(unicode(replylist[0] + "\n\n" + unicode(replylist[2])))
                    self.if_have_reply = True
                except:
                    self.ghtt_postedit.setText(u"无回复")
                break
            else:
                p = p.pre
                # if unicode(str(i[1])) == text:

    @pyqtSignature("")
    def on_getweibo_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: 开一子线程，调用微博OAuth2.0接口读取最新微博
        from threads import WeiboWorkThread
        self.wbThread = WeiboWorkThread()
        self.wbThread.start()
        self.wbThread.finishSignal.connect(self.wbEnd)

    def wbEnd(self, weiboList):
        self.weiboList = weiboList
        self.weibo_p0 = self.weiboList.head
        self.weibo_author1 = self.weiboList.getValue(1)['nickname']
        self.weibo_text1 = self.weiboList.getValue(1)['text']
        self.weibo_desc1 = self.weiboList.getValue(1)['description']
        self.weibo_created_at = self.weiboList.getValue(1)['created_at']
        self.textEdit1.setText(
            self.weibo_author1 + "\n" + self.weibo_desc1 + "\n" + self.weibo_created_at + "\n" + self.weibo_text1)

    @pyqtSignature("")
    def on_getzhihu_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: 开一子线程，调用知乎0Auth2.0接口读取最新知乎
        from threads import ZhihuWorkThread
        self.zhThread = ZhihuWorkThread()
        self.zhThread.start()
        self.zhThread.finishSignal.connect(self.zhEnd)
        self.zhThread.clientSignal.connect(self.getZhihuClient)
        # self.textEdit2.setText(zhihu.Zhihu.getZhihuTrends())

    def zhEnd(self, zhihuList):
        self.zhihuList = zhihuList
        self.zhihu_p0 = self.zhihuList.head
        self.textEdit2.setText(self.zhihu_p0.data)
        self.zhihu_now_p = str(self.zhihuList.p0.data).split("---")[0]
        #  raise NotImplementedError

    @pyqtSignature("")
    def on_zhihu_relogin_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: 开一子窗口
        zhihuDialog = zhihu_login_dialog()
        zhihuDialog.show()
        zhihu_u_p = []
        zhihuDialog.exec_()
        if zhihuDialog.flag == 1:
            zhihu_u_p = zhihuDialog.getUsernamePassword()
            zhihuDialog.close()
        username = zhihu_u_p[0]
        password = zhihu_u_p[1]
        # 开一子线程，调用知乎0Auth2.0接口读取最新知乎
        from threads import ZhihuWorkThread2
        self.zhThread = ZhihuWorkThread2()
        self.zhThread.setUsername(username)
        self.zhThread.setPassword(password)
        try:
            self.zhThread.start()
        except:
            self.textEdit2.setText(u"账号或密码错误！请重新登录或用默认账号！")
            return False
        self.textEdit2.setText(u"正在登录中。。请稍等")
        self.textEdit_zhihu_user.setText(unicode(username))
        self.zhThread.finishSignal.connect(self.zhEnd)
        self.zhThread.nextSignal.connect(self.setZhihuName)
        # self.textEdit2.setText(zhihu.Zhihu.getZhihuTrends())
        # 判断是否是默认账号，从而获得不同的client
        self.zhThread.clientSignal.connect(self.getZhihuClient)

    def getZhihuClient(self, client):
        self.zhihu_client = client

    def setZhihuName(self, name):
        self.textEdit_zhihu_user.setText(unicode(str(name)))

    def zhEnd(self, zhihuList):
        self.zhihuList = zhihuList
        self.zhihu_p0 = self.zhihuList.head
        self.textEdit2.setText(self.zhihu_p0.data)
        #  raise NotImplementedError

    # 打开知乎回复评论的窗口
    @pyqtSignature("")
    def on_zhihu_reply_clicked(self):
        from pyzhihu_reply import ZhihuReply
        replyDialog = ZhihuReply()
        replyDialog.setZhihuClientPid(self.zhihu_client, self.zhihu_p0.ans)
        replyDialog.show()
        replyDialog.exec_()


    @pyqtSignature("")
    def on_p1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if (self.weibo_p0 != self.weiboList.head):
            self.weibo_p0 = self.weibo_p0.pre
            self.weibo_author1 = self.weibo_p0.data['nickname']
            self.weibo_text1 = self.weibo_p0.data['text']
            self.weibo_desc1 = self.weibo_p0.data['description']
            self.weibo_created_at = self.weibo_p0.data['created_at']
            self.textEdit1.setText(
                self.weibo_author1 + "\n" + self.weibo_desc1 + "\n" + self.weibo_created_at + "\n" + self.weibo_text1)
        else:
            pass


            # raise NotImplementedError

    @pyqtSignature("")
    def on_p2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if (self.zhihu_p0 != self.zhihuList.head):
            self.zhihu_p0 = self.zhihu_p0.pre
            self.zhihu_now_p = str(self.zhihu_p0.data).split("---")[0]
            self.textEdit2.setText(self.zhihu_p0.data)
        else:
            pass
            # raise NotImplementedError

    @pyqtSignature("")
    def on_n1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if (self.weibo_p0 != self.weiboList.tail):
            self.weibo_p0 = self.weibo_p0.next
            self.weibo_author1 = self.weibo_p0.data['nickname']
            self.weibo_text1 = self.weibo_p0.data['text']
            self.weibo_desc1 = self.weibo_p0.data['description']
            self.weibo_created_at = self.weibo_p0.data['created_at']
            self.textEdit1.setText(
                self.weibo_author1 + "\n" + self.weibo_desc1 + "\n" + self.weibo_created_at + "\n" + self.weibo_text1)
        else:
            pass
            # raise NotImplementedError

    @pyqtSignature("")
    def on_n2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if (self.zhihu_p0 != self.zhihuList.tail):
            self.zhihu_p0 = self.zhihu_p0.next
            self.zhihu_now_p = str(self.zhihu_p0.data).split("---")[0]
            self.textEdit2.setText(self.zhihu_p0.data)
        else:
            pass


class WebView(QWebView):
    def __init__(self):
        super(WebView, self).__init__()
        global url
        self.load(url)
        self.setWindowTitle(u"新闻连连看")
        self.page().setLinkDelegationPolicy(QWebPage.DelegateAllLinks)
        self.page().linkClicked.connect(self.linkClicked)
        self.show()

    def linkClicked(self, url):
        self.load(url)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dig = TabWidget3()
    dig.show()
    sys.exit(app.exec_())