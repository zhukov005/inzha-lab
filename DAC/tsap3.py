import RPi.GPIO as GPIO
import time as TIME

import numpy
import matplotlib.pyplot as pyplot
import math

time = 10
frequency = 0.5
samplingFrequency = 50

GPIO_pins = (26, 19, 13, 6, 5, 11, 9, 10)

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_pins, GPIO.OUT)

def num2dec(value):
    if value > 255 or value < 0: raise ValueError
    for i in range(7, -1, -1):
        GPIO.output(GPIO_pins[i], value % 2)
        value //= 2

# ndarray = numpy.sin(numpy.arange(0, time, 1/samplingFrequency))
# ndarray = list(map(lambda x: 127 * x + 128, ndarray))


try:
    ndarray = []

    t = 0
    while t < time:
        ndarray.append(128 + 127 * math.sin(2 * math.pi * frequency * t))
        t += 1/samplingFrequency



    pyplot.plot(ndarray)
    pyplot.show()

    if input("Continue? n if no>>") != 'n':

        ndarray = list(map(math.trunc, ndarray))

        for value in ndarray:
            num2dec(value)
            TIME.sleep(1/samplingFrequency)

        num2dec(0)

except KeyboardInterrupt:
    print("KeyboardInterrupt")
except ValueError:
    print("Некорректное число")
finally:
    GPIO.cleanup()





