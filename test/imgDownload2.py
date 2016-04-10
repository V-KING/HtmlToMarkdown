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
			os.mkdir(path)
			return 0
		except:
			os.chdir(path)
			return 1
	def downloadOne(self,image,path):
		print 'image_down function'
		self.__cd(path)
		try:
			urllib.urlretrieve(image,image.split('/')[-1]) #利用image.split('/')[-1]获得文件名
			print "ok : "+image
			return image
		except:
			print "Fail download image: "+image
			return False

	def downloadImages(self,images,path):
		print 'image_down function'
		self.__cd(path)
		if not images:
			print "no images arg"
		else:
			for image in images:
				try:
					urllib.urlretrieve(image,image.split('/')[-1]) #利用image.split('/')[-1]获得文件名
					print "ok : "+image
					return True
				except:
					print "Fail download image: "+image
					return False



def main():
	imgLists=["http://www.wikihow.com/images/0/07/Name-a-Class-in-Java-Step-5.jpg"]
	imgD = ImageDownload()
	imglink='http://www.wikihow.com/images/0/07/Name-a-Class-in-Java-Step-5.jpg'
	imgD.downloadOne(imglink,'img')
	imgD.downloadImages(imgLists, 'img')




if __name__ == '__main__':
	main()

