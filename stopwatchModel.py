# stopwatchModel.

# Classes implementing a stopwatch.

# Written by Patch Salts.
# Last edited 06/03/2024

import time
import baseState

class stopwatchModel:
    """Class for operating a stopwatch.
    
    Attributes:
        elapsedTime_ms (int): The time that has elapsed in milliseconds.
        state (stopwatchModelState): The object representing the current state.
    """
    def __init__(self):
        """Construct stopwatchModel."""
        self.elapsedTime_ms = 0
        self.state = stopwatchModelState(self)
        self.state.enter()
        self.transition(stopwatchModelStateStop)

    def transition(self, state: stopwatchModelState):
        """Transition stopwatchModel from one state to another.
        
        Parameters:
            state (stopwatchModelState): Class of state to transition into.
        """
        self.state.exit()
        self.state = state(self)
        self.state.enter()

    def addElapsedTime_ms(self, time_ms: int):
        """Add time in milliseconds to the current elapsed time.
        
        Parameters:
            time_ms (int): The time in milliseconds to add to the elapsed time.
        """
        self.elapsedTime_ms = time.ticks_add(self.elapsedTime_ms, time_ms)

    def getElapsedTime_ms(self) -> int:
        """Return current elapsed time in milliseconds.
        
        Returns:
            int: Current elapsed time in milliseconds.
        """
        return self.elapsedTime_ms
    
    def resetElapsedTime_ms(self):
        """Reset elapsed time to 0."""
        self.elapsedTime_ms = 0

    def update(self):
        """Allow current state to update model and request a new state."""
        newState = self.state.update()
        if newState is not None:
            self.transition(newState)

class stopwatchModelState(baseState.baseState):
    """Base class for states for stopwatchModel.
    
    Attributes:
        model (stopwatchModel): The model this state is attached to.
    """
    def __init__(self, model: stopwatchModel):
        """Construct stopwatchModelState.
        
        Parameters:
            model (stopwatchModel): The model this state is attached to.
        """
        super().__init__(model)

    def update(self) -> stopwatchModelState:
        """Update the model.
        
        Returns:
            stopwatchModelState: Optional class of state to transtition into.
        """
        pass

class stopwatchModelStateStop(stopwatchModelState):
    """Class for the "stopped" state. Does nothing but resets upon entry."""
    def enter(self):
        """Run setup actions when entering state: reset stopwatch."""
        self.model.resetElapsedTime_ms()

class stopwatchModelStatePlay(stopwatchModelState):
    """Class for the "playing" state. Adds to elapsed time when active.
    
    Attributes:
        timeThen_ms (int): The time (ms) when this state was previously updated.
        timeNow_ms (int): The time (ms) when this state is currently updated.
    """
    def __init__(self, model: stopwatchModel):
        """Construct stopwatchModelStatePlay.
        
        Parameters:
            model (stopwatchModel): The model this state is attached to.
        """
        super().__init__(model)
        self.timeThen_ms = int()
        self.timeNow_ms = int()

    def enter(self):
        """Run setup actions when entering state: set times to current time."""
        now = time.ticks_ms()
        self.timeThen_ms = now
        self.timeNow_ms = now

    def exit(self):
        """Run cleanup actions when exiting state: run one last update."""
        self.update()

    def update(self):
        """Update the model: refresh times and add difference to stopwatch."""
        self.timeNow_ms = time.ticks_ms()
        timeElapsed_ms = time.ticks_diff(self.timeNow_ms, self.timeThen_ms)
        self.model.addElapsedTime_ms(timeElapsed_ms)
        self.timeThen_ms = self.timeNow_ms

class stopwatchModelStatePause(stopwatchModelState):
    """Class for the "paused" state. Does absolutely nothing."""
    pass
