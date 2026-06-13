# GUI Classes
from Classes.GUIClasses.Frame import Frame
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.TextButton import TextButton
from Classes.GUIClasses.ImageLabel import Image
from Classes.GUIClasses.ScrollingFrame import ScrollingFrame
from Classes.GUIClasses.Textbox import Textbox
from Classes.GUIClasses.NonRendered.UIListLayout import UIListLayout
from Classes.GUIClasses.NonRendered.UIStroke import UIStroke
from Classes.GUIClasses.NonRendered.UICorner import UICorner

# THIS MODULE SHOULD ONLY BE USED FOR THE CREATION OF ASSETS, NOT FOR FUNCTIONALITY!

# Menu
Background = Image()
Background.Size = [1, 1]
Background.ImagePath = "Assets\Images\Backgrounds\RedFrontierGamebackground.png"

Title = TextLabel()
Title.Size = [0.5, 0.2]
Title.Pos = [0.5, 0.2]
Title.BackgroundTransparency = 1
Title.Font = "pressstart2p"
Title.Text = "Red Frontier"

BUTTON_SIZE = [1, 0.27]
STROKE_SIZE = 0.04

PlayB = TextButton()
PlayB.Size = BUTTON_SIZE
PlayB.Font = "pressstart2p"
PlayB.TextColor = (255, 0, 0)
PlayB.Text = "Play"
PlayB.Name = "PlayB"

PlayStroke = UIStroke()
PlayStroke.Size = STROKE_SIZE
PlayStroke.Parent = PlayB

SettingsB = TextButton()
SettingsB.Size = BUTTON_SIZE
SettingsB.Font = "pressstart2p"
SettingsB.TextColor = (255, 0, 0)
SettingsB.Text = "Settings"
SettingsB.Name = "SettingsB"

SettingsStroke = UIStroke()
SettingsStroke.Size = STROKE_SIZE
SettingsStroke.Parent = SettingsB

CreditsB = TextButton()
CreditsB.Size = BUTTON_SIZE
CreditsB.Font = "pressstart2p"
CreditsB.TextColor = (255, 0, 0)
CreditsB.Text = "Credits"
CreditsB.Name = "CreditsB"

CreditsStroke = UIStroke()
CreditsStroke.Size = STROKE_SIZE
CreditsStroke.Parent = CreditsB

ButtonsFrame = Frame()
ButtonsFrame.Size = [0.4, 0.5]
ButtonsFrame.Pos = [0.5, 0.6]
ButtonsFrame.BackgroundTransparency = 1
ButtonsFrame.BackgroundColor = (0, 255, 0)

ButtonsFrameListLayout = UIListLayout()
ButtonsFrameListLayout.Padding = 0.08
ButtonsFrameListLayout.Parent = ButtonsFrame

MenuFrame = Frame()
MenuFrame.Size = [1, 1]
MenuFrame.Pos = [0.5, 0.5]
MenuFrame.BackgroundTransparency = 1
MenuFrame.zIndex = 1

PlayB.Parent = ButtonsFrame
SettingsB.Parent = ButtonsFrame
CreditsB.Parent = ButtonsFrame
ButtonsFrame.Visible = True
Background.Parent = MenuFrame
ButtonsFrame.Parent = MenuFrame
Title.Parent = MenuFrame