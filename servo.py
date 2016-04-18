import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 50)
pwm.start(5)
try:
        while True:
                #duty cycle is duty = float(angle) / 10.0 + 2.5
                duty = 0 / 10.0 + 2.5
                print duty
                pwm.ChangeDutyCycle(7.5)
                time.sleep(3)
                duty = 180 / 10.0 + 2.5
                print duty
		#pwm.ChangeDutyCycle(2.5)
                time.sleep(3)
except KeyboardInterrupt:  
	# here you put any code you want to run before the program   
	# exits when you press CTRL+C
	print "Exiting cleanly..."
except:  
	# this catches ALL other exceptions including errors.  
	# You won't get any error messages for debugging  
	# so only use it once your code is working  
	print "Other error or exception occurred!"  
finally:
	print "Cleanup"
	pwm.stop()
	GPIO.cleanup()
