from GeneralFunctions import CreateUniqueKeyForMap

GuiAssets = {}


def addGuiAsset(asset):
    key = CreateUniqueKeyForMap(GuiAssets)
    GuiAssets[key] = asset
    return key


def destoryGuiAsset(key):
    GuiAssets[key] = None
