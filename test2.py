''' a test file '''
import urllib2
import cookielib
COOKIE = cookielib.CookieJar()
OPENER = urllib2.build_opener(urllib2.HTTPCookieProcessor(COOKIE))
RESPONSE = OPENER.open('http://www.baidu.com')
for item in COOKIE:
    print 'name = '+item.name
    print 'value ='+item.value
