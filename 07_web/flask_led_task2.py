from flask import Flask, render_template
import RPi.GPIO as GPIO

R_PIN = 17
B_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)
app = Flask(__name__) #파일명 얻어오기

@app.route("/")
def hello():
    return render_template("led2.html")

@app.route("/led/<op>/<cmd>")
def led_op(op, cmd):
    print(op)
    if op == "red" and cmd == "on":
        GPIO.output(R_PIN, GPIO.HIGH)
        return "RED LED ON"
    elif op == "red" and cmd == "off":
        GPIO.output(R_PIN, GPIO.LOW)
        return "RED LED OFF"
    elif op == "blue"and cmd == "on":
        GPIO.output(B_PIN, GPIO.HIGH)
        return "BLUE LED OFF"
    elif op == "blue" and cmd == "off":
        GPIO.output(B_PIN, GPIO.LOW)
        return "BLUE LED OFF"

#터미널에서 직접실행한 경우
if __name__ == "__main__" :
    try : 
        app.run(host="0.0.0.0") #port = 5000 - default
    finally :
        GPIO.cleanup()
