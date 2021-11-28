# sleep 

import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO_PIN = 27
led_pin = 19

GPIO.setup(GPIO_PIN, GPIO.IN)
GPIO.setup(RGB, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

try:
    while True:
        if GPIO.input(GPIO_PIN) == True:
            print 'Motion Detected.'
        time.sleep(10)
        else :
            print 'Motion Not detected.'
        pwm_led.ChangeDutyCycle(0)  
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
