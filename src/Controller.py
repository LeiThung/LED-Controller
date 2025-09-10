from gpiozero import PWMLED
from time import sleep

# Pins (BCM)
red = PWMLED(4)    # physischer Pin 7
green = PWMLED(3)  # physischer Pin 5
blue = PWMLED(2)   # physischer Pin 3

def led_off():
    red.off()
    green.off()
    blue.off()

def led_red():
    led_off()
    red.value = 1

def led_green():
    led_off()
    green.value = 1

def led_blue():
    led_off()
    blue.value = 1

def fade(from_led, to_led, steps=50, delay=0.02):
    for i in range(steps + 1):
        from_led.value = 1 - i / steps
        to_led.value = i / steps
        sleep(delay)

try:
    while True:
        led_red()
        sleep(1)
        led_green()
        sleep(1)
        led_blue()
        sleep(1)

        fade(red, green)
        fade(green, blue)
        fade(blue, red)

except KeyboardInterrupt:
    pass
finally:
    led_off()