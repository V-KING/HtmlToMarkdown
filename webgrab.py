#!/usr/bin/python
# -*- coding: UTF-8 -*-
from HTMLParser import HTMLParser
import urllib2
from imgDownload import ImageDownload
from getPageLinks import HtmlLink
import re

page = urllib2.urlopen('https://www.arduino.cc/en/Tutorial/AnalogReadSerial').read()
content=' '

class MyHTMLParser(HTMLParser):
	wikistart = False 
	f_end = False
	f_start=False
	_content=''
	addH1Tag=False
	addH2Tag=False
	addCodeStartTag=False
	addH4RedTag=False
	addColorCodeTag=False
	getcode_f=False
	meet_span_times=0
	isNotContentTag=False
	htmlink=HtmlLink()
	imgD=ImageDownload()
	_imgLink=''
	_imgName=''
	_imgDir=''

	def handle_starttag(self, tag, attrs):
		if tag=='div' :
			for var,value in attrs:
				if var == 'id' and value=='wikitext':
					self.wikistart = True
		if tag=='h1' or tag=='h2' and self.wikistart==True:
			self.f_start=True
			if tag=='h1':
				self.addH1Tag=True
			if tag=='h2':
				self.addH2Tag=True
		if tag=='h3' or tag=='h4':
			self.addH4RedTag=True
		if tag=='pre' :
			self.addCodeStartTag=True
		##after mit h1 or h2 , you meet 'span', and is the first time you meet 'span'
		if tag=='span' and self.f_start==True :
			if self.meet_span_times==0:
				self.addColorCodeTag=True
			self.meet_span_times+=1
		# usefull html part's end
		if tag=='a' and self.f_start==True:
			for var,value in attrs:
				if value=='//www.arduino.cc/en/Reference/HomePage':
					self.f_end=True
		if tag=='style' and self.f_start==True:
			self.isNotContentTag=True
		if tag=='script' and self.f_start==True:
			self.isNotContentTag=True
		if tag=='img' and self.f_start==True and self.f_end==False:
			for var,link in attrs:
				if var == 'src' :
					imgL=self.htmlink.getFullLink('https://www.arduino.cc', link)
					# self._imgLink = self.imgD.downloadOne(imgL,'_'.join(self._imgDir.split(' ')))
					self._imgLink = self.imgD.downloadOne(imgL,"img")
					self._imgName=self.imgD.getImgName(self._imgLink)
					print '------------'+self._imgLink
					print '------------'+self._imgName
					# if meet img tag , add Markdown image sting here
					self._content += '\n![](' + self._imgDir + self._imgName + ')\n'
					print '\n![](' + self._imgDir + self._imgName + ')\n'
					return



	def handle_data(self, data):
		if  self.f_start==True and self.f_end==False:
			if  self.addH1Tag==True:
				self._content+='#'
			if  self.addH2Tag==True:
				self._content+='##'
			if  self.addCodeStartTag==True:
				self._content+='\n```\n'
			if  self.addColorCodeTag==True :
				self.addColorCodeTag=False
				if  re.match('click the image to enlarge', data) or re.match('image developed using', data) or re.match('Fritzing',data) or re.match('For more circuit examples', data) or re.match('Fritzing project page', data):
					# print '----------------'+data+'------------------------'
					self.meet_span_times=0;
					return
				self._content+='\n```c++\n'
			if  self.addH4RedTag==True:
				self._content+='####`'
			# when meet '[Get Code]' , it is the end of one code block.
			if data=='[Get Code]' :
				self.getcode_f=True
				self.meet_span_times=0
				# self._content+=data
				self._content+='\n```\n'
				return
			if data == 'Share':
				self.f_end=True
			if self.isNotContentTag==True:
				return
			# if self.isImgTag==True:
			# 	#if hava no data, then handle_data() can not execute 
			# 	self._content += '\n![](' + self._imgDir + self._imgName + ')\n'
			# 	print '\n![](' + self._imgDir + self._imgName + ')\n'
			# 	return
			self._content+=data



	def handle_endtag(self, tag):
		if self.f_start==True:
			if tag=='h1':
				self.addH1Tag=False
			if tag=='h2':
				self.addH2Tag=False
			if tag=='pre':
				self.addCodeStartTag=False
				self._content+='```\n'
			if tag=='span':
				self.addColorCodeTag=False
			if tag=='h3' or tag=='h4':
				self.addH4RedTag=False
				self._content+='`\n'
			if self.isNotContentTag==True:
				self.isNotContentTag=False	
				pass

		pass

	def setImgDir(self,  pImgDir):
		self._imgDir=pImgDir+'/'
		pass
	def close(self):
		self.wikistart = False 
		self.f_end = False
		self.f_start=False
		self._content=''
		self.addH1Tag=False
		self.addH2Tag=False
		self.addCodeStartTag=False
		self.addH4RedTag=False
		self.addColorCodeTag=False
		self.getcode_f=False
		self.meet_span_times=0
		# htmlink.close()
		pass


def main():
	parser = MyHTMLParser()
	parser.feed(page)
	print parser._content 

	parser.close()

if __name__ == '__main__':
	main()

