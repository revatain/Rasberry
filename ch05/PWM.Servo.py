import RPi.GPIO as GPIO
import time
SERVO_PIN = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
servo = GPIO.PWM(SERVO_PIN, 50)
servo.start(0)

try:
	while 1:
		servo.ChangeDutyCycle(7.5)
		time.sleep(1)
		servo.ChangeDutyCycle(12.5)
		time.sleep(1)
		servo.ChangeDutyCycle(2.5)
		time.sleep(1)
except KeyboardInterrupt:
	servo.stop(0)
	GPIO.cleanup()
