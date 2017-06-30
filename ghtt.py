# coding=utf-8
from __future__ import unicode_literals, print_function
import csv
import Queue
import threading
import requests
from bs4 import BeautifulSoup
import time

ghtt_headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'IQsk_19c0_nofavfid=1; IQsk_19c0_saltkey=s2jzcZ19; IQsk_19c0_lastvisit=1486630002; IQsk_19c0_client_created=1486802457; IQsk_19c0_client_token=59FAF31F554D649F2DACDEFC11FBC788; IQsk_19c0_auth=2669AmqxiW7BMFB%2FGL8LUiGZt8UXGsV0g%2BoDQ%2BV29kcSXsPJy3xOKXnk40VSwbNILDGSBAQscZ2e1WwgwhEJ6MxGqVk; IQsk_19c0_connect_login=1; IQsk_19c0_connect_uin=59FAF31F554D649F2DACDEFC11FBC788; IQsk_19c0_ulastactivity=b6cblm9hDI09VowIKi1e2TyGirE3CC7zXCZcY6Woy2xeGqUSWdva; pgv_pvi=8413941535; pgv_info=ssi=s9821747182; CNZZDATA1252993724=669560946-1458134158-http%253A%252F%252Fwww.so.com%252F%7C1487144575; IQsk_19c0_smile=1D1; IQsk_19c0_home_diymode=1; IQsk_19c0_pvi=1694583033; IQsk_19c0_si=s2049309081; IQsk_19c0_clearUserdata=forum; IQsk_19c0_creditnotice=0D1D0D0D0D0D0D0D0D201522; IQsk_19c0_creditbase=0D536D0D0D0D0D0D0D0; IQsk_19c0_creditrule=%E5%8F%91%E8%A1%A8%E5%9B%9E%E5%A4%8D; IQsk_19c0_lip=172.29.153.254%2C1487148504; IQsk_19c0_st_t=201522%7C1487151552%7Cfcccdb0fbd88a106b0cbe9d7e71f66a3; IQsk_19c0_forum_lastvisit=D_103_1486802288D_1_1487146510D_183_1487147459D_93_1487151552; IQsk_19c0_visitedfid=93D183D1D136D135; IQsk_19c0_cr180_swap_cookiefid=93D183D1; IQsk_19c0_lastact=1487151554%09forum.php%09viewthread; IQsk_19c0_connect_is_bind=1; IQsk_19c0_st_p=201522%7C1487151554%7C1191447cf7defc032b1b769a255fd19d; IQsk_19c0_viewid=tid_2045495; IQsk_19c0_cr180_swap_cookietid=2045495D2045104D2045500D2045518D2045070D2043538; IQsk_19c0_sid=kSZ243',
'Host':'bbs.ghtt.net',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
}
ghtt_headers1 = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'102',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'IQsk_19c0_nofavfid=1; IQsk_19c0_saltkey=s2jzcZ19; IQsk_19c0_lastvisit=1486630002; IQsk_19c0_client_created=1486802457; IQsk_19c0_client_token=59FAF31F554D649F2DACDEFC11FBC788; IQsk_19c0_auth=2669AmqxiW7BMFB%2FGL8LUiGZt8UXGsV0g%2BoDQ%2BV29kcSXsPJy3xOKXnk40VSwbNILDGSBAQscZ2e1WwgwhEJ6MxGqVk; IQsk_19c0_connect_login=1; IQsk_19c0_connect_uin=59FAF31F554D649F2DACDEFC11FBC788; IQsk_19c0_lip=117.136.95.239%2C1487129052; IQsk_19c0_onlineusernum=311; IQsk_19c0_ulastactivity=b6cblm9hDI09VowIKi1e2TyGirE3CC7zXCZcY6Woy2xeGqUSWdva; IQsk_19c0_sendmail=1; tjpctrl=1487147538630; IQsk_19c0_noticeTitle=1; pgv_pvi=8413941535; pgv_info=ssi=s9821747182; CNZZDATA1252993724=669560946-1458134158-http%253A%252F%252Fwww.so.com%252F%7C1487144575; IQsk_19c0_smile=1D1; IQsk_19c0_home_diymode=1; IQsk_19c0_pvi=1694583033; IQsk_19c0_si=s2049309081; IQsk_19c0_st_t=201522%7C1487145595%7C2d3072268449a785a1b73bbf0f7ebbe8; IQsk_19c0_forum_lastvisit=D_103_1486802288D_1_1486820788D_93_1487145595; IQsk_19c0_visitedfid=93D136D1D135D103; IQsk_19c0_cr180_swap_cookiefid=93; IQsk_19c0_lastact=1487145598%09forum.php%09viewthread; IQsk_19c0_connect_is_bind=1; IQsk_19c0_st_p=201522%7C1487145598%7Ca97d19c65561372b3ecea552d05a24f1; IQsk_19c0_viewid=tid_2045518; IQsk_19c0_cr180_swap_cookietid=2045518; IQsk_19c0_sid=GDHWwD',
'Host':'bbs.ghtt.net',
'Origin':'http://bbs.ghtt.net',
'Referer':'http://bbs.ghtt.net/forum.php?mod=viewthread&tid=2045518&mobile=1',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
}

ghtt_post_url_module = 'http://bbs.ghtt.net/forum.php?mod=post&action=reply&fid=93&tid=2045518&extra=&replysubmit=yes&mobile=yes'

ghtt_post_data = {
'formhash':'fe5f3e70',
'message':u'泰山吼啊！',
'replysubmit':'回复'
}


