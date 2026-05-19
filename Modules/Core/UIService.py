from Modules.Core.CoreGUI.GUIElementsList import GuiAssets
from Modules.Core.ErrorHandler import ThrowError, ThrowWarning

#Classes
from Classes.GUIClasses.GuiBase import GuiBase
from Classes.GUIClasses.NonRendered.UIStructure import UIStructure

<<<<<<< Updated upstream

def addGuiAsset(asset):
    key = CreateUniqueKeyForMap(GuiAssets)
    GuiAssets[key] = asset
    return key


def destoryGuiAsset(key):
    GuiAssets[key] = None
=======
#UI Structure Ordering
StructureOrdering = [
    "UIAspectRatio",
    "UIListLayout"
]
>>>>>>> Stashed changes


def _renderChildren(asset, screen):
    if len(asset.Children) == 0:
        return
<<<<<<< Updated upstream

    for child in _sortByZindex(asset.Children):
        if not child.Visible:
            continue
        child.render(screen, asset.AbsoluteSize, asset.AbsolutePos)
        _renderChildren(child, screen)
=======
    
    for child in _sortAssets(asset.Children):
        if isinstance(child, UIStructure):
            if not child.Enabled:
                continue
            child.render()
        elif isinstance(child, GuiBase):
            if not child.Visible:
                continue
            child.render(screen, asset.AbsoluteSize, asset.AbsolutePos)
            _renderChildren(child, screen)

def _sortByStructure(AssetList):
    def getSortVal(a):
        ObjectName = type(a).__name__
        orderI = StructureOrdering.index(ObjectName)

        if not orderI:
            ThrowWarning(f"When sorting Structure UI elements found an element that isn't in the sorting list; ClassName:{ObjectName}")
            orderI = 0

        return orderI


    AssetList.sort(key=getSortVal, reverse=False)
    return AssetList
>>>>>>> Stashed changes


def _sortByZindex(AssetList):
<<<<<<< Updated upstream
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
=======
    def getSortVal(a):
        return a.zIndex


    AssetList.sort(key=getSortVal, reverse=False)
    return AssetList

def _sortAssets(AssetList):
    
    renderedAssets = []
    structureAssets = []

    for assetKey in AssetList:
        asset = GuiAssets[assetKey]
        if isinstance(asset, UIStructure):
            structureAssets.append(asset)
        else:
            renderedAssets.append(asset)

    renderedAssets = _sortByZindex(renderedAssets)
    structureAssets = _sortByStructure(structureAssets)


    return structureAssets + renderedAssets



    

def RenderAssets(screen, screenSize):


    for asset in _sortAssets(GuiAssets.keys()):
        if asset.Parent != "game": 
            #if the asset's parent isn't game that 
            #means that the assets will 
            #be render by it's parent
>>>>>>> Stashed changes
            continue
        if not asset.Visible:
            continue
        asset.render(screen, screenSize)
        _renderChildren(asset, screen)
