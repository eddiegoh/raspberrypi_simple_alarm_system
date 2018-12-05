import RPi.GPIO as GPIO
import time


class Sensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
    def getState(self):
        return GPIO.input(self.pin)
 

