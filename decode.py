# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 01:23:09 2018

@author: HCHO
"""

import base64
code='happytogather'
encodestr = base64.b85encode(code.encode('utf-8'))
print(encodestr)

#decode=base64.b85decode(encodestr.decode())
#print(decode)