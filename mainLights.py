#!/usr/bin/python

import bluetooth
import time
import os
beforePresent = False
timeSleep = 0
countDown = 10

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
#    tpPresent = bluetooth.lookup_name('2C:54:CF:79:C3:5E', timeout=3)
#    pwPresent = bluetooth.lookup_name('A0:99:9B:3D:94:11', timeout=3)
#    jaPresent = bluetooth.lookup_name('18:AF:61:62:9D:BC', timeout=3)
#    tnPresent = bluetooth.lookup_name('', timeout=4)
#    if (tpPresent != None or pwPresent != None or jaPresent != None):
    if (bluetooth.lookup_name('2C:54:CF:79:C3:5E', timeout=3) != None or bluetooth.lookup_name('A0:99:9B:3D:94:11', timeout=3) != None or bluetooth.lookup_name('18:AF:61:62:9D:BC', timeout=3) != None):
        print "Roommates present"
	if (beforePresent == False):
		os.system("./codesend 357635")
		time.sleep(1)
		os.system("./codesend 357635")
		time.sleep(1)
		beforePresent = True
	#backoff to conserve bluetooth power
	if (timeSleep < 60):
		timeSleep += 10
	countDown = 10
    else:
	timeSleep = 3
        print "Everyone out of range " + str(countDown)
	#if countdown expired, send off code
	if (countDown < 0):
		if (beforePresent == True):
			os.system("./codesend 357644")
			time.sleep(1)
			os.system("./codesend 357644")
			time.sleep(1)
              		beforePresent = False
	else:
		countDown-=1
    time.sleep(timeSleep)
