#!/usr/bin/python

import ephem
import datetime

somewhere = ephem.Observer()
somewhere.lat = '41.744579' # <== change me
somewhere.lon = '-72.691917' # <== and change me
somewhere.elevation = 112
#print somewhere.date

sun = ephem.Sun()

r1 = somewhere.next_rising(sun)
s1 = somewhere.next_setting(sun)
print (r1)
print (s1)
