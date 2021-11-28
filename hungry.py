# hungry

import RPi.GPIO as GPIO 
import time
from time import sleep
from mcp3208 import MCP3208

ADC = MCP3208()

ADC_PIN = 0
TRIG = 18
ECHO = 21
DC_MOTOR = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(DC_MOTOR, GPIO.OUT)
GPIO.output(DC_MOTOR, False)

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
	# for i in range(8):
        #    print i, "ch Value: ", ADC.read(ADC_PIN)
        if distance < 10 and ADC.read(ADC_PIN) < 2000
           print("your pet is hungry")
           GPIO.output(pins["DC_MOTOR"], True)
           time.sleep(5)
        else
           print("your pet is not hungry")
           GPIO.output(pins["DC_MOTOR"], False)
           time.sleep(5)
            
except KeyboardInterrupt:
    GPIO.cleanup()
