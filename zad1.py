import RPi.GPIO as GPIO
import time as time
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
arr = [ 0, 0, 0, 0, 0, 0, 0, 0]
GPIO.setup(dac, GPIO.OUT)
per = float(input())  
per = per / 512
c = 1
while (c):
    try: 
    
        a = 0  
        while (1):
            while(a < 255):
                a = a+1
                time.sleep (per)
                bin2list (arr,a)
                GPIO.output(dac, arr)
                print (arr)
            while (a > 0):

                a = a-1
                time.sleep (per)
                bin2list (arr,a)
                GPIO.output(dac, arr)
                print(arr)
          
    except Err:
        printf('error')

    finally:
        GPIO.output(dac,0)
        GPIO.cleanup()
        c = 0