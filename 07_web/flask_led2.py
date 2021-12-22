from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
app = Flask(__name__) #파일명 얻어오기

@app.route("/")
def hello():
    return render_template("led.html")

@app.route("/led/<op>")
def led_op(op):
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "LED ON"
    elif op == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return"LED OFF"
    else :
        return "URL error"

#터미널에서 직접실행한 경우
if __name__ == "__main__" :
    try: 
        app.run(host="0.0.0.0") #port = 5000 - default

    finally:
        GPIO.cleanup()
