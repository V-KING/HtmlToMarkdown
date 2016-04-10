#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import urllib
import os

class ImageDownload(object):
	"""docstring for ImageDownload"""
	def __init__(self):
		super(ImageDownload, self).__init__()

	def __cd(self,path):
		try:
			os.chdir(path)
			return 0
		except:
			os.mkdir(path)
			return 1
	def downloadOne(self,image,path):
		if path=='':
			path = './'
		self.__cd(path)
		try:
			urllib.urlretrieve(image,image.split('/')[-1]) #利用image.split('/')[-1]获得文件名
			print "ok : "+image
			self.__cd('../')
			return image 
		except:
			print "Fail download image: "+image
			self.__cd('../')
			return False

	def getImgName(self, pImgLink):
		return pImgLink.split('/')[-1]

	def downloadImages(self,images,path):
		self.__cd(path)
		if not images:
			print "no images arg"
		else:
			for image in images:
				try:
					urllib.urlretrieve(image,image.split('/')[-1]) #利用image.split('/')[-1]获得文件名
					print "ok : "+image
					result=True
				except:
					print "Fail download image: "+image
					result=False
		return result




def main():
	imgLists=["http://www.wikihow.com/images/0/07/Name-a-Class-in-Java-Step-5.jpg",
	"https://www.arduino.cc/en/uploads/Tutorial/AnalogReadSerial_BB.png"]
	imgD = ImageDownload()
	imglink='http://www.wikihow.com/images/0/07/Name-a-Class-in-Java-Step-5.jpg'
	imgD.downloadOne(imglink,'')
	print imgD.getImgName(imglink)
	# imgD.downloadImages(imgLists, "")




if __name__ == '__main__':
	main()

