from GUIClasses.TextButton import TextButton


def is_valid_chr(n):  # basically
    return isinstance(n, int) and 0 <= n <= 0x10FFFF


class Textbox(TextButton):
    def __init__(self):
        super().__init__()

        self.PlaceholderText = "This is placeholder text!"
        self.Text = self.PlaceholderText

        self.Button.MouseButton1Up.Connect(self.startTyping)
        self.Button.MouseButton2Up.Connect(self.startTyping)
        self.Button.ClickOff.Connect(self.stopTyping)

    def startTyping(self):
        self.IsTyping = True

    def stopTyping(self):
        self.IsTyping = False

    def typing(self, keycode):
        if not is_valid_chr(keycode):
            # keycode is not able to be translated to a string therefore remove it
            return

        if not self.TypingIn:
            return

        if keycode == 8:
            # this is on an backspace key press
            self.Text = self.Text[:-1]
            return
        if keycode == 13:
            # this is on an enter key press
            self.stopTyping(self)
            return

        SetText = self.Text + chr(keycode)
        self.Text = SetText
