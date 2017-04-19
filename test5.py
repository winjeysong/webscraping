# _*_ coding: utf-8 _*_
import string,urllib2

# 定义贴吧获取函数
def tieba(url, firstpage, lastpage):
    for i in range(firstpage, lastpage):
        strName = string.zfill(i,5) + '.html'
        print '正在下载第' + str(i) + '个网页，并将其存储为' + strName + '...'
        f = open(strName, 'w+')
        m = urllib2.urlopen(url + str(i)).read()
        f.write(m)
        f.close()

# 输入参数
tiebaURL = str(raw_input('输入贴吧地址，去掉pn=后面的数字：\n'))
firstPage = int(raw_input('输入开始页数：\n'))
lastPage = int(raw_input('输入结束页数：\n'))

# 调用函数
tieba(tiebaURL, firstPage, lastPage)
