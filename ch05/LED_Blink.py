import RPi.GPIO as GPIO
import time

led_pin = 4 #GPIO4

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

for i in range(10):
	GPIO.output(led_pin, 1) #on
	time.sleep(1)
	GPIO.output(led_pin, 0) #off
	time.sleep(1)

GPIO.cleanup()

