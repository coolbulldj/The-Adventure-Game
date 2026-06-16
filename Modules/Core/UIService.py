from Modules.Core.CoreGUI.GUIElementsList import GuiAssets
from Modules.Core.ErrorHandler import ThrowError, ThrowWarning

# Classes
from Classes.GUIClasses.GuiBase import GuiBase
from Classes.GUIClasses.NonRendered.UIStructure import UIStructure

# UI Structure Ordering
StructureOrdering = [
    "UIAspectRatio",
    "UIListLayout",
    "UIGridLayout",
    "UICorner",
    "UIStroke",
]


def _sortByStructure(AssetList):
    def getSortVal(a):
        ObjectName = type(a).__name__
        orderI = StructureOrdering.index(ObjectName)

        if not orderI:
            ThrowWarning(
                f"When sorting Structure UI elements found an element that isn't in the sorting list; ClassName:{ObjectName}"
            )
            orderI = 0

        return orderI

    AssetList.sort(key=getSortVal, reverse=False)
    return AssetList


def _sortByZindex(AssetList):
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
            # if the asset's parent isn't game that
            # means that the assets will
            # be render by it's parent
            continue
        if not asset.Visible:
            continue
        asset.render(screen, screenSize)
