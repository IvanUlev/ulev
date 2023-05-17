import RPi.GPIO as GPIO
import time


def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


dac    = [26, 19, 13, 6, 5, 11, 9, 10]
comp   = 4
troyka = 17
bits   = len(dac)
levels = 2 ** bits
max_voltage = 3.3


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    t = int(input())
except ValueError:
    t = 10

try:
    num = 0
    delta = 1

    while True:
        GPIO.output(dac, decimal2binary(num))
        time.sleep(t / 512)
        if (num + delta) > 255 or (num + delta) < 0:
            delta = -delta
        num += delta

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
