from GeneralFunctions import CreateUniqueKeyForMap

GuiAssets = {}


def addGuiAsset(asset):
    key = CreateUniqueKeyForMap(GuiAssets)
    GuiAssets[key] = asset
    return key

def destoryGuiAsset(key):
    GuiAssets[key] = None

def _renderChildren(asset, screen, screenSize):
    if len(asset.Children) == 0:
        return
    
    for child in asset.Children:
        if not child.Visible:
            continue
        child.render(screen, screenSize)
        _renderChildren(child, screen, screenSize)


def RenderAssets(screen, screenSize):
    for asset in GuiAssets.values():
        if asset.Parent != "game": 
            #if the asset's parent isn't game that 
            #means that the assets will 
            #be render by it's parent
            continue
        if not asset.Visible:
            continue
        asset.render(screen, screenSize)
        _renderChildren(asset, screen, screenSize)
