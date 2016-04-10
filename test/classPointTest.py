from urlparse import urlparse
class ClassPointTest(object):
	"""docstring for ClassPointTest"""
	def __init__(self, _hrefs):
		super(ClassPointTest, self).__init__()
		self._hrefs = _hrefs

	def setFullUrls(self, prefix):
		fullHrefs = self._hrefs
		for index in range(len(self._hrefs)):
			o = urlparse(self._hrefs[index])
			if o.netloc=='':
				fullHrefs[index] = prefix+self._hrefs[index]
				continue;
			if o.scheme=='':
				fullHrefs[index]='http:'+self._hrefs[index]
				continue;
		# self._hrefs=fullHrefs
		return fullHrefs

# add prefix to evrey listArg
listArg = ['/en/setup', 'en/loop']		

test = ClassPointTest(listArg)
print test._hrefs
print test.setFullUrls('http:www.arduino.cc')
