# -*- coding: utf8 -*-

import sys
import struct

# row		[1..94]
# column	[1..94]

# print(__file__[:-3])

def gb2312_20180608():
	"""
	get the gb2312 character glyphs.
	"""
	for row in range(1,95):
		for column in range(1,95):
			b = struct.pack('2B', row + 0xA0, column + 0xA0)
			figure = b.decode('gb2312', 'ignore')
			print(b, figure, struct.unpack('>H',b))
		print('\n')

if __name__ = '__main__':
	gb2312_20180608()