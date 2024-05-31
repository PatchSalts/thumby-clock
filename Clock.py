# Clock.

# Use your Thumby as a timing tool!
# Unfortunately no RTC means no actual clock, but a timer and a stopwatch is all
# I ever wanted to implement anyway.

# Written by Patch Salts.
# Last edited 05/31/2024

import thumbyButton
import thumbyGraphics
import thumbyHardware
import time

import sys
sys.path.append('/Games/Clock')
import stopwatchModel

stopwatch = stopwatchModel.stopwatchModel()

thumbyHardware.reset()
