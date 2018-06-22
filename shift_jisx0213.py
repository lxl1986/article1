# -*- coding: utf-8 -*-

import sys
import struct

# m, plane [1,2]
# k, row [1--94]
# t, column [1--94]


def shift_jisx0213():
	"""
	get the shift_jisx0213 character glyphs.
	the parameters are obtained from Internet.
	"""
	# m = 1, plane 1
	for k in range(1,95):
		for t in range(1,95):
			if k <= 62:
				s1 = int((k+257)/2)  ## int((1+257)/2)=129 --> int((62+257)/2)=159
			else:
				s1 = int((k+385)/2)  ## int((63+385)/2)=224 --> int((94+385)/2)=239

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
			if k <= 15:## why there are two 244? k==15, s1==244; k==78, s1==244.
				s1 = int((k+479)/2) - int(k/8) * 3  ## [240, 241, 241, 242, 240, 242, 243, 243, 244]
			else:
				s1 = int((k+411)/2) ## [244, 245, 245, 246, 246, 247, 247, 248, 248, 249, 249, 250, 250, 251, 251, 252, 252]
			
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
