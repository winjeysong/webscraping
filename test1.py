''' a test file '''
import urllib2
RESPONSE = urllib2.urlopen('http://www.baidu.com')
HTML = RESPONSE.read()
print HTML
