## feed

import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

PUMP = 5
DC_MOTOR = 13
GPIO.setup(DC_MOTOR, GPIO.OUT)
GPIO.setup(PUMP, GPIO.OUT)
GPIO.output(DC_MOTOR, False)
GPIO.output(PUMP, False)

print("사료를 주시겠습니까? yes/no")
feed = input() #input함수는 사용자에게 입력을 받습니다.
print("물을  주시겠습니까? yes/no")
water = input()

try:
    while True:

        if feed = "yes":
            print("feed bin on.")
            GPIO.output(pins["DC_MOTOR"], True)
            time.sleep(10)
        else:
            print("feed bin off.")
            GPIO.output(pins["DC_MOTOR"], False)
            time.sleep(10)
        if water = "yes":
            print("water pump on.")
            GPIO.output(pins["PUMP"], True)
            time.sleep(10)
        else:
            print("water pump off")
            GPIO.output(pins["PUMP"], False)
            time.sleep(10)
            
except KeyboardInterrupt:
    GPIO.cleanup()
