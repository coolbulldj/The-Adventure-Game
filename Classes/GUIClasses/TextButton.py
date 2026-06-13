from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.Button import Button


class TextButton(TextLabel):
    def __init__(self):
        super().__init__()
        self.Button = Button(self.AbsolutePos, self.AbsoluteSize)

    def render(self, screen, screenSize, LastFrame, posOffset):
        super().render(screen, screenSize, LastFrame, posOffset)
        self.Button.render(self.AbsolutePos, self.AbsoluteSize, LastFrame)
