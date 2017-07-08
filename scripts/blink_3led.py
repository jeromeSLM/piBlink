import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
while True:
    GPIO.output(7,True)
    GPIO.output(11,False)
    GPIO.output(13,False)
    time.sleep(0.5)
    GPIO.output(7,False)
    GPIO.output(11,True)
    GPIO.output(13,False)
    time.sleep(0.5)
    GPIO.output(7,False)
    GPIO.output(11,False)
    GPIO.output(13,True)
    time.sleep(0.5)
