# cooling

import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

DHT_PIN = 7
FAN = 6

GPIO.setup(FAN, GPIO.OUT)
GPIO.output(FAN, False)

try:
    while True:
        # Read Temp and Hum from DHT22
        h, t = dht.read_retry(dht.DHT22, DHT_PIN)
        # print Temperature on Shell window
        print ("----------Value----------")
        print ("Temperature: ", t, "*C")
        sleep(10) # Wait 10 seconds and read again
        #print("temerature = {}C".format(t))
        if t > 25:
             print("temperature high")
             GPIO.output(pins["FAN"], True)
        else:
             print("temperature low")
             GPIO.output(pins["FAN"], False)
             
except KeyboardInterrupt:
    GPIO.cleanup()
