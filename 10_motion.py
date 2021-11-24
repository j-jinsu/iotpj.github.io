# 10_motion.py

import RPi.GPIO as GPIO
import time

motion_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_pin, GPIO.IN)

def callback(pin):
    if GPIO.input(pin):
        print("motion detected!")
    else:
        print("it is gone!")

GPIO.add_event_detect(motion_pin, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(motion_pin, callback)

try:
    while True:
        time.sleep(0.1)
finally:
    print("cleaning up")
    GPIO.cleanup()
