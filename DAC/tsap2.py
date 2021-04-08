import RPi.GPIO as GPIO
import time

GPIO_pins = (26, 19, 13, 6, 5, 11, 9, 10)

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_pins, GPIO.OUT)

def num2dec(value):
    if value > 255 or value < 0: raise ValueError
    for i in range(7, -1, -1):
        GPIO.output(GPIO_pins[i], value % 2)
        value //= 2                                          


try:
    print("Введите число повторений: ")
    repetetionsNumber = int(input())

    if repetetionsNumber < 0: raise ValueError


    for i in range(repetetionsNumber):
        for j in range(256):
            num2dec(j)
            time.sleep(0.01)

except KeyboardInterrupt:
    print("KeyboardInterrupt")
except ValueError:
    print("Некорректное число")
finally:
    GPIO.cleanup()
