from Classes.GUIClasses.GuiBase import GuiBase

class ScrollingFrame(GuiBase):
    def __init__(self):
        super().__init__()
        self.ScrollingBarWidth = 0.1 #done by percentage of size
        self._CanvasSize = [0,0]
        self.AutoCanvasX = False
        self.AutoCanvasY = True

    def mouseMotion(self, motionData):
        pass

    def render(self):
        pass
