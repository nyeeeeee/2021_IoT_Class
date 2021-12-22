#스위치로 LED 제어하기
import RPi.GPIO as GPIO

RED_PIN = 13
RED_SWITCH_PIN = 4
YELLOW_PIN = 19
YELLOW_SWITCH_PIN = 17
GREEN_PIN = 26
GREEN_SWITCH_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
#내부 풀다운저항 (안 눌렀을 때 : 0, 눌렀을 때 : 1)
GPIO.setup(RED_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(YELLOW_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GREEN_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        val1 = GPIO.input(RED_SWITCH_PIN)
        print(val1)
        GPIO.output(RED_PIN, val1) #GPIO.HIGH(1), GPIO.LOW(0)

        val2 = GPIO.input(YELLOW_SWITCH_PIN)
        print(val2)
        GPIO.output(YELLOW_PIN, val2)

        val3 = GPIO.input(GREEN_SWITCH_PIN)
        print(val3)
        GPIO.output(GREEN_PIN, val3)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
