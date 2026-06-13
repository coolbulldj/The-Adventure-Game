from Classes.CoreClasses.EventClass import Event
from Modules.Core.CoreGUI.ButtonHandler import AddButton


class Button:
    def __init__(self, pos, size):
        self.AbsolutePos = size
        self.AbsoluteSize = pos
        self.MouseButton1Up = Event()
        self.MouseButton1Down = Event()
        self.MouseButton2Up = Event()
        self.MouseButton2Down = Event()
        self.ClickOff = Event()
        self.LastFrame = 0  # use to track whether the button was rendered for the frame if not then the button events shall not trigger.
        AddButton(self)

    def check_mouse_hit(self, mouseHit, currentFrame):
        # print(self.LastFrame, currentFrame)
        if self.LastFrame != currentFrame:
            return
        # bounds of the button
        lx, hx = (
            self.AbsolutePos[0],
            self.AbsolutePos[0] + self.AbsoluteSize[0],
        )  # low x, high x
        ly, hy = (
            self.AbsolutePos[1],
            self.AbsolutePos[1] + self.AbsoluteSize[1],
        )  # low y, high y

        mx, my = mouseHit
        # print("checking mouse hit:", mx, my, "bounding x(s) are:", lx, hx)
        if mx < lx or hx < mx:
            return False
        elif my < ly or hy < my:
            return False

        return True

    def render(self, pos, size, LastFrame):
        self.AbsolutePos = size
        self.AbsoluteSize = pos
        self.LastFrame = LastFrame
        # print(self.LastFrame)
