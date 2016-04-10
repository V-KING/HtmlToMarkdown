#! /usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Error: 
# Traceback (most recent call last):
#   File "getPageLinks.py", line 67, in <module>
#     main()
#   File "getPageLinks.py", line 48, in main
#     hlk.feed(hlk.unescape(page))  
#   File "/usr/lib/python2.7/HTMLParser.py", line 472, in unescape
#     return re.sub(r"&(#?[xX]?(?:[0-9a-fA-F]+|\w{1,8}));", replaceEntities, s)
#   File "/usr/lib/python2.7/re.py", line 151, in sub
#     return _compile(pattern, flags).sub(repl, string, count)
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 5822: ordinal not in range(128)


