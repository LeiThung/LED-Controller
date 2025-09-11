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
            blue.value = b
            green.value = g
            red.value = r
            sleep(delay)

        # Green → Blue
        for i in range(steps + 1):
            r = 0
            g = (steps - i) / steps
            b = i / steps
            blue.value = b
            green.value = g
            red.value = r
            sleep(delay)

        # Blue → Red
        for i in range(steps + 1):
            r = i / steps
            g = 0
            b = (steps - i) / steps
            blue.value = b
            green.value = g
            red.value = r
            sleep(delay)

@app.route("/api/color-picker", methods=["POST"])
def changeColor():
    try:
        data = request.get_json()
        
        rgb_string = data.get("color")  # z.B. "rgb(1, 1, 1)"
        if not rgb_string:
            return jsonify({"error": "No color provided"}), 400

        # Entferne "rgb(" und ")" und splitte nach Komma
        rgb_values = rgb_string.strip()[4:-1].split(",")
        
        # Konvertiere Strings in Float oder Int und normalisiere falls nötig
        r = float(rgb_values[0].strip())
        g = float(rgb_values[1].strip())
        b = float(rgb_values[2].strip())

        # Wenn deine GPIO-PWM Werte von 0.0 bis 1.0 erwarten, kannst du sie direkt so setzen
        red.value = r
        green.value = g
        blue.value = b

        return jsonify({"status": "success", "r": r, "g": g, "b": b}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)