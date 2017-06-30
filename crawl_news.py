# -*- coding:utf-8 -*-
from __future__ import unicode_literals, print_function
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
reload(sys)
#sys.setDefaultEncoding('utf-8')
#reload(sys)
import requests
from bs4 import BeautifulSoup

headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'ALLYESID4=0D64B77A3D4766E7; Hm_lvt_d130ad2e0466d0dbb676e389eb463ef5=1486979906; Hm_lpvt_d130ad2e0466d0dbb676e389eb463ef5=1486979906',
'Host':'district.ce.cn',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'
}

if __name__ == "__main__":
    page = requests.get('http://district.ce.cn/zt/friend-link/', headers=headers).content
    page = BeautifulSoup(page, "lxml", from_encoding='utf-8')
    print(str(page))
    province_list = page.findAll(attrs={"class": "tou"})
    for i in range(len(province_list)):
        province_list[i] = province_list[i].get_text()
        print(province_list[i])
    province_number = len(province_list)
    print(len(province_list))
    module_list = page.findAll('ul', attrs={'class': 'list'})
    count = 0
    # zhengfu_name_list = []
    # xinwen_name_list = []
    # dangbao_name_list = []
    # wanbao_name_list = []
    with open('bstree.txt','a') as f:
        for i in province_list:
            f.write(i.strip()+"!!!")
        f.write("\n")
    with open("bstree.txt", "a") as f:
        for i in range(31):
            f.write("政府网站!!!新闻网站!!!党报网站!!!晚报网站" + "\n")
    while True:
        if count/4>=31:
            break
        # 政府网站
        zf_list = module_list[count].findAll('li')
        with open("bstree.txt", "a") as f:
            f.write("#")
        for i in zf_list:
            with open("bstree.txt", "a") as f:
                f.write(i.get_text().strip()+"---"+i.a.attrs['href']+"!!!")
        with open("bstree.txt", "a") as f:
            f.write("\n")
            f.write("#")
        # 新闻网站
        zf_list = module_list[count+1].findAll('li')
        for i in zf_list:
            with open("bstree.txt", "a") as f:
                f.write(i.get_text().strip()+"---"+i.a.attrs['href']+"!!!")
        with open("bstree.txt", "a") as f:
            f.write("\n")
            f.write("#")
        # 党报网站
        zf_list = module_list[count+2].findAll('li')
        for i in zf_list:
            with open("bstree.txt", "a") as f:
                f.write(i.get_text().strip()+"---"+i.a.attrs['href']+"!!!")
        with open("bstree.txt", "a") as f:
            f.write("\n")
            f.write("#")
        # 晚报网站
        zf_list = module_list[count+3].findAll('li')
        for i in zf_list:
            with open("bstree.txt", "a") as f:
                f.write(i.get_text().strip()+"---"+i.a.attrs['href']+"!!!")
        with open("bstree.txt", "a") as f:
            f.write("\n")
        count = count + 4

