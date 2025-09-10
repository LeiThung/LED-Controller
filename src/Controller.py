import RPi.GPIO as GPIO
from time import sleep

# Pins
RED_PIN = 3
GREEN_PIN = 5
BLUE_PIN = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# PWM für jede Farbe
r = GPIO.PWM(RED_PIN, 100)
g = GPIO.PWM(GREEN_PIN, 100)
b = GPIO.PWM(BLUE_PIN, 100)

r.start(0)
g.start(0)
b.start(0)

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

def fade(from_pwm, to_pwm):
    for i in range(0, 101, 2):
        from_pwm.ChangeDutyCycle(100 - i)
        to_pwm.ChangeDutyCycle(i)
        sleep(0.02)

try:
    while True:
        led_red()
        sleep(1)
        led_green()
        sleep(1)
        led_blue()
        sleep(1)
        fade(r, g)
        fade(g, b)
        fade(b, r)
        
except KeyboardInterrupt:
    pass
finally:
    led_off()
    GPIO.cleanup()
