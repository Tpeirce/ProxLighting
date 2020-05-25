#!/usr/bin/python

import bluetooth
import time
import os
beforePresent = False
tpBefore = False
timeSleep = 0
countDown = 10
tpCount = 10

def tpOn():
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
   return

def tpOff():
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
   return

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
    tpPresent = bluetooth.lookup_name('2C:54:CF:79:C3:5E', timeout=3)
    pwPresent = bluetooth.lookup_name('A0:99:9B:3D:94:11', timeout=3)
    jaPresent = bluetooth.lookup_name('18:AF:61:62:9D:BC', timeout=3)
#    tnPresent = bluetooth.lookup_name('', timeout=4)
    if (tpPresent != None or pwPresent != None or jaPresent != None):
        print "Roommates present"
	if (beforePresent == False):
		os.system("./codesend 357635")
		time.sleep(1)
		os.system("./codesend 357635")
		time.sleep(1)
		beforePresent = True
	#backoff to conserve bluetooth power
	if (timeSleep < 60 and tpPresent != None):
		timeSleep += 10
	countDown = 10
    else:
        print "Everyone out of range " + str(countDown)
	#if countdown expired, send off code
	if (countDown < 0):
		if (beforePresent == True):
			os.system("./codesend 357644")
			os.system("./codesend 357644")
			time.sleep(1)
              		beforePresent = False
	else:
		countDown-=1
	timeSleep = 0

#   my room
#   if I am here and the code hasn't been sent yet, send the on code
    if (tpPresent != None and tpBefore == False):
	print "tp lights on"
	tpOn()
	tpBefore = True
	
    if(tpPresent != None):
	tpCount = 10
#   if I'm not here
    if (tpPresent == None):
#	and it's been a little bit since I was last seen, and the off code hasn't been sent before
	timeSleep = 0
	if (tpCount < 0):
		if (tpBefore == True):
			print "tp lights off"
			tpOff()
			tpBefore = False
#	otherwise just countdown until either I'm seen or it's time to turn off the lights
	else:
		tpCount-=1
		print "tp away for " + str(tpCount)
    time.sleep(0)
