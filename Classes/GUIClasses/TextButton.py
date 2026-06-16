from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.Button import Button


class TextButton(TextLabel):
    def __init__(self):
        super().__init__()
        self.Button = Button(self.AbsolutePos, self.AbsoluteSize)
        self.Button.Name = ""

    def __setattr__(self, name, value):
        if hasattr(self, "Button"):
            if hasattr(self.Button, name):
                setattr(self.Button, name, value)
        return super().__setattr__(name, value)

    def render(self, *args):
        super().render(*args)
        # print(self.AbsolutePos, self.AbsoluteSize, self.Name)
        self.Button.render(self.AbsolutePos, self.AbsoluteSize)
