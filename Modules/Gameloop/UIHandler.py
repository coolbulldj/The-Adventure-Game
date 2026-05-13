# GUI Classes
from Classes.GUIClasses.Frame import Frame
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.TextButton import TextButton
from Classes.GUIClasses.ImageLabel import Image

#THIS MODULE SHOULD ONLY BE USED FOR THE CREATION OF ASSETS, NOT FOR FUNCTIONALITY!

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
PlayB.Size = [0.1, 0.1]
PlayB.Pos = [0.05, 0.5]
PlayB.Font = "pressstart2p"
PlayB.TextColor = (255, 0, 0)
PlayB.Text = "Play"

SettingsB = TextButton()
SettingsB.Size = [0.1, 0.1]
SettingsB.Pos = [0.05, 0.7]
SettingsB.Font = "pressstart2p"
SettingsB.TextColor = (255, 0, 0)
SettingsB.Text = "Settings"

CreditsB = TextButton()
CreditsB.Size = [0.1, 0.1]
CreditsB.Pos = [0.05, 0.9]
CreditsB.Font = "pressstart2p"
CreditsB.TextColor = (255, 0, 0)
CreditsB.Text = "Credits"

ButtonsFrame = Frame()
ButtonsFrame.Size = [0.1, 0.4]
ButtonsFrame.Pos = [0.05, 0.7]
ButtonsFrame.BackgroundColor = (0,255,0)

PlayB.setParent(ButtonsFrame)
SettingsB.setParent(ButtonsFrame)
CreditsB.setParent(ButtonsFrame)
