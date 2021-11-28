# goodjob

import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)


# set DATA pin
DHT_PIN = 7
DC_MOTOR = 13
GPIO.setup(DC_MOTOR, GPIO.OUT)
GPIO.output(DC_MOTOR, False)

try:
    while True:
        # Read Temp and Hum from DHT22
        h, t = dht.read_retry(dht.DHT22, DHT_PIN)
        # print Temperature and Humidity on Shell window
        print "----------Value----------"
        print "Temperature: ", t, "*C"
        print "Humidity   : ", h, "%"
        sleep(10) # Wait 2 seconds and read again
        if t > 25 and h > #??
            print("good job.")
            GPIO.output(pins["DC_MOTOR"], True)
            time.sleep(10)
        else
            GPIO.output(pins["DC_MOTOR"], False)
            
except KeyboardInterrupt:
    GPIO.cleanup()
