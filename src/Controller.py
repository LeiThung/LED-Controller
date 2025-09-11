from gpiozero import PWMLED
from flask import Flask, request, jsonify
from flask_cors import CORS
from time import sleep

app = Flask(__name__)
CORS(app)

# Pins (BCM)
red = PWMLED(4)    # physischer Pin 4
green = PWMLED(3)  # physischer Pin 3
blue = PWMLED(2)   # physischer Pin 2

@app.route("/api/led-off", methods=["POST"])
def led_off():
    red.off()
    green.off()
    blue.off()
    return jsonify({"status": "off"})

@app.route("/api/led-red", methods=["POST"])
def led_red():
    led_off()
    red.value = 1
    return jsonify({"status": "red"})

@app.route("/api/led-green", methods=["POST"])
def led_green():
    led_off()
    green.value = 1
    return jsonify({"status": "green"})

@app.route("/api/led-blue", methods=["POST"])
def led_blue():
    led_off()
    blue.value = 1
    return jsonify({"status": "blue"})

def fade(from_led, to_led, steps=50, delay=0.02):
    for i in range(steps + 1):
        from_led.value = 1 - i / steps
        to_led.value = i / steps
        sleep(delay)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)