# coding:utf-8
from PyQt4 import QtCore, QtGui
from data_structure import *
import weibo
import time
import os
from zhihu_oauth import ZhihuClient
import requests
from bs4 import BeautifulSoup
import csv
import lxml


APP_KEY = '3175988140'
APP_SECRET = 'f445636b8fc0b7b5e75474c3ab8d320b'
CALL_BACK = 'http://api.weibo.com/oauth2/default.html'
ACCESS_TOKEN = '2.00xUU4VGKbHw9D47e3cfc2c8UhoSBB'



TOKEN_FILE = 'token.pkl'
TOKEN_FILE2 = 'token2.pkl'


class myAPIClient(weibo.APIClient):
    """
    微博提供的接口类
    """
    def __init__(self, app_key, app_secret, redirect_uri, access_token):
        weibo.APIClient.__init__(self, app_key, app_secret, redirect_uri, access_token)
       # super(myAPIClient(self))

    def request_access_token_info(self, access_token):
        r = weibo._http_post('%s%s' % (self.auth_url, 'get_token_info'), access_token=access_token)
        current = int(time.time())
        expires = r.expire_in + current
        return weibo.JsonDict(expires_in=expires)


class WeiboWorkThread(QtCore.QThread):
    """
    获取最新微博
    避免UI界面卡死，另开一工作线程处理
    """
    # 不能放在__init__中 具体原因不明
    # 需指定返回的类型
    finishSignal = QtCore.pyqtSignal(TwoWayLinkedList)
    def __init__(self, parent=None):
        super(WeiboWorkThread, self).__init__(parent)

    # 默认调用run方法
    def run(self):
        self.startCollecte()
        # 结束后发送一个信号告诉主线程窗口
        self.finishSignal.emit(self.weiboList)

    def get_client(self, appkey, appsecret, callback, access_token):
        client = myAPIClient(appkey, appsecret, callback, access_token)
        r = client.request_access_token_info(access_token)
        expires_in = r.expires_in
        client.set_access_token(access_token, expires_in)
        return client

    def run2(self, weiboList, client):
        # 获取公共微博，一次约20条
        statuses = client.statuses__public_timeline()['statuses']
        length = len(statuses)
        print('现在获得了' + str(length) + '条新微博')

        for i in range(0, length):
            created_at = statuses[i]['created_at']
            id = statuses[i]['user']['id']
            province = statuses[i]['user']['province']
            city = statuses[i]['user']['city']
            followers_count = statuses[i]['user']['followers_count']
            friends_count = statuses[i]['user']['friends_count']
            statuses_count = statuses[i]['user']['statuses_count']
            url = statuses[i]['user']['url']
            geo = statuses[i]['geo']
            comments_count = statuses[i]['comments_count']
            reposts_count = statuses[i]['reposts_count']
            nickname = statuses[i]['user']['screen_name']
            desc = statuses[i]['user']['description']
            location = statuses[i]['user']['location']
            text = statuses[i]['text']

            weibo_dict = {
                'created_at': created_at,
                'id': id,
                'nickname': nickname,
                'text': text,
                'province': province,
                'location': location,
                'description': desc,
                'city': city,
                'followers_count': followers_count,
                'friends_count': friends_count,
                'statuses_count': statuses_count,
                'url': url,
                'geo': geo,
                'comments_count': comments_count,
                'reposts_count': reposts_count
            }
            weiboList.append(weibo_dict)
        return weiboList

    def startCollecte(self, count_=-1):
        self.weiboList = TwoWayLinkedList()
        client = self.get_client(APP_KEY, APP_SECRET, CALL_BACK, ACCESS_TOKEN)
        while True:
            print('ddddddddddd')
            if 1:
                self.weiboList = self.run2(self.weiboList, client)
                return self.weiboList
            else:
                time.sleep(0.1)
                # 默认循环无数次，直到获得成功为止
                # 可通过更改参数count_的值来改变循环次数
                if (count_ != 0):
                    count_ = count_ - 1
                else:
                    break


