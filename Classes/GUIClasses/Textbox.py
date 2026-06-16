import time
from Classes.GUIClasses.TextButton import TextButton
from Modules.Core.CoreGUI.TextboxHandler import addTextboxAsset, destoryTextboxAsset


def is_valid_chr(n):  # basically
    return isinstance(n, int) and 0 <= n <= 0x10FFFF


FLASH_INTERVAL = 0.5


class Textbox(TextButton):
    def __init__(self):
        super().__init__()
        # print("created new text box button")
        # print(self._GUIKey)
        self.PlaceholderText = "This is placeholder text!"
        self.Text = self.PlaceholderText
        self.IsTyping = False
        self.Button.MouseButton1Up.Connect(self.startTyping)
        self.Button.MouseButton2Up.Connect(self.startTyping)
        self.Button.ClickOff.Connect(self.stopTyping)
        self.FlashTimer = (
            time.time()
        )  # used to track the flashing | line to display when a textbox is active
        self.CursorVisible = True  # tracks whether the cursor should be visible

        addTextboxAsset(self)

    def startTyping(self):
        # print("starting typing", self.Name)
        self.IsTyping = True

    def stopTyping(self):
        # print('stop typing', self.Name)
        self.IsTyping = False

    def typing(self, keycode):
        if not is_valid_chr(keycode):
            # keycode is not able to be translated to a string therefore remove it
            # print("invalid keycode")
            return

        if not self.IsTyping:
            # print("typing typing typing but can't")
            return
        if keycode == 8:
            # this is on an backspace key press
            self.Text = self.Text[:-1]

            return
        if keycode == 13:
            # this is on an enter key press
            self.stopTyping(self)
            return
        # print(self.Text + chr(keycode))
        SetText = self.Text + chr(keycode)
        self.Text = SetText

    def render(self, screen, screenSize, posOffset):
        realText = self.Text

        if self.IsTyping:
            currentTime = time.time()

            if currentTime - self.FlashTimer >= FLASH_INTERVAL:
                self.CursorVisible = not self.CursorVisible
                self.FlashTimer = currentTime

            if self.CursorVisible:
                self.Text = realText + "|"
            else:
                self.Text = realText + " "

        super().render(screen, screenSize, posOffset)

        # Restore actual text value
        self.Text = realText
