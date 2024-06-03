# baseState.

# Base class for implementing a state machine.

# Written by Patch Salts.
# Last edited 06/03/2024

class baseState:
    """Base class for states.

    Attributes:
        model: The model this state is attached to.
    """
    def __init__(self, model):
        """Construct baseState.

        Parameters:
            model: The model this state is attached to.
        """
        self.model = model

    def enter(self):
        """Run setup actions when entering state."""
        pass

    def exit(self):
        """Run cleanup actions when exiting the state."""
        pass

    def update(self) -> baseState:
        """Update the model.

        Returns:
            baseState: Optional class of state to transition into.
        """
        pass
