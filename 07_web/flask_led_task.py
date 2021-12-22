from flask import Flask
import RPi.GPIO as GPIO

R_PIN = 17
B_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(R_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)
app = Flask(__name__) #파일명 얻어오기

@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p>
        <a href="/led/red/on">RED LED ON</a>
        <a href="/led/red/off">RED LED OFF</a>
        <a href="/led/blue/on">BLUE LED ON</a>
        <a href="/led/blue/off">BLUE LED OFF</a>
    '''

@app.route("/led/<op>/<cmd>")
def led_op(op, cmd):
    print(op)
    if op == "red" and cmd == "on":
        GPIO.output(R_PIN, GPIO.HIGH)
        return '''
            <p>RED LED ON</p>
            <a href="/">Go Home</a>
        '''
    elif op == "red" and cmd == "off":
        GPIO.output(R_PIN, GPIO.LOW)
        return '''
            <p>RED LED OFF</p>
            <a href="/">Go Home</a>
        '''
    elif op == "blue"and cmd == "on":
        GPIO.output(B_PIN, GPIO.HIGH)
        return '''
            <p>BLUE LED OFF</p>
            <a href="/">Go Home</a>
        '''
    elif op == "blue" and cmd == "off":
        GPIO.output(B_PIN, GPIO.LOW)
        return '''
            <p>BLUE LED OFF</p>
            <a href="/">Go Home</a>
        '''

#터미널에서 직접실행한 경우
if __name__ == "__main__" :
    try : 
        app.run(host="0.0.0.0") #port = 5000 - default
    finally :
        GPIO.cleanup()
