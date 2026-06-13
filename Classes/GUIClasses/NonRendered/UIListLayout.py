from Classes.GUIClasses.NonRendered.UIStructure import UIStructure
from Classes.GUIClasses.GuiBase import GuiBase
from Modules.Core.CoreGUI.GUIElementsList import GuiAssets


class UIListLayout(UIStructure):
    def __init__(self):
        super().__init__()
        self.Padding = 0.05
        self.AlignmentDirection = "Vertical"

    def render(self, _):
        if self.Parent == "game":
            return
        realPadding = self.Padding

        if realPadding == 0:
            realPadding = -0.005
            # do this so there isn't any gaps between gui assets due to rounding when the elements get rendered
        currentOffset = 0
        for childKey in self.Parent.Children:
            asset = GuiAssets[childKey]

            if not isinstance(asset, GuiBase):
                continue
            asset.Pos = [self.Parent.Pos[0], asset.Size[1] / 2 + currentOffset]
            currentOffset += asset.Size[1] + realPadding
