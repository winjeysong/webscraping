'''this is a test'''
import urllib2
try:
    RESPONSE = urllib2.urlopen('http://bbs.csdn.net/why')
except urllib2.HTTPError, error:
    print error.code