class ZhihuWorkThread(QtCore.QThread):
    """
    获取最新知乎答案
    避免UI界面卡死，另开一工作线程处理
    """
    # 不能放在__init__中 具体原因不明
    # 需指定返回的类型
    finishSignal = QtCore.pyqtSignal(TwoWayLinkedList)
    from zhihu_oauth import zhcls
    clientSignal = QtCore.pyqtSignal(zhcls.me.Me)
    def __init__(self, parent=None):
        super(ZhihuWorkThread, self).__init__(parent)

    def run(self):
        self.getZhihuTrends()
        self.finishSignal.emit(self.zhihuList)

    def get_client(self, reset_=0):
        client = ZhihuClient()
        if reset_ != 0:
            client.login_in_terminal()
            client.save_token(TOKEN_FILE)
        if os.path.isfile(TOKEN_FILE):
            client.load_token(TOKEN_FILE)
        else:
            client.login_in_terminal()
            client.save_token(TOKEN_FILE)
        return client

    def getZhihuTrends(self):
        self.zhihuList = TwoWayLinkedList()

        client = self.get_client()
        me = client.me()
       ## maqianzu = client.people(u'ling-jian-94')
       # for ans, count in zip(maqianzu.answers, range(6)):
        #    self.zhihuList.append(ans.content)
        keaimou = client.people(u'ke-ai-mou')
        self.clientSignal.emit(me)
        for ans, count in zip(keaimou.answers, range(3)):
            self.zhihuList.append(str(ans.id)+"---"+ans.content, ans)

        print(self.zhihuList.getValue(2))


class ZhihuWorkThread2(QtCore.QThread):
    """
    获取最新知乎答案
    避免UI界面卡死，另开一工作线程处理
    """
    # 不能放在__init__中 具体原因不明
    # 需指定返回的类型
    finishSignal = QtCore.pyqtSignal(TwoWayLinkedList)
    nextSignal = QtCore.pyqtSignal(str)
    from zhihu_oauth import zhcls
    clientSignal = QtCore.pyqtSignal(zhcls.me.Me)
    def __init__(self, parent=None):
        super(ZhihuWorkThread2, self).__init__(parent)
        self.username = ""
        self.password = ""
        self.name = ""

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def run(self):
        if self.username and self.password:
            self.getZhihuTrends()
            self.finishSignal.emit(self.zhihuList)
            self.nextSignal.emit(self.name)
        else:
            print u"没有填写完整登录信息！"

    def get_client(self, reset_=1):
        client = zhihu_oauth.ZhihuClient()
        # if reset_ != 0:
        #     client.login_in_terminal(username=self.username, password=self.password)
        #     client.save_token(TOKEN_FILE2)
        if os.path.isfile(TOKEN_FILE):
            client.load_token(TOKEN_FILE2)
        else:
            client.login_in_terminal(client.login_in_terminal(username=self.username, password=self.password))
            client.save_token(TOKEN_FILE2)
        print type(client)
        return client

    def getZhihuTrends(self):
        self.zhihuList = TwoWayLinkedList()
        client = self.get_client()
        me = client.me()
        print 'name :'+str(me.name)
        self.name = unicode(str(me.name))

        followings_list = []
        for man in me.followings:
             followings_list.append(man.id)
        if len(followings_list)>2:
             followings_list = followings_list[:2]
        self.zhihuList = TwoWayLinkedList()
        for man_id in followings_list:
             man = client.people(man_id)
             for ans, count in zip(man.answers, range(3)):
                 self.zhihuList.append(str(ans.id)+"---"+ans.content, ans)

        self.clientSignal.emit(me)
        # maqianzu = client.people(u'ling-jian-94')
        # for ans, count in zip(maqianzu.answers, range(6)):
        #     self.zhihuList.append(ans.content)
        # keaimou = client.people(u'ke-ai-mou')
        # for ans, count in zip(keaimou.answers, range(3)):
        #     self.zhihuList.append(ans.content)

        print(self.zhihuList.getValue(2))



