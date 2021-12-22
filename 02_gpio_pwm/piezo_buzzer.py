#도 출력
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

#주파수 설정 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262) #도 
pwm.start(10)     #duty cycle (0~100)

time.sleep(2)
pwm.ChangeDutyCycle(0)  #부저음이 들리지 않음

pwm.stop()
GPIO.cleanup()
