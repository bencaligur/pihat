#!/usr/bin/env python
# this script will display colors for individual pixels on the Pi HAT
from sense_hat import SenseHat
sense = SenseHat()
import time

sense.set_pixel(7, 2, (0, 0, 200))
sense.set_pixel(4, 2, (0, 0, 200))
sense.set_pixel(5, 4, (0, 200, 0))
sense.set_pixel(3, 5, (200, 0, 0))
sense.set_pixel(5, 6, (200, 0, 0))
sense.set_pixel(2, 6, (200, 0, 0))
sense.set_pixel(5, 6, (200, 0, 0))
sense.set_pixel(1, 5, (200, 0, 0))

time.sleep(5)
sense.clear()