class SinaGnThread(QtCore.QThread):
    """
    获取最新新浪新闻
    避免UI界面卡死，另开一工作线程处理
    """
    def __init__(self, parent=None):
        super(SinaGnThread, self).__init__(parent)
        self.hrefList = []

    def run(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        try:
            a = requests.get('http://roll.news.sina.com.cn/news/gnxw/gdxw1/index.shtml', timeout=3).content
            a = BeautifulSoup(a, "lxml")
        except:
            print u'目录获取失败'
            return
        href_list = a.findAll(attrs={'class': "list_009"})[0].findAll('li')
        for i in href_list:
            href = i.a.attrs['href']
            self.hrefList.append(href)
        for i in self.hrefList[:5]:
            try:
                b = requests.get(i, timeout=3).content
            except:
                print u'网页新闻获取失败'
                continue
            b = BeautifulSoup(b, "lxml")
            page_time = b.find(attrs={'id': 'navtimeSource'}).contents[0].strip()
            page_content = b.find(attrs={'id': 'artibody'}).get_text()

            year = page_time.split('年')
            month = year[1].split('月')
            day = month[1].split('日')
            hour = day[1].split(':')[0]
            minute = day[1].split(':')[1]
            year = year[0]
            month = month[0]
            day = day[0]
            #  print year, month, day, hour, minute
            page_time = str(year+month+day+hour+minute)
            print page_time

            page_list = []
            page_list.append(page_content)
            page_list.append(page_time)

            time_set = set()
            with open('sina_guonei.csv', 'r') as f:
                reader = csv.reader(f)
                for line in reader:
                    try:
                        time_set.add(line[1])
                    except:
                        pass
            if page_time not in time_set:
                with open('sina_guonei.csv', 'ab+') as f:
                    writer = csv.writer(f)
                    writer.writerow(page_list)
            else:
                print u"该新闻已被爬取！"


class SinaGjThread(QtCore.QThread):
    """
    获取最新新浪国际类新闻
    避免UI界面卡死，另开一工作线程处理
    """
    def __init__(self, parent=None):
        super(SinaGjThread, self).__init__(parent)
        self.hrefList = []

    def run(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        try:
            a = requests.get('http://roll.news.sina.com.cn/news/gjxw/gjmtjj/index.shtml', timeout=3).content
            a = BeautifulSoup(a, "lxml")
        except:
            print u'目录获取失败'
            return
        href_list = a.findAll(attrs={'class': "list_009"})[0].findAll('li')
        for i in href_list:
            href = i.a.attrs['href']
            self.hrefList.append(href)
        for i in self.hrefList[:5]:
            try:
                b = requests.get(i, timeout=3).content
            except:
                print u'网页新闻获取失败'
                continue
            b = BeautifulSoup(b, "lxml")

            page_time = b.find(attrs={'id': 'navtimeSource'}).contents[0].strip()
            page_content = b.find(attrs={'id': 'artibody'}).get_text()
            year = page_time.split('年')
            month = year[1].split('月')
            day = month[1].split('日')
            hour = day[1].split(':')[0]
            minute = day[1].split(':')[1]
            year = year[0]
            month = month[0]
            day = day[0]
            # print year, month, day, hour, minute
            page_time = str(year+month+day+hour+minute)
            print page_time
            page_list = []
            page_list.append(page_content)
            page_list.append(page_time)

            time_set = set()
            with open('sina_guoji.csv', 'r') as f:
                reader = csv.reader(f)
                for line in reader:
                    try:
                        time_set.add(line[1])
                    except:
                        pass
            if page_time not in time_set:
                with open('sina_guoji.csv', 'ab+') as f:
                    writer = csv.writer(f)
                    writer.writerow(page_list)
            else:
                print u"该新闻已被爬取！"


class SinaShThread(QtCore.QThread):
    """
    获取最新新浪社会类新闻
    避免UI界面卡死，另开一工作线程处理
    """
    def __init__(self, parent=None):
        super(SinaShThread, self).__init__(parent)
        self.hrefList = []

    def run(self):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        try:
            a = requests.get('http://roll.news.sina.com.cn/news/shxw/qwys/index.shtml', timeout=3).content
            a = BeautifulSoup(a, "lxml")
        except:
            print u'目录获取失败'
            return
        href_list = a.findAll(attrs={'class': "list_009"})[0].findAll('li')
        for i in href_list:
            href = i.a.attrs['href']
            self.hrefList.append(href)
        for i in self.hrefList[:5]:
            try:
                b = requests.get(i, timeout=3).content
            except:
                print u'网页新闻获取失败'
                continue
            b = BeautifulSoup(b, "lxml")
            page_time = b.find(attrs={'id': 'navtimeSource'}).contents[0].strip()
            page_content = b.findAll(attrs={'id': 'artibody'})[-1].get_text().strip()
            print type(page_content)
            year = page_time.split('年')
            month = year[1].split('月')
            day = month[1].split('日')
            hour = day[1].split(':')[0]
            minute = day[1].split(':')[1]
            year = year[0]
            month = month[0]
            day = day[0]
            print year, month, day, hour, minute
            page_time = str(year+month+day+hour+minute)
            print page_time

            page_list = []
            page_list.append(page_content)
            page_list.append(page_time)

            time_set = set()
            with open('sina_shehui.csv', 'r') as f:
                reader = csv.reader(f)
                for line in reader:
                    try:
                        time_set.add(line[1])
                    except:
                        pass
            if page_time not in time_set:
                print u"找到了新新闻"
                with open('sina_shehui.csv', 'ab+') as f:
                    writer = csv.writer(f)
                    writer.writerow(page_list)
            else:
                print str(page_time) + u"该新闻已被爬取！"