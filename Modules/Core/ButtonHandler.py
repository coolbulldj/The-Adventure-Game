from GeneralFunctions import CreateUniqueKeyForMap

buttons = {}


def AddButton(button):
    key = CreateUniqueKeyForMap(buttons)

    buttons[key] = button
    return key


def CheckButtons(mousePositon, MouseUp: bool, MouseCode: int):
    for button in buttons.values():
        if not button.check_mousehit(mousePositon):
            continue
        if MouseUp:
            if MouseCode == 1:
                button.MouseButton1Up._FireEvent()
            elif MouseCode == 2:
                button.MouseButton2Up._FireEvent()
            elif MouseCode == 3:
                # will be middle button potentially in the future
                # v.MouseButton1Up._FireEvent()
                pass
        else:
            if MouseCode == 1:
                button.MouseButton1Down._FireEvent()
            elif MouseCode == 2:
                button.MouseButton2Down._FireEvent()
            elif MouseCode == 3:
                # will be middle button potentially in the future
                # v.MouseButton1Up._FireEvent()
                pass
