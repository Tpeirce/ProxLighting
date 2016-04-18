#!/usr/bin/python

import bluetooth
import time
import os
beforePresent = False
timeSleep = 5
countDown = 10

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
    result = bluetooth.lookup_name('2C:54:CF:79:C3:5E', timeout=10)
    if (result != None):
        print "tp present"
	if (beforePresent == False):
		os.system("./codesend 351491")
		os.system("./codesend 351491")
		time.sleep(1)
		os.system("./codesend 349955")
		os.system("./codesend 349955")
		time.sleep(1)
		os.system("./codesend 349635")
		os.system("./codesend 349635")
		time.sleep(1)
		os.system("./codesend 349491")
		os.system("./codesend 349491")
		beforePresent = True
#		os.system("echo 0=90% > /dev/servoblaster")
#		time.sleep(20)
#                os.system("echo 0=0% > /dev/servoblaster")
	#backoff to conserve bluetooth power
	if (timeSleep < 60):
		timeSleep += 10
	countDown = 10
    else:
        print "tp out of range"
	#if countdown expired
	if (countDown < 0):
		#this line is prolly pointless
		if (beforePresent == True):
              		os.system("./codesend 351500")
			os.system("./codesend 351500")
               		time.sleep(1)
			os.system("./codesend 349964")
			os.system("./codesend 349964")
                	time.sleep(1)
			os.system("./codesend 349644")
			os.system("./codesend 349644")
                	time.sleep(1)
			os.system("./codesend 349500")
			os.system("./codesend 349500")
			beforePresent = False
			
	else:
		countDown-=1
	timeSleep = 5
    time.sleep(timeSleep)
