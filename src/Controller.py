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

def fade():
    steps = 100
    delay = 0.02

    while True:
        # Red → Green
        for i in range(steps + 1):
            r = (steps - i) / steps
            g = i / steps
            b = 0
            led_blue = b
            led_green = g
            led_red = r
            sleep(delay)

        # Green → Blue
        for i in range(steps + 1):
            r = 0
            g = (steps - i) / steps
            b = i / steps
            led_blue = b
            led_green = g
            led_red = r
            sleep(delay)

        # Blue → Red
        for i in range(steps + 1):
            r = i / steps
            g = 0
            b = (steps - i) / steps
            led_blue = b
            led_green = g
            led_red = r
            sleep(delay)

@app.route("/api/color-picker", methods=["POST"])
def changeColor():
    try:
        data = request.get_json()

        r = int(data.get("r", 0))
        g = int(data.get("g", 0))
        b = int(data.get("b", 0))

        return jsonify({"status": "success"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)