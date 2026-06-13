from GeneralFunctions import CreateUniqueKeyForMap

buttons = {}


def AddButton(button):
    print("new button!")
    key = CreateUniqueKeyForMap(buttons)

    buttons[key] = button
    return key


def CheckButtons(mousePositon, MouseUp: bool, MouseCode: int, CurrentFrame):
     
    for button in buttons.values():
        if not button.check_mouse_hit(mousePositon, CurrentFrame):
            button.ClickOff._FireEvent()
            continue
        if MouseUp:
            if MouseCode == 1:
                button.MouseButton1Up._FireEvent()  # Left Click
            elif MouseCode == 2:
                # will be middle button potentially in the future
                # v.MouseButton1Up._FireEvent()
                pass
            elif MouseCode == 3:
                button.MouseButton2Up._FireEvent()  # Right Click

        else:
            if MouseCode == 1:
                button.MouseButton1Down._FireEvent()  # Left Click
            elif MouseCode == 2:
                # will be middle button potentially in the future
                # v.MouseButton1Up._FireEvent()
                pass
            elif MouseCode == 3:
                button.MouseButton2Down._FireEvent()  # Right Click
                pass
