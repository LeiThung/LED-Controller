import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- GPIO Setup ---
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

# --- Webserver Handler ---
class LEDHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/led/on":
            GPIO.output(LED_PIN, GPIO.HIGH)
            self._respond("LED ist AN")
        elif self.path == "/led/off":
            GPIO.output(LED_PIN, GPIO.LOW)
            self._respond("LED ist AUS")
        elif self.path == "/":
            self._respond(self._html_page())
        else:
            self.send_error(404, "Seite nicht gefunden")

    def _respond(self, content, content_type="text/html"):
        self.send_response(200)
        self.send_header("Content-type", content_type)
        self.end_headers()
        if isinstance(content, str):
            content = content.encode("utf-8")
        self.wfile.write(content)

    def _html_page(self):
        return """
        <html>
        <head><title>LED Steuerung</title></head>
        <body>
            <h1>LED Steuerung</h1>
            <form action="/led/on" method="get">
                <button type="submit">LED AN</button>
            </form>
            <form action="/led/off" method="get">
                <button type="submit">LED AUS</button>
            </form>
        </body>
        </html>
        """

# --- Server Start ---
def run(server_class=HTTPServer, handler_class=LEDHandler, port=8080):
    server_address = ("0.0.0.0", port)  # Lauscht auf allen Interfaces
    httpd = server_class(server_address, handler_class)
    print(f"Starte Webserver auf http://0.0.0.0:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer wird beendet...")
    finally:
        GPIO.cleanup()
        print("GPIO aufgeräumt.")

if __name__ == "__main__":
    run()
