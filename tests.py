# tests.

# Testing the various modules involved in the Clock project.

# Written by Patch Salts.
# Last edited 05/31/2024

import thumbyGraphics
import thumbyHardware
import time

import sys
sys.path.append('/Games/Clock')
import stopwatchModel


def testStopwatchModel() -> bool:
    thumbyGraphics.display.fill(0)
    fps = 10
    i = 1
    err = 200
    thumbyGraphics.display.setFPS(fps)
    stopwatch = stopwatchModel.stopwatchModel()
    frame = 0
    while(frame <= fps * i * 7):
        # testing state transitions;
        # play
        # pause
        # stop
        # play
        # pause
        # play
        # stop
    
        frame += 1
        if frame == fps * i:
            stopwatch.transition(stopwatchModel.stopwatchModelStatePlay)
        elif frame == fps * i * 2:
            stopwatch.transition(stopwatchModel.stopwatchModelStatePause)
            elapsedTime_ms = stopwatch.getElapsedTime_ms()
            if elapsedTime_ms < 1000 * i - err or elapsedTime_ms > 1000 * i + err:
                return False
        elif frame == fps * i * 3:
            stopwatch.transition(stopwatchModel.stopwatchModelStateStop)
            elapsedTime_ms = stopwatch.getElapsedTime_ms()
            if elapsedTime_ms != 0:
                return False
        elif frame == fps * i * 4:
            stopwatch.transition(stopwatchModel.stopwatchModelStatePlay)
        elif frame == fps * i * 5:
            stopwatch.transition(stopwatchModel.stopwatchModelStatePause)
            elapsedTime_ms = stopwatch.getElapsedTime_ms()
            if elapsedTime_ms < 1000 * i - err or elapsedTime_ms > 1000 * i + err:
                return False
        elif frame == fps * i * 6:
            stopwatch.transition(stopwatchModel.stopwatchModelStatePlay)
        elif frame == fps * i * 7:
            elapsedTime_ms = stopwatch.getElapsedTime_ms()
            if elapsedTime_ms < 1000 * i * 2 - err or elapsedTime_ms > 1000 * i * 2 + err:
                return False
            stopwatch.transition(stopwatchModel.stopwatchModelStateStop)
            elapsedTime_ms = stopwatch.getElapsedTime_ms()
            if elapsedTime_ms != 0:
                return False
    
        thumbyGraphics.display.fill(0)
        stopwatch.update()
        thumbyGraphics.display.setFont("/lib/font5x7.bin", 5, 7, 1)
        thumbyGraphics.display.drawText(str(stopwatch.getElapsedTime_ms()/1000), 0, 0, 1)
        thumbyGraphics.display.setFont("/lib/font3x5.bin", 3, 5, 1)
        thumbyGraphics.display.drawText(str(type(stopwatch.state))[0:18], 0, 8, 1)
        thumbyGraphics.display.drawText(str(type(stopwatch.state))[18:], 0, 14, 1)
        thumbyGraphics.display.update()
    return True

def runTests(tests: list[function]) -> bool:
    results = dict()

    for test in tests:
        print(f'Running {test.__name__}...')
        result = test()
        results[test.__name__] = result

    passes = int()
    fails = int()
    print()
    print('SUMMARY:')
    for result in results:
        print(f'{result}: {'PASS' if results[result] else 'FAIL'}')
        if results[result]:
            passes += 1
        else:
            fails += 1
    print(f'{passes} passes and {fails} failures')

tests = [testStopwatchModel]
runTests(tests)

thumbyHardware.reset()
