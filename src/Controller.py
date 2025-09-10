import RPi.GPIO as GPIO
from time import sleep

# Pins
RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

def led_off():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.LOW)

def led_red():
    led_off()
    GPIO.output(RED_PIN, GPIO.HIGH)

def led_green():
    led_off()
    GPIO.output(GREEN_PIN, GPIO.HIGH)

def led_blue():
    led_off()
    GPIO.output(BLUE_PIN, GPIO.HIGH)

try:
    while True:
        led_red()
        sleep(1)
        led_green()
        sleep(1)
        led_blue()
        sleep(1)
except KeyboardInterrupt:
    pass
finally:
    led_off()
    GPIO.cleanup()
