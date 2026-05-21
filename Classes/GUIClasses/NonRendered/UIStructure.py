from Modules.Core.ErrorHandler import ThrowError, ThrowWarning
from Modules.Core.CoreGUI.GUIElementsList import addGuiAsset, destoryGuiAsset
from Classes.GUIClasses.GuiBase import GuiBase

class UIStructure():
    def __init__(self):
        self.Enabled = True
        self.Parent: GuiBase = "game"
        #self.Children = [] UIStructures can't have children
        self._GUIKey = addGuiAsset(self)

    def __setattr__(self, name, value):
        if name == "Parent":
            self._setParent(value)
        #This has to happen after _setParent as _setParent has to remove children from the previous parent
        super.__setattr__(self, name, value)

    def _setParent(self, parent):
        if parent == "game":
            return

        if self.Parent != "game":
            #means object had a parent
            self.Parent._removeChild(self._GUIKey)

        #add child
        parent._addChild(self._GUIKey)

    def _addChild(self, _):
        ThrowWarning("Add child method was performed on a UI Structure this class doesn't allow children")

    def _removeChild(self, _):
        ThrowWarning("Remove child method was performed on a UI Structure this class doesn't allow children")

    def renderChildren(self):
        ThrowError("Render children method was performed on a UI Structure this class doesn't allow children therfore can't render children")

    def render(self):
        pass

    def destroy(self):
        destoryGuiAsset(self._GUIKey)