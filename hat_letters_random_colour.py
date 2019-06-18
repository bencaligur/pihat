#!/usr/bin/env python
# this script will display letters with random colors on the Pi HAT
from sense_hat import SenseHat
import time
import random
sense = SenseHat()
# assign a random interger between 0 and 255 to a variable named r
r = random.randint(0,255)

sense.show_letter("J", (r, 0, 0))
time.sleep(1)
sense.show_letter("A", (0, r, 0))
time.sleep(1)
sense.show_letter("H", (0, 0, r))
time.sleep(1)

sense.clear()
