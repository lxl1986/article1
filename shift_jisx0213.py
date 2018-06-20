# -*- coding: utf8 -*-

import sys
import struct

# m, plane [1,2]
# k, row [1--94]
# t, column [1--94]


def shift_jisx0213():
	"""
	get the shift_jisx0213 character glyphs.
	"""
	# m = 1, plane 1
	for k in range(1,95):
		for t in range(1,95):
			if k <= 62:
				s1 = int((k+257)/2)
			else:
				s1 = int((k+385)/2)

			if k % 2 == 0:
				s2 = t + 158
			elif t <= 63:
				s2 = t + 63
			else:
				s2 = t + 64

			b = struct.pack('2B', s1, s2)
			figure = b.decode('shift_jisx0213', 'ignore')		
			print(b, figure, struct.unpack('>H',b))
	
	# m = 2, plane 2
	km2 = [1, 3, 4, 5, 8, 12, 13, 14, 15] + list(range(78,95))
	for k in km2:
		for t in range(1,95):
			if k <= 15:
				s1 = int((k+479)/2) - int(k/8) * 3
			else:
				s1 = int((k+411)/2)

			if k % 2 == 0:
				s2 = t + 158
			elif t <= 63:
				s2 = t + 63
			else:
				s2 = t + 64

			b = struct.pack('2B', s1, s2)
			figure = b.decode('shift_jisx0213', 'ignore')		
			print(b, figure, struct.unpack('>H',b))

if __name__ == '__main__':
	shift_jisx0213()
