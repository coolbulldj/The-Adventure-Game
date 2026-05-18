from GeneralFunctions import CreateUniqueKeyForMap

ScrollAssets = {}


def addScrollAsset(asset):
    key = CreateUniqueKeyForMap(ScrollAssets)
    ScrollAssets[key] = asset
    return key


def destoryScrollAsset(key):
    ScrollAssets[key] = None


def triggerScrollMotion(motionData):
    for asset in ScrollAssets.values():
        asset.mouseMotion(motionData)
