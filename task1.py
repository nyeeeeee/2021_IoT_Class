import threading
import time

import RPi.GPIO as GPIO

SEGMENT_PINS = [22, 20, 16, 23, 25, 26, 24]
DIGIT_PINS = [13, 18, 19, 17]
SWITCH_PIN = 5
LED_PIN = 4
PIEZO_PIN = 29

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #스위치 핀 초기값 0

GPIO.setup(LED_PIN, GPIO.OUT) #LED와 피에조부저 초기값 0
GPIO.output(LED_PIN, GPIO.LOW)

GPIO.setup(PIEZO_PIN, GPIO.OUT) #피에조 부저 초가값 0
GPIO.output(PIEZO_PIN, GPIO.LOW)

#주파수 설정 (262Hz)
pwm = GPIO.PWM(PIEZO_PIN, 262)
pwm.start(10)

#4 digit 초기값 0
for segment in SEGMENT_PINS:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)
for digit in DIGIT_PINS:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)

# 도   레   미   파   솔   라   시   도
#262, 294, 330, 349, 392, 440, 494, 523
melody = [262,262,392,392,440,440,392,349,349,330,330,294,294,262]

#반짝반짝 작은별
data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9

#숫자출력함수
def display1(digit, number):
    for i in range(4):
        if i + 1 == digit:
             GPIO.output(DIGIT_PINS[i], GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)

    for i in range(7):
        GPIO.output(SEGMENT_PINS[i], data[number][i])
        time.sleep(0.1)

def display2(): #노래재생함수
    GPIO.output(LED_PIN, GPIO.HIGH) #LED 불켜짐
    for i in melody:
        GPIO.output(PIEZO_PIN, GPIO.HIGH)
        pwm.ChangeFrequency(i)
        time.sleep(0.5)
        GPIO.cleanup()
        print('the end')

def play1():
    for b in range(6): #십의 자리/분세기
        display1(1,b)
        time.sleep(0.5)
        if b == 5:
            display2() #60:00일때 불이 켜지고 노래가 나옴

def play2():
    for a in range(10): #일의 자리/분세기
        display1(2,a)
        time.sleep(0.5)
        if a == 9:
            display1(2,0)

def play3():
    for j in range(6): #십의 자리/초세기
            display1(3,j)
            time.sleep(0.5)
            if j == 5:
                display1(3,0)

def play4():
    for i in range(10): #일의 자리/초세기
            display1(4,i)
            time.sleep(0.5)
            if i == 9:
                display1(0,0)

try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        if val == 1 : #시간재기
            pi1 = threading.Thread(target=play4)
            pi1.start()
            pi2 = threading.Thread(target=play3)
            pi2.start()
            pi3 = threading.Thread(target=play2)
            pi3.start()
            pi4 = threading.Thread(target=play1)
            pi4.start()

finally :
    GPIO.cleanup()
    print('bye')
