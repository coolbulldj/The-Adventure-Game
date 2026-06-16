Inventory = []


def AddItem(item):
    Inventory.append(item)


def RemoveItem(item):
    Inventory.remove(item)


def GetInventory():
    return Inventory
