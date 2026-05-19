from Modules.Core.CoreGUI.GUIElementsList import addGuiAsset, destoryGuiAsset
from Modules.Core.ErrorHandler import ThrowError, ThrowWarning


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

        self.Parent = "game"
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
<<<<<<< Updated upstream
            ThrowWarning(
                f"Warning attempting to remove a child from a parent while child isn't a child of said parent; ClassName:{type(self)}"
            )
=======
            ThrowWarning(f"Warning attempting to remove a child from a parent while child isn't a child of said parent; ClassName:{type(self).__name__}")
>>>>>>> Stashed changes
            return

        self.Children.remove(child)

    def render(self, screenSize, positionOffset=[0, 0]):
        self.AbsoluteSize = [self.Size[0] * screenSize[0], self.Size[1] * screenSize[1]]
        self.AbsolutePos = [
            self.Pos[0] * screenSize[0]
            - self.AbsoluteSize[0] * self.AnchorPoint[0]
            + positionOffset[0],
            self.Pos[1] * screenSize[1]
            - self.AbsoluteSize[1] * self.AnchorPoint[1]
            + positionOffset[1],
        ]

    def destroy(self):
        destoryGuiAsset(self._GUIKey)
