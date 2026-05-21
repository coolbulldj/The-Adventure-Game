from GeneralFunctions import CreateUniqueKeyForMap

TextboxAssets = {}


def addTextboxAsset(asset):
    key = CreateUniqueKeyForMap(TextboxAssets)
    TextboxAssets[key] = asset
    return key


def destoryTextboxAsset(key):
    TextboxAssets[key] = None


def triggerTyping(char):
    for asset in TextboxAssets.values():
        asset.typing(char)
