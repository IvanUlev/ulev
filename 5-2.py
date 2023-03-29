import RPi.GPIO as GPIO
import time 
def dec2bin(a):
    return [int (num) for num in bin(a)[2:].zfill(8)]
def num2dac(a):
    signal = dec2bin(a)
    GPIO.output(dac,signal)
    return signal


def adc():
    x = 0
    for i in range(bits - 1, -1, -1):
        x += 2**i
        GPIO.output(dac, dec2bin(x))
        time.sleep(0.01)
        comp_val = GPIO.input(comp)
        if (comp_val == 0):
            x -= 2**i
    return x


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
bits = len(dac)
levels = 2 ** bits
maxv = 3.3
GPIO.setmode (GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
c = 1
while (c):
    try:     
        while (1):
            val = adc()
            print(val, dec2bin(val) ,"V= {:.4}" .format(val / levels * maxv))  
    finally:
        GPIO.output(dac, 0)
        GPIO.output(troyka, 0)
        GPIO.cleanup()
        c = 0