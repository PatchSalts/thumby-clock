# thumby-clock
A multi-function clock application for the Thumby device by TinyCircuits.

## Current status
Currently, just the backend is in progress, but the stopwatch feature is complete! Check out this demo of my test suite running:

[stopwatch demo.webm](https://github.com/PatchSalts/thumby-clock/assets/9244116/9886e5c5-3274-492a-862c-212e22b4b7c6)

Here you can see it switching between a few states. It starts in the "Stop" state, then slowly goes through "Play," "Stop," "Play," "Pause," "Play," and "Stop."

I decided that it makes the most sense for me to implement a state machine for this, so this order was chosen specifically to test all possible transitions I will use between the 3 states in the final product.

![Stopwatch state machine](https://github.com/PatchSalts/thumby-clock/assets/9244116/26fe9008-365b-4ced-9cce-e87fdb6cfeed)

(Please forgive the crude nature of the drawing, it was more or less a "napkin scribble" that all geniuses seem to be famous for doing. "A" and "B" represent the 2 buttons on the Thumby device itself. Pressing these buttons will transition from one state to another in the final application.)

The version of Python on the Thumby (MicroPython) doesn't have the `match` function, so I couldn't do "case/switch" style logic, so I ended up just doing object-orientation with the State Pattern. It doesn't have Python's `abc` module for making Abstract Base Classes, the Pythonic way of making interfaces, so I decided that it was OK to make my own concrete base class and override its implementations for the states in this application.

On top of all that, this greatly simplifies the work I will need to do for the upcoming timer feature, since I think I can just use the stopwatch class to keep track of elapsed time and compare it to the intended target time. Very exciting stuff. I intend for the application to be able to run a stopwatch and a timer at the same time, so this won't be too bad!
