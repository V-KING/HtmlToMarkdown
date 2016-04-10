#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
from getPageLinks import HtmlLink

page = urllib2.urlopen('http://192.168.1.222/t.html').read()

hlk = HtmlLink()  
hlk.feed(hlk.unescape(page))  
# print len(hlk._hrefs)
# print len(hlk._names)

# for index in range(len(hlk._hrefs)):
# 	print "hlk._hrefs[%s]:%s"%(index,hlk._hrefs[index])
# 	pass
for index in range(len(hlk._names)):
	print "(%s):   %s"%(hlk._names[index],hlk._hrefs[index])
	pass
# for name,href in hlk.getNameLinks().items():
# 	print "{%s:%s}"%(name,href)
# 	pass

hlk.close()