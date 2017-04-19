# _*_ coding:utf-8 _*_
import urllib2
import string
import re

# ------ 处理页面标签 -------


class HTMLDeal:
    # -- 以下都为非贪婪模式 --

    # 匹配 \t 或 \n 或 空格 或 超链接 或 图片
    re_start_ele = re.compile("(\t|\n| |<a.*?>|<img.*?>)")

    # 匹配任意标签
    re_end_ele = re.compile("<.*?>")

    # 匹配任意p标签
    re_para_tag = re.compile("<p.*?>")

    # 匹配换行元素
    re_next_line = re.compile("(<br/>|</p>|<tr>|<div>|</div>|<br>+?)")

    # 匹配制表符元素
    re_next_tab = re.compile("<td>")

    # 将html中的实体字符转为原始符号
    replace_tag = [('&lt;','<'),('&gt;','>'),('&amp','&'),('&quot;','\''),('&nbsp;',' ')]

    def replace_ele(self, my_str):
        my_str = self.re_start_ele.sub("", my_str)
        my_str = self.re_para_tag.sub("\n   ", my_str)
        my_str = self.re_next_line.sub("\n" ,my_str)
        my_str = self.re_next_tab.sub("\t", my_str)
        my_str = self.re_end_ele.sub("", my_str)

        for symbol in self.replace_tag:
            my_str = my_str.replace(symbol[0], symbol[1])

        return my_str

# ------ 结束标签处理 ------

# ------ 开始抓取页面 ------


class WebScrap:
    # 声明属性
    def __init__(self, url):
        self.my_url = url + '?see_lz=1'
        self.my_data = []
        self.my_deal = HTMLDeal()
        print u'已启动贴吧爬虫...'

    # 加载页面并转码存储
    def tieba(self):
        # 加载整个页面并将其从utf-8转码
        my_page = urllib2.urlopen(self.my_url).read().decode("utf-8")
        # 计算总共页数
        total_page = self.page_counter(my_page)
        # 获取标题
        my_title = self.get_title(my_page)
        print u'文章名称：' + my_title
        # 存储所需数据
        self.save_data(self.my_url, my_title, total_page)

    # 总页数计算
    def page_counter(self, my_page):
        # 匹配"共有<span class="red">x页</span>"来获取总页数
        my_match = re.search(r'class="red">(\d+?)</span>', my_page, re.S)
        if my_match:
            total_page = int(my_match.group(1))
            print u'发现共有%d页内容' % total_page
        else:
            total_page = 0
            print u'未发现内容'
        return total_page

    # 找出标题
    def get_title(self, my_page):
        # 匹配标题<h3 class="core_title_txt" title="xxx">...</h3>
        my_match = re.search(r'<h3.*?>(.*?)</h3>', my_page, re.S)
        my_title = u'暂无标题'
        if my_match:
            my_title = my_match.group(1)
        else:
            print u'无法加载标题'

        # 去除文件名中不能含有的符号(/ \ : * ? " < >)
        my_title = re.sub(r'[/:*?"<>|\\]', '', my_title)
        return my_title

    # 存储数据
    def save_data(self, url, my_title, total_page):
        # 将页面数据载入列表中
        self.get_data(url, total_page)
        # 打开本地文件并写入
        f = open(my_title+'.txt', 'w+')
        f.writelines(self.my_data)
        f.close()
        print u'数据已下载并存为文件'
        print u'按任意键结束'
        raw_input();

    # 获取页面源码并将其存储到列表中
    def get_data(self, url, total_page):
        url = url + '&pn='
        for i in range(1,total_page+1):
            print u'正在加载第%d页' % i
            my_page = urllib2.urlopen(url + str(i)).read()
            # 将my_page中的html代码处理并存储到my_data中
            self.deal_data(my_page.decode('utf-8'))

    # 将所需内容从html中匹配提取出来
    def deal_data(self, my_page):
        my_content = re.findall('id="post_content.*?>(.*?)</div>', my_page, re.S)
        for content in my_content:
            data = self.my_deal.replace_ele(content.replace('\n','').encode('utf-8'))
            self.my_data.append(data + '\n')

# ------ 结束页面抓取 ------

# ------ 开始处理 ------
print u'输入贴吧地址最后的数字串'
tieba_url = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))

my_scrap = WebScrap(tieba_url)
my_scrap.tieba()
