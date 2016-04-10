#!/usr/bin/python
# -*- coding: UTF-8 -*-
from HTMLParser import HTMLParser
import urllib2

page = urllib2.urlopen('http://192.168.1.222/t5.html').read()
content=' '

class MyHTMLParser(HTMLParser):
	a_start=False
	

	def handle_starttag(self, tag, attrs):
		if tag=='a':
			self.a_start=True
		


	def handle_data(self, data):
		if self.a_start==True:
			print data


	def handle_endtag(self, tag):
		if tag=='a':
			self.a_start=False
		




def main():
	parser = MyHTMLParser()
	parser.feed(page)
	parser.close()

if __name__ == '__main__':
	main()

