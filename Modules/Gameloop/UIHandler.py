# GUI Classes
from Classes.GUIClasses.Frame import Frame
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.TextButton import TextButton
from Classes.GUIClasses.ImageLabel import Image
from Classes.GUIClasses.ScrollingFrame import ScrollingFrame
from Classes.GUIClasses.NonRendered.UIListLayout import UIListLayout
from Classes.GUIClasses.Textbox import Textbox

# THIS MODULE SHOULD ONLY BE USED FOR THE CREATION OF ASSETS, NOT FOR FUNCTIONALITY!

# Menu
Background = Image()
Background.Size = [1, 1]
Background.ImagePath = "Assets\Images\Backgrounds\RedFrontierGamebackground.png"

Title = TextLabel()
Title.Size = [0.5, 0.25]
Title.Pos = [0.5, 0.2]
Title.BackgroundTransparency = 1
Title.Font = "pressstart2p"
Title.Text = "Red Frontier"

PlayB = TextButton()
PlayB.Size = [1, 0.2]
PlayB.Pos = [0.5, 0.15]
PlayB.Font = "pressstart2p"
PlayB.TextColor = (255, 0, 0)
PlayB.Text = "Play"

SettingsB = TextButton()
SettingsB.Size = [1, 0.2]
SettingsB.Pos = [0.5, 0.4]
SettingsB.Font = "pressstart2p"
SettingsB.TextColor = (255, 0, 0)
SettingsB.Text = "Settings"

CreditsB = TextButton()
CreditsB.Size = [1, 0.2]
CreditsB.Pos = [0.5, 0.65]
CreditsB.Font = "pressstart2p"
CreditsB.TextColor = (255, 0, 0)
CreditsB.Text = "Credits"

ButtonsFrame = Frame()
ButtonsFrame.Size = [0.1, 0.4]
ButtonsFrame.Pos = [0.05, 0.7]
ButtonsFrame.BackgroundColor = (0,255,0)

MenuFrame = Frame()
MenuFrame.Size = [1, 1]
MenuFrame.Pos = [0.5, 0.5]
MenuFrame.BackgroundTransparency = 0.5
MenuFrame.zIndex = 1

PlayB.Parent = ButtonsFrame
SettingsB.Parent = ButtonsFrame
CreditsB.Parent = ButtonsFrame
ButtonsFrame.Visible = True
Background.Parent = MenuFrame
ButtonsFrame.Parent = MenuFrame

#Main screen
MainScreen = Frame()
MainScreen.Size = [1, 1]
MainScreen.BackgroundColor = (0,255,0)

MessageBox = Textbox()
MessageBox.Parent = MainScreen

# TestScrollFrame = ScrollingFrame()
# TestScrollFrame._CanvasSize = [1, 1]

# TestLayout = UIListLayout()
# TestLayout.Parent = TestScrollFrame

# testFrames = 10

# for i in range(testFrames):
#     TestFrame = Frame()
#     TestFrame.Size = [0.8, 0.1]
#     color = i/testFrames
#     TestFrame.BackgroundColor = (color*255, color*255, color*255)
#     TestFrame.Parent = TestScrollFrame