class CrawlGhttPage(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global queue_viewHref, mutex_href_get, mutex_href_put
        # 若在while外增加acquire() 编译器莫名其妙地认为没有acquire(), 导致下面release()时报错：unlocked
        # mutex_href_get.acquire()
        while queue_viewHref.qsize() > 0:
            # 在任务队列中取得帖子链接和序号
            mutex_href_get.acquire()
            v_and_n = queue_viewHref.get()
            viewHref = v_and_n.split("wxw")[0]
            number = v_and_n.split("wxw")[1]
            mutex_href_get.release()

            result = self.get_page(viewHref, number)

            try:
                mutex_href_put.acquire()
                if str(type(result)) == "<type 'list'>":
                    print(str(type(result)))
                    with open('ghtt.csv', 'ab+') as f:
                        writer = csv.writer(f)
                        writer.writerow(result)
                else:
                    with open('ghtt_notfound.txt', 'a') as f:
                        f.write(viewHref+"\n")
            except:
                print("unexpected error raise!")
            finally:
                mutex_href_put.release()
       # mutex_href_get.release()


    def get_page(self, viewHref, uid):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        try:
            print(222)
            response = requests.get(viewHref, headers=ghtt_headers, timeout=5).content
            print(222)
        except:
            return -1
     #   time.sleep(1)
        soup = BeautifulSoup(response, 'lxml', from_encoding='utf-8')
        # 若没有此属性的标签则页面不存在
        if not soup.find(attrs={'class': 'cr180_title'}):
            return -2
        else:
            page_title = soup.find(attrs={"class": "cr180_title"}).get_text().strip()
            page_author = soup.find(attrs={"class": "z cr180_member_jon"}).a.get_text()
            page_time = soup.find(attrs={"class": "dateline"}).get_text()
            page_content = soup.find(attrs={"class": "postmessage"}).get_text()
        print(page_title)
        print(viewHref)
        result_list = []
        result_list.append(str(uid))
        result_list.append(page_title)
        result_list.append(page_author)
        result_list.append(page_time)
        result_list.append(page_content)
        result_list.append(viewHref)

        # 获取回帖
        if len(soup.findAll(attrs={'class': 'z cr180_member_jon'})) > 1:
            page_author_list = soup.findAll(attrs={"class": 'z cr180_member_jon'})[1:]
            page_time_list = soup.findAll(attrs={"class": 'dateline'})[1:]
            page_content_list = soup.findAll(attrs={"class": "postmessage"})[1:]
            for i, j, k in zip(page_author_list, page_time_list, page_content_list):
                result_list.append(i.get_text()+"!!wxw!!"+j.get_text()+"!!wxw!!"+k.get_text())

        # result_dict = {
        #     'uid': uid,
        #     'page_title': page_title,
        #     'page_author' : page_author,
        #     'page_time': page_time,
        #     'page_content': page_content
        # }
        return result_list


def start_crawl_ghtt(latest='2050000', add_=1):
    # 链接队列、得到链接的锁、给于链接的锁
    global queue_viewHref, mutex_href_get, mutex_href_put
    # 任务队列
    queue_viewHref = Queue.Queue()
    threads = []
    spiderUrl = 'http://bbs.ghtt.net/forum.php?mod=viewthread&mobile=1&tid='

    target = int(latest) + add_
    num = 2
    mutex_href_get = threading.Lock()
    mutex_href_put = threading.Lock()

    for i in range(int(latest), int(target)):
        viewHref = spiderUrl + str(i)
        # 将帖子链接和序号同时放入队列
        queue_viewHref.put(viewHref+"wxw"+str(i))

    for i in xrange(0, num):
        print(1111)
        threads.append(CrawlGhttPage())

    for thread in threads:
        print(1111)
        thread.start()

    for thread in threads:
        thread.join()


# 归并排序 分治法
def mergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int( len(lists)/2 )
    left = mergeSort(lists[:num])
    right = mergeSort(lists[num:])
    return merge(left, right)


def merge(left, right):
    r, l = 0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l][0] < right[r][0]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += right[r:]
    result += left[l:]
    return result


class AfterFirstCrawl(object):
    def __init__(self):
        pass

    def sortAllP(self):
        with open('ghtt.csv', 'r') as f:
            reader_o = csv.reader(f)
            reader = []
            for i in reader_o:
                reader.append(i)
            reader = reader[1:]
        reader = mergeSort(reader)
        with open('ghtt.csv', 'wb+') as f:
            writer = csv.writer(f)
            for i in reader:
                writer.writerow(i)

    # def shellInsert(self, knuth):
    #     for i in range(knuth, self.length+1, knuth):
    #         if self.reader[i]
    #

    # def shellSort(self):
    #     with open('ghtt.csv', 'r') as f:
    #         self.reader = csv.reader(f)
    #     # Knuth提出的步长序列方便选取，且效率较高
    #     knuth = 0
    #     self.length = len(self.reader)
    #     dlta = []
    #     while knuth<=self.length/3:
    #         knuth = knuth*3+1
    #         dlta.append(knuth)
    #     dlta.reverse()
    #     for knuth in dlta:
    #         self.shellInsert(knuth)

    def crawlMore(self):
        add_ = 100
        if add_ == 0:
            return
        with open('ghtt.csv', 'r') as f:
            reader_o = csv.reader(f)
            reader = []
            # 函数式编程
            reader = map(lambda x: x, reader_o)
            latest = str(int(reader[-1][0]) + 1)
        start_crawl_ghtt(latest, add_)
        self.sortAllP()

if __name__ == '__main__':
   # start_crawl_ghtt('2040000', 5500)
   # a = AfterFirstCrawl()
    #a.crawlMore()
    pass