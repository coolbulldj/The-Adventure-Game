from Modules.Core.CoreGUI.GUIElementsList import addGuiAsset, destoryGuiAsset, GuiAssets
from Modules.Core.ErrorHandler import ThrowError, ThrowWarning

# UI Structure Ordering
StructureOrdering = ["UIAspectRatio", "UIListLayout", "UICorner", "UIStroke"]


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


class GuiBase:
    def __init__(self):
        self.Pos = [0.5, 0.5]
        self.Size = [0.5, 0.5]
        self.AnchorPoint = [0.5, 0.5]  # determines where the position
        self.AbsolutePos = []
        self.AbsoluteSize = []
        self.BackgroundColor = (0, 0, 255)
        self.BackgroundTransparency = 0
        self.zIndex = 1
        self.Visible = True
        self.BorderRadius = 0 #this is edit by the UI corner class.

        self.Parent = "game"
        self.Name = "UnknownName"
        self.Children: list[GuiBase] = []
        self._GUIKey = addGuiAsset(self)

    def __setattr__(self, name, value):
        if name == "Parent":
            self._setParent(value)
        # This has to happen after _setParent as _setParent has to remove children from the previous parent
        super.__setattr__(self, name, value)

    def _setParent(self, parent):
        if parent == "game":
            return

        if self.Parent != "game":
            # means object had a parent
            self.Parent._removeChild(self._GUIKey)

        # add child
        parent._addChild(self._GUIKey)

    def _addChild(self, child):
        self.Children.append(child)

    def _removeChild(self, child):
        if child not in self.Children:
            ThrowWarning(
                f"Warning attempting to remove a child from a parent while child isn't a child of said parent; ClassName:{type(self).__name__}"
            )
            return

        self.Children.remove(child)

    # these are former methods for rendering children
    # def _sortChildren(self):
    #     renderedAssets = []
    #     structureAssets = []

    #     for assetKey in self.Children:
    #         asset = GuiAssets[assetKey]
    #         if isinstance(asset, GuiBase):
    #             renderedAssets.append(asset)
    #         else:
    #             structureAssets.append(asset)

    #     renderedAssets = _sortByZindex(renderedAssets)
    #     structureAssets = _sortByStructure(structureAssets)

    #     return structureAssets + renderedAssets

    # def renderChildren(self, screen):
    #     AssetList = self._sortChildren()
    #     for child in AssetList:
    #         if isinstance(child, GuiBase):
    #             # rendering a GuiBase
    #             if not child.Visible:
    #                 continue
    #             child.render(
    #                 screen, self.AbsoluteSize, self.LastFrame, self.AbsolutePos
    #             )
    #         else:
    #             # rendering a UI Structure
    #             if not child.Enabled:
    #                 continue
    #             child.render(screen)

    def _sortUIStructures(self):
        structureAssets = []

        for assetKey in self.Children:
            asset = GuiAssets[assetKey]
            if not isinstance(asset, GuiBase):
                structureAssets.append(asset)
        return structureAssets

    def _sortUIAssets(self):
        renderedAssets = []

        for assetKey in self.Children:
            asset = GuiAssets[assetKey]
            if isinstance(asset, GuiBase):
                renderedAssets.append(asset)

        renderedAssets = _sortByZindex(renderedAssets)

        return renderedAssets

    def renderUIStructures(self, screen):
        structureAssets = self._sortUIStructures()

        for asset in structureAssets:
            asset.render(screen)

    def renderUIAssets(self, screen):
        renderedAssets = self._sortUIAssets()

        for asset in renderedAssets:
            asset.render(screen, self.AbsoluteSize, self.AbsolutePos)

    def render(self, screenSize, positionOffset=[0, 0]):
        # print(screenSize, LastFrame, positionOffset, self.__class__.__name__)
        self.AbsoluteSize = [self.Size[0] * screenSize[0], self.Size[1] * screenSize[1]]
        self.AbsolutePos = [
            round(
                self.Pos[0] * screenSize[0]
                - self.AbsoluteSize[0] * self.AnchorPoint[0]
                + positionOffset[0]
            ),
            round(
                self.Pos[1] * screenSize[1]
                - self.AbsoluteSize[1] * self.AnchorPoint[1]
                + positionOffset[1]
            ),
        ]
    def FindFirstChild(self, QueryName, returnKey: bool = False):
        for key in self.Children:
            child = GuiAssets[key]
            if child.Name == QueryName:
                if returnKey:
                    return key
                else:
                    return child

    def FindFirstDescendant(self, QueryName):
        pass

    def FindFirstChildOfClass(self, QueryName, returnKey: bool = False):
        for key in self.Children:
            child = GuiAssets[key]
            if child.__class__.__name__ == QueryName:
                if returnKey:
                    return key
                else:
                    return child

    def FindFirstDescendantOfClass(self, QueryName):
        pass

    def destroy(self):
        destoryGuiAsset(self._GUIKey)
