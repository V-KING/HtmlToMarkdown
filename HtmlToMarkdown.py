#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
from webgrab import MyHTMLParser
from getPageLinks import HtmlLink
import sys
import re
import os 

reload(sys)
sys.setdefaultencoding('utf-8')
# 里面包含你要抓取的页面的所以链接
page0 = urllib2.urlopen('http://192.168.1.222/t4.html').read()


htmlLink = HtmlLink()  
htmlLink.feed(htmlLink.unescape(page0))  
htmlLink.close()
# for index in range(len(htmlLink._names)):
# 	print "[%d] : (%s)-->   %s"%(index,htmlLink._names[index],htmlLink._hrefs[index])
# 	pass


links1 = htmlLink.setFullUrls('https://www.arduino.cc')

def delSpace(s):
	x = s.split(' ')
	return '_'.join(s.split(' ')) 

pwd=unicode(os.getcwd(), sys.stdin.encoding)



# for index in range(230, 250):
for index in range(0, len(htmlLink._names)):
	
	#####1. Use re lib
	# link = re.sub('http:', '', htmlLink._hrefs[index])
	#####2. Unicode process
	# print type(htmlLink._hrefs[index].encode("ascii"))
	# print (htmlLink._hrefs[index].encode("ascii"))
	page1= urllib2.urlopen(htmlLink._hrefs[index].encode("ascii")).read()
	

	parser = MyHTMLParser()
	# parser.setImgDir(htmlLink._names[index])
	parser.feed(parser.unescape(page1))
	print parser._content 
	
	name = delSpace(htmlLink._names[index])

	filename = pwd+'/order_md/'+str(index+191)+'_'+name+'.md'
	fd = open(filename , "w")
	if fd:
		print 'open : ' + filename
	fd.write( parser._content)
	fd.close()
	parser.close()

