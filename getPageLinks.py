#!/usr/bin/python
# -*- coding: UTF-8 -*-
from HTMLParser import HTMLParser  
import urllib2
import sys
from urlparse import urlparse
import re


reload(sys)
sys.setdefaultencoding('utf-8')

page = urllib2.urlopen('http://192.168.1.222/t4.html').read()

class HtmlLink(HTMLParser):  
	aTag = False
	links=[]
	hrefAttr=False
	_names=[]
	_hrefs=[]	
	def handle_starttag(self,tag,attr):  
		if tag == 'a':  
			# print '<a>'
			self.aTag = True  
			for var,value in attr:
				if var=='href':
					self.hrefAttr=True
					self._hrefs.append(value)
					return


	def handle_endtag(self,tag):  
		if tag == 'a':  
			# print '</a>'
			self.aTag = False  
			self.hrefAttr=False


	def handle_data(self,data):  
		if self.aTag and self.hrefAttr==True:  
			# print '++++++++'
			self._names.append(data);
			self.hrefAttr=False
			self.aTag=False

	def getLinkNames(self):
		return self._names

	def getLinks(self):
		return self._hrefs

	def getNamesAndLinks(self):
		self.links=dict(zip(self._names, self._hrefs))
		return self.links
		pass

	def getFullLink(self, prefix, link):
		o = urlparse(link)
		if o.netloc=='':
			return prefix+link
		if o.scheme=='':
			return 'http:' + link

	def setFullUrls(self, prefix):
		fullHrefs = self._hrefs
		for index in range(len(self._hrefs)):
			o = urlparse(self._hrefs[index])
			if o.netloc=='':
				fullHrefs[index] = prefix+self._hrefs[index]
				continue;
			if o.scheme=='':
				fullHrefs[index]='https:'+self._hrefs[index]
				continue;
			# fullHrefs[index]=self._hrefs
		self._hrefs=fullHrefs
		return fullHrefs

	def helpPrint(self):
		for index in range(len(self._names)):
			# print "(%s):   %s"%(self._names[index],self._hrefs[index])
			print "%d_%s.md"%(index+191,self._names[index])

		for index in range(len(self._hrefs)):
			# print "self._hrefs[%s]:%s"%(index,self._hrefs[index])
			print "self._hrefs[x]:%s"%(self._hrefs[index])
		pass
	def delSpace(self,s):
		x = s.split(' ')
		return '_'.join(s.split(' ')) 

def main():
	hlk = HtmlLink()  
	print hlk.getFullLink('https://www.arduino.cc', '//www.arduino.cc/en/Tutorial/AnalogReadSerial')
	hlk.feed(hlk.unescape(page))  

	for index in range(len(hlk._names)):
		# print "(%s):   %s"%(self._names[index],self._hrefs[index])
		name=hlk.delSpace(hlk._names[index])	
		print "%d_%s.md"%(index+191,name)

	# print len(hlk._hrefs)
	# print len(hlk._names)

	# for name,href in hlk.getNameLinks().items():
	# 	print "{%s:%s}"%(name,href)
	# 	pass
	# for value in hlk._hrefs:
	# 	print value
	# print len(hlk._hrefs)

	# print '--------------------------------'
	hlk.close()

	# links1=hlk.setFullUrls('http://www.arduino.cc')
	# print hlk._hrefs 

	# for value in hlk._hrefs:
	# 	print value
	# print len(hlk._hrefs)
	

if __name__ == '__main__':
	main()


