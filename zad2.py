import RPi.GPIO as GPIO


def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


max_voltage = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

pwm = GPIO.PWM(2, 100)
pwm.start(0)

try:
    while True:
        koeff = input()

        if koeff == 'q':
            break
        
        if not is_number(koeff):
            print("Введено не число")
            continue
        koeff = float(koeff)
        if koeff < 0 or koeff > 100:
            print("Неверное число")
            continue

        print("Напряжение - {:.3}".format((koeff / 100) * max_voltage))
        pwm.stop()
        pwm.start(koeff)

finally:
    pwm.stop()
    GPIO.cleanup()
