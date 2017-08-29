#!/usr/bin/python
import subprocess
import time
from datetime import datetime

import Adafruit_DHT
import RPi.GPIO as GPIO
import pytz as pytz
from RPLCD import CharLCD

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)

while True:
    now = datetime.now(pytz.timezone('Europe/London'))
    lcd.clear()
    lcd.cursor_pos = (0, 0)

    if int(now.strftime('%S')) % 10 == 0:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

        lcd.write_string('Temp: {0:0.1f} C'.format(temperature))
        lcd.cursor_pos = (1, 0)
        lcd.write_string('Humidity: {0:0.1f} %'.format(humidity))
        time.sleep(3.5)
    else:
        ip = subprocess.getoutput("ifconfig wlan0 | awk -F '[ :]+' '/inet/ {print $3}'").split()[0]

        lcd.write_string(now.strftime('%b %d  %H:%M:%S\n'))
        lcd.cursor_pos = (1, 0)
        lcd.write_string('IP: {}'.format(ip))
        time.sleep(1)
