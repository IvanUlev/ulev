import RPi.GPIO as GPIO

def dec2bin(a):
    return [int (num) for num in bin(a)[2:].zfill(8)]

def bin2list(arr, a):
    for i in range(0,8):
        if (a & pow(2, i) == pow(2, i)):
            arr[7 - i] = 1
        else:
            arr[7 - i] = 0
    return arr
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
arr = [0, 0, 0, 0, 0, 0, 0, 0]
GPIO.setup(dac, GPIO.OUT)

c = 1
while (c):
    try:     
        while (1):
            a = int(input())

            if (a == 'l'):
                break
            if (a > 255 or a < 0):
                break
            bin2list (arr,a)
            GPIO.output(dac, arr)
            print("V = ", a/pow(2,8) * 3.3)
    except Err:
        printf('error')

    finally:
        GPIO.output(dac,0)
        GPIO.cleanup()
        c = 0