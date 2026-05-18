from GeneralFunctions import CreateUniqueKeyForMap

GuiAssets = {}


def addGuiAsset(asset):
    key = CreateUniqueKeyForMap(GuiAssets)
    GuiAssets[key] = asset
    return key


def destoryGuiAsset(key):
    GuiAssets[key] = None


def _renderChildren(asset, screen):
    if len(asset.Children) == 0:
        return

    for child in _sortByZindex(asset.Children):
        if not child.Visible:
            continue
        child.render(screen, asset.AbsoluteSize, asset.AbsolutePos)
        _renderChildren(child, screen)


def _sortByZindex(AssetList):
    Sortedlist = []

    for assetKey in AssetList:
        asset = GuiAssets[assetKey]
        Sortedlist.append(asset)

    def getSortVal(a):
        return a.zIndex

    Sortedlist.sort(key=getSortVal, reverse=False)
    return Sortedlist


def RenderAssets(screen, screenSize):
    for asset in _sortByZindex(GuiAssets.keys()):
        if asset.Parent != "game":
            # if the asset's parent isn't game that
            # means that the assets will
            # be render by it's parent
            continue
        if not asset.Visible:
            continue
        asset.render(screen, screenSize)
        _renderChildren(asset, screen)
