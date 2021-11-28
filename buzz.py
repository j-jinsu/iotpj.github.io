# Buzzer

import RPi.GPIO as GPIO 
import time
from time import sleep

TRIG = 18
ECHO = 21
buzzer_pin = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.output(buzzer_pin, False)


try:
    while True:
	GPIO.output(TRIGGER, False)
	time.sleep(0.5)

	GPIO.output(TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(TRIGGER, False)

	while GPIO.input(ECHO) == 0:
	    pulse_start = time.time()

	while GPIO.input(ECHO) == 1:
	    pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17000
	distance = round(distance, 2)

	print 'distance: ', distance, 'cm'
	time.sleep(1)
        if distance < 10    
           GPIO.output(buzzer_pin, True)       
           time.sleep(5)
           GPIO.output(buzzer_pin, False)
        else
            GPIO.output(buzzer_pin, False)
            
except KeyboardInterrupt:
    GPIO.cleanup()
