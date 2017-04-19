# _*_ coding:utf-8 _*_

import urllib2
import re
import thread
import time

# 加载处理糗事百科


class DataScrap:

    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    # 爬取段子，添加到列表中并返回列表
    def get_clip(self, page):
        my_url = "http://m.qiushibaike.com/hot/page/"+ page
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        req = urllib2.Request(my_url, headers=headers)
        my_response = urllib2.urlopen(req)
        my_page = my_response.read()

        unicode_page = my_page.decode("utf-8")

        # 爬取div中的content类
        # re.S是任意匹配模式，可以匹配换行符
        my_items = re.findall('<div.*?class="content">\n+<span>(.*?)</span>\n+</div>', unicode_page, re.S)
        return my_items

    # 加载新段子
    def load_clip(self):
        # 如果未输入quit则一直执行
        while self.enable:
            # 如果pages数组中的内容少于2
            if len(self.pages) < 2:
                try:
                    # 获取新页面的段子
                    my_page = self.get_clip(str(self.page))
                    self.page += 1
                    self.pages.append(my_page)
                except:
                    print '无法链接'
            else:
                time.sleep(5)

    def show_clip(self, cur_page, page):
        i = 0
        for i in range(0, len(cur_page)):
            if i < len(cur_page):
                clip = "\n\n" + cur_page[i].replace("\n","").replace("<br/>","\n") + "\n\n"
                print u'第%d页，第%d个故事' % (page, i+1) , clip
                i += 1
            else:
                break

        input = str(raw_input(u'回车看下一页内容，输入quit退出。\n'))
        if input == "quit":
            self.enable = False

    def start(self):
        self.enable = True
        page = self.page
        print u'正在加载中请稍后...'

        # 新建一个线程在后台加载段子并存储
        thread.start_new_thread(self.load_clip,())

        # 加载处理
        while self.enable:
            # 如果self的page数组中存有元素
            if self.pages:
                cur_page = self.pages[0]
                del self.pages[0]
                self.show_clip(cur_page, page)
                page += 1

# ---------界面部分--------
print u'请按下回车浏览今日内容'
raw_input(" ")
run_clip = DataScrap()
run_clip.start()
