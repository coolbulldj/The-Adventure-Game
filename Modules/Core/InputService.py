from Modules.Core.CoreGUI.TextboxHandler import triggerTyping

HoldTimes = {}
HeldKeys = []

KeyDelay = 0.05  # How long it takes until the input is registered as a key stroke
KeyRepeat = 0.2  # How often a key stroke is registery again while being held


def KeyDown(key):
    HoldTimes[key] = 0


def KeyUp(key):
    if key in HoldTimes:
        del HoldTimes[key]
    if key in HeldKeys:
        HeldKeys.remove(key)


def Tick(dt: float):
    for key, heldTime in HoldTimes.items():
        HoldTimes[key] += dt

        if heldTime > KeyDelay and key not in HeldKeys:
            HeldKeys.append(key)
            HoldTimes[key] -= KeyRepeat
        elif key in HeldKeys:
            HeldKeys.remove(key)

    for key in HeldKeys:
        triggerTyping(key)
