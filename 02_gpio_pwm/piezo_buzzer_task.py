import RPi.GPIO as GPIO
import time

BUZZER_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

#주파수 설정 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10)     #duty cycle (0~100)

melody =[392, 392, 440, 440, 392, 392, 330, 392,392, 330,330, 294,392, 392, 440, 440,392, 392, 330, 392, 330, 294, 330, 262]

try:
    for i in melody:
        pwm.ChangeDutyCycle(10)
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
        if i == melody[11] :
            pwm.ChangeDutyCycle(0)
            time.sleep(1)

finally:
    pwm.stop()
    GPIO.cleanup()
