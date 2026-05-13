from Modules.Core.UIService import addGuiAsset, destoryGuiAsset


class GuiBase:
    def __init__(self):
        self.Pos = [0.5, 0.5]
        self.Size = [0.5, 0.5]
        self.AnchorPoint = [0.5, 0.5]  # determines where the position
        self.AbsolutePos = []
        self.AbsoluteSize = []
        self.UIAspectRatio = None
        self.BackgroundColor = (0, 0, 255)
        self.BackgroundTransparency = 0
        self.Visible = True

        self.Parent = "game"
        self.Children = []
        self._GUIKey = addGuiAsset(self)

    def setParent(self, parent):
        if self.Parent != "game":
            #means object had a parent
            self.Parent._removeChild(self)

        #set parent
        self.Parent = parent
        #add child
        parent._addChild(self)
        

    def _addChild(self, child):
        self.Children.append(child)

    def _removeChild(self, child):
        self.Children.remove(child)

    def render(self, screenSize):
        self.AbsoluteSize = [self.Size[0] * screenSize[0], self.Size[1] * screenSize[1]]
        self.AbsolutePos = [
            self.Pos[0] * screenSize[0] - self.AbsoluteSize[0] * self.AnchorPoint[0],
            self.Pos[1] * screenSize[1] - self.AbsoluteSize[1] * self.AnchorPoint[1],
        ]

    def destroy(self):
        destoryGuiAsset(self._GUIKey)
