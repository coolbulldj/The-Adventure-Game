from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.Button import Button


class TextButton(TextLabel):
    def __init__(self):
        super().__init__()
        self.Button = Button(self.AbsolutePos, self.AbsoluteSize)

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

        if hasattr(self, "Button"):
            # attempt to replicated values to button
            if hasattr(self.Button, name):
                setattr(self.Button, name, value)
