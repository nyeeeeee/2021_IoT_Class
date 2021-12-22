from lcd import drivers
import datetime
import Adafruit_DHT
import time

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
PIN = 5

try:
    while True:
        hum , tem = Adafruit_DHT.read_retry(sensor, PIN)
        now = datetime.datetime.now()
        display.lcd_display_string((now.strftime("%x%X")),1)
        if hum is not None and tem is not None:
            #display.lcd_display_string(('%.1f*C,%.1f%%' % (tem,hum)),2)
            display.lcd_display_string(str(tem) + "*C, " + str(hum) + "%", 2)
        else:
            display.lcd_display_string('Read Error', 2)

finally:
    display.lcd_clear()