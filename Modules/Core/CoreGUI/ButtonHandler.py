from GeneralFunctions import CreateUniqueKeyForMap

buttons = {}
active_buttons = []


def ActiveButton(key):
    active_buttons.append(key)


def AddButton(button):
    key = CreateUniqueKeyForMap(buttons)

    buttons[key] = button
    return key


def ResetActiveButtons():
    global active_buttons
    active_buttons = []


def CheckButtons(mousePositon, MouseUp: bool, MouseCode: int):
    global active_buttons
    # creates a copy so then if data edits caused by mouse events
    # don't cause a dictionary changed size during iteration error
    for buttonKey in active_buttons:
        button = buttons[buttonKey]
        if not button.check_mouse_hit(mousePositon):
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
                # print("right click")
                button.MouseButton2Down._FireEvent()  # Right Click
