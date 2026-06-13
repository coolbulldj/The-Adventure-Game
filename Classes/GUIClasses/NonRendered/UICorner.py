from Classes.GUIClasses.NonRendered.UIStructure import UIStructure
from Classes.GUIClasses.GuiBase import GuiBase
from Modules.Core.CoreGUI.GUIElementsList import GuiAssets


class UICorner(UIStructure):
    def __init__(self):
        super().__init__()
        self.RelativeAxis = (
            "Horoizontal"  # defines which axis the corner is relative to
        )
        self.Size = (
            0  # defines how much of the corner is sized (done in percentage btw)
        )
        self.AbsoluteSize = 0  # defines the corner radius

    def render(self, *args):
        super().render(*args)
