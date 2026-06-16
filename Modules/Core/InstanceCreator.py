from typing import Literal, TypeAlias, overload

from Modules.Core.ErrorHandler import ThrowError

from Classes.GUIClasses.GuiBase import GuiBase
from Classes.GUIClasses.Frame import Frame
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.TextButton import TextButton
from Classes.GUIClasses.Textbox import Textbox
from Classes.GUIClasses.ScrollingFrame import ScrollingFrame
from Classes.GUIClasses.ImageLabel import Image
from Classes.GUIClasses.Button import Button

from Classes.GUIClasses.NonRendered.UIStructure import UIStructure
from Classes.GUIClasses.NonRendered.UICorner import UICorner
from Classes.GUIClasses.NonRendered.UIGridLayout import UIGridLayout
from Classes.GUIClasses.NonRendered.UIListLayout import UIListLayout
from Classes.GUIClasses.NonRendered.UIStroke import UIStroke
from Classes.GUIClasses.NonRendered.UIAspectRatio import UIAspectRatio

_GUI_CLASSES = {
    "Frame": Frame,
    "TextLabel": TextLabel,
    "TextButton": TextButton,
    "Textbox": Textbox,
    "ScrollingFrame": ScrollingFrame,
    "Image": Image,
    "Button": Button,
    "UICorner": UICorner,
    "UIGridLayout": UIGridLayout,
    "UIListLayout": UIListLayout,
    "UIStroke": UIStroke,
    "UIAspectRatio": UIAspectRatio,
}

_EXCLUDE_CLASSES = [
    "GuiBase",
    "UIStructure",
]

GuiClassName: TypeAlias = Literal[
    "Frame",
    "TextLabel",
    "TextButton",
    "Textbox",
    "ScrollingFrame",
    "Image",
    "Button",
    "UICorner",
    "UIGridLayout",
    "UIListLayout",
    "UIStroke",
    "UIAspectRatio",
]

GuiInstance: TypeAlias = (
    Frame
    | TextLabel
    | TextButton
    | Textbox
    | ScrollingFrame
    | Image
    | Button
    | UICorner
    | UIGridLayout
    | UIListLayout
    | UIStroke
    | UIAspectRatio
)


@overload
def createNewInstance(className: Literal["Frame"]) -> Frame: ...


@overload
def createNewInstance(className: Literal["TextLabel"]) -> TextLabel: ...


@overload
def createNewInstance(className: Literal["TextButton"]) -> TextButton: ...


@overload
def createNewInstance(className: Literal["Textbox"]) -> Textbox: ...


@overload
def createNewInstance(className: Literal["ScrollingFrame"]) -> ScrollingFrame: ...


@overload
def createNewInstance(className: Literal["Image"]) -> Image: ...


@overload
def createNewInstance(className: Literal["Button"]) -> Button: ...


@overload
def createNewInstance(className: Literal["UICorner"]) -> UICorner: ...


@overload
def createNewInstance(className: Literal["UIGridLayout"]) -> UIGridLayout: ...


@overload
def createNewInstance(className: Literal["UIListLayout"]) -> UIListLayout: ...


@overload
def createNewInstance(className: Literal["UIStroke"]) -> UIStroke: ...


@overload
def createNewInstance(className: Literal["UIAspectRatio"]) -> UIAspectRatio: ...


@overload
def createNewInstance(className: str) -> GuiInstance | None: ...


def createNewInstance(className: str) -> GuiInstance | None:
    if className in _EXCLUDE_CLASSES:
        ThrowError(
            f"Class {className} is cannot be created by InstanceCreator as it is only a base class"
        )
        return None

    guiClass = _GUI_CLASSES.get(className)
    if guiClass is None:
        ThrowError(f"Unknown GUI class name; ClassName:{className}")
        return None

    if className == "Button":
        return guiClass([0, 0], [0, 0])

    return guiClass()
