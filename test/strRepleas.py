#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
input = 'hello  abc world'


#第一个参数是正则表达式，第二个参数是要替换成的内容，第三个参数是替换原字符串
output = re.sub('http:', '','http://arduino.cc/en/Reference/FunctionDeclaration')
print output