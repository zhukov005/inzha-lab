import RPi.GPIO as GPIO
import time

import numpy as np
import matplotlib.pyplot as pyplot
import math
import scipy.io.wavfile as sc

GPIO_pins = (26, 19, 13, 6, 5, 11, 9, 10)

GPIO.setmode(GPIO.BCM)

GPIO.setup(GPIO_pins, GPIO.OUT)

def num2dec(value):
    if value > 255 or value < 0: raise ValueError
    for i in range(7, -1, -1):
        GPIO.output(GPIO_pins[i], value % 2)
        value //= 2

try:
    rate, data = sc.read("file1.wav")

    # rate = 44100

    length = data.shape[0] / rate
    channelsCount = data.shape[1]

    print("Channels: ", channelsCount, "\n", "Length: ", length, "sec\n", "Sample rate: ", rate, "Hz", sep = "")

    wait = 1 / rate
    data = list(map(lambda x: int(x[0]), data))
    for value in data:
        num2dec((value // 256) & 255)
        # time.sleep(wait)


except KeyboardInterrupt:
    print("KeyboardInterrupt")

finally:
    GPIO.cleanup()




