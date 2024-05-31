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
fps = 10
thumbyGraphics.display.setFPS(fps)
frame = 0

while(True):
    # testing state transitions;
    # 3s:  play
    # 6s:  pause
    # 9s:  stop
    # 12s: play
    # 15s: pause
    # 18s: play
    # 21s: stop

    frame += 1
    if frame == fps*3:
        stopwatch.transition(stopwatchModel.stopwatchModelStatePlay)
    elif frame == fps*6:
        stopwatch.transition(stopwatchModel.stopwatchModelStatePause)
    elif frame == fps*9:
        stopwatch.transition(stopwatchModel.stopwatchModelStateStop)
    elif frame == fps*12:
        stopwatch.transition(stopwatchModel.stopwatchModelStatePlay)
    elif frame == fps*15:
        stopwatch.transition(stopwatchModel.stopwatchModelStatePause)
    elif frame == fps*18:
        stopwatch.transition(stopwatchModel.stopwatchModelStatePlay)
    elif frame == fps*21:
        stopwatch.transition(stopwatchModel.stopwatchModelStateStop)

    thumbyGraphics.display.fill(0)
    stopwatch.update()
    thumbyGraphics.display.drawText(str(stopwatch.getElapsedTime_ms()/1000), 0, 0, 1)
    thumbyGraphics.display.update()

thumbyHardware.reset()
