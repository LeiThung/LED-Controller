from gpiozero import PWMLED
from flask import Flask, request, jsonify
from flask_cors import CORS
from time import sleep

app = Flask(__name__)
CORS(app)

fade = False

# Pins (BCM)
red = PWMLED(4)    # physischer Pin 4
green = PWMLED(3)  # physischer Pin 3
blue = PWMLED(2)   # physischer Pin 2

@app.route("/api/led-off", methods=["POST"])
def led_off():
    global fade
    fade = False
    red.off()
    green.off()
    blue.off()
    return jsonify({"status": "off"})

@app.route("/api/led-fade", methods=["POST"])
def fadeLED():
    steps = 100
    delay = 0.02
    global fade
    fade = True

    while fade:
        # Red → Green
        for i in range(steps + 1):
            r = (steps - i) / steps * 255
            g = i / steps * 255
            b = 0
            red.value = r / 255
            green.value = g / 255
            blue.value = b / 255
            sleep(delay)

        # Green → Blue
        for i in range(steps + 1):
            r = 0
            g = (steps - i) / steps * 255
            b = i / steps * 255
            red.value = r / 255
            green.value = g / 255
            blue.value = b / 255
            sleep(delay)

        # Blue → Red
        for i in range(steps + 1):
            r = i / steps * 255
            g = 0
            b = (steps - i) / steps * 255
            red.value = r / 255
            green.value = g / 255
            blue.value = b / 255
            sleep(delay)

@app.route("/api/color-picker", methods=["POST"])
def changeColor():
    global fade
    fade = False
    try:
        data = request.get_json()

        print(data)
        
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
        red.value = r / 255
        green.value = g / 255
        blue.value = b / 255

        return jsonify({"status": "success", "r": r, "g": g, "b": b}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)