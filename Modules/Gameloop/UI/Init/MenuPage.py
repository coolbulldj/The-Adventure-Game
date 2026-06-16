import Modules.Core.InstanceCreator as InstanceCreator

# THIS MODULE SHOULD ONLY BE USED FOR THE CREATION OF ASSETS, NOT FOR FUNCTIONALITY!

# Menu
Background = InstanceCreator.createNewInstance("Image")
Background.Size = [1, 1]
Background.ImagePath = "Assets\Images\Backgrounds\RedFrontierGamebackground.png"

Title = InstanceCreator.createNewInstance("TextLabel")
Title.Size = [0.5, 0.2]
Title.Pos = [0.5, 0.2]
Title.BackgroundTransparency = 1
Title.Font = "pressstart2p"
Title.Text = "Red Frontier"

BUTTON_SIZE = [1, 0.27]
STROKE_SIZE = 0.04
PANEL_SIZE = [0.45, 0.65]
PANEL_COLOR = (20, 20, 20)

PlayB = InstanceCreator.createNewInstance("TextButton")
PlayB.Size = BUTTON_SIZE
PlayB.Font = "pressstart2p"
PlayB.TextColor = (255, 0, 0)
PlayB.Text = "Play"
PlayB.Name = "PlayB"

PlayStroke = InstanceCreator.createNewInstance("UIStroke")
PlayStroke.Size = STROKE_SIZE
PlayStroke.Parent = PlayB

SettingsB = InstanceCreator.createNewInstance("TextButton")
SettingsB.Size = BUTTON_SIZE
SettingsB.Font = "pressstart2p"
SettingsB.TextColor = (255, 0, 0)
SettingsB.Text = "Settings"
SettingsB.Name = "SettingsB"

SettingsStroke = InstanceCreator.createNewInstance("UIStroke")
SettingsStroke.Size = STROKE_SIZE
SettingsStroke.Parent = SettingsB

CreditsB = InstanceCreator.createNewInstance("TextButton")
CreditsB.Size = BUTTON_SIZE
CreditsB.Font = "pressstart2p"
CreditsB.TextColor = (255, 0, 0)
CreditsB.Text = "Credits"
CreditsB.Name = "CreditsB"

CreditsStroke = InstanceCreator.createNewInstance("UIStroke")
CreditsStroke.Size = STROKE_SIZE
CreditsStroke.Parent = CreditsB

ButtonsFrame = InstanceCreator.createNewInstance("Frame")
ButtonsFrame.Size = [0.4, 0.5]
ButtonsFrame.Pos = [0.5, 0.6]
ButtonsFrame.BackgroundTransparency = 1
ButtonsFrame.BackgroundColor = (0, 255, 0)

ButtonsFrameListLayout = InstanceCreator.createNewInstance("UIListLayout")
ButtonsFrameListLayout.Padding = 0.08
ButtonsFrameListLayout.Parent = ButtonsFrame

MenuFrame = InstanceCreator.createNewInstance("Frame")
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


SettingsFrame = InstanceCreator.createNewInstance("Frame")
SettingsFrame.Size = [1, 1]
SettingsFrame.Pos = [0.5, 0.5]
SettingsFrame.BackgroundColor = (0, 0, 0)
SettingsFrame.BackgroundTransparency = 0.45
SettingsFrame.Visible = False
SettingsFrame.zIndex = 2
SettingsFrame.Parent = MenuFrame

SettingsPanel = InstanceCreator.createNewInstance("Frame")
SettingsPanel.Size = PANEL_SIZE
SettingsPanel.Pos = [0.5, 0.5]
SettingsPanel.BackgroundTransparency = 0
SettingsPanel.BackgroundColor = PANEL_COLOR
SettingsPanel.zIndex = 3
SettingsPanel.Parent = SettingsFrame

SettingsPanelCorner = InstanceCreator.createNewInstance("UICorner")
SettingsPanelCorner.Parent = SettingsPanel

SettingsPanelLayout = InstanceCreator.createNewInstance("UIListLayout")
SettingsPanelLayout.Padding = 0.04
SettingsPanelLayout.Parent = SettingsPanel

SettingsTitle = InstanceCreator.createNewInstance("TextLabel")
SettingsTitle.Size = [1, 0.12]
SettingsTitle.Font = "pressstart2p"
SettingsTitle.TextColor = (255, 255, 255)
SettingsTitle.Text = "SETTINGS"
SettingsTitle.BackgroundTransparency = 1
SettingsTitle.Parent = SettingsPanel

SettingsTroll = InstanceCreator.createNewInstance("TextLabel")
SettingsTroll.Size = [1, 0.12]
SettingsTroll.Font = "pressstart2p"
SettingsTroll.TextColor = (255, 255, 255)
SettingsTroll.Text = "this game is too good to have settings"
SettingsTroll.BackgroundTransparency = 1
SettingsTroll.Parent = SettingsPanel

SettingsCloseB = InstanceCreator.createNewInstance("TextButton")
SettingsCloseB.Size = [1, 0.12]
SettingsCloseB.Font = "pressstart2p"
SettingsCloseB.TextColor = (255, 255, 255)
SettingsCloseB.Text = "Close"
SettingsCloseB.Parent = SettingsPanel

# ---------------------------------------------------------------
# Credits overlay
# ---------------------------------------------------------------

CreditsFrame = InstanceCreator.createNewInstance("Frame")
CreditsFrame.Size = [1, 1]
CreditsFrame.Pos = [0.5, 0.5]
CreditsFrame.BackgroundColor = (0, 0, 0)
CreditsFrame.BackgroundTransparency = 0.45
CreditsFrame.Visible = False
CreditsFrame.zIndex = 2
CreditsFrame.Parent = MenuFrame

CreditsPanel = InstanceCreator.createNewInstance("Frame")
CreditsPanel.Size = PANEL_SIZE
CreditsPanel.Pos = [0.5, 0.5]
CreditsPanel.BackgroundTransparency = 0
CreditsPanel.BackgroundColor = PANEL_COLOR
CreditsPanel.Parent = CreditsFrame

CreditsPanelCorner = InstanceCreator.createNewInstance("UICorner")
CreditsPanelCorner.Parent = CreditsPanel

CreditsPanelLayout = InstanceCreator.createNewInstance("UIListLayout")
CreditsPanelLayout.Padding = 0.04
CreditsPanelLayout.Parent = CreditsPanel

CreditsTitle = InstanceCreator.createNewInstance("TextLabel")
CreditsTitle.Size = [1, 0.12]
CreditsTitle.Font = "pressstart2p"
CreditsTitle.TextColor = (255, 255, 255)
CreditsTitle.Text = "CREDITS"
CreditsTitle.BackgroundTransparency = 1
CreditsTitle.Parent = CreditsPanel

CreditsGameNameTitle = InstanceCreator.createNewInstance("TextLabel")
CreditsGameNameTitle.Size = [1, 0.12]
CreditsGameNameTitle.Font = "pressstart2p"
CreditsGameNameTitle.TextColor = (255, 0, 0)
CreditsGameNameTitle.Text = "Red Frontier"
CreditsGameNameTitle.BackgroundTransparency = 1
CreditsGameNameTitle.Parent = CreditsPanel

CreditsTheOnlyCreator = InstanceCreator.createNewInstance("TextLabel")
CreditsTheOnlyCreator.Size = [1, 0.12]
CreditsTheOnlyCreator.Font = "pressstart2p"
CreditsTheOnlyCreator.TextColor = (255, 255, 255)
CreditsTheOnlyCreator.Text = "By Matthew"
CreditsTheOnlyCreator.BackgroundTransparency = 1
CreditsTheOnlyCreator.Parent = CreditsPanel

CreditsCloseB = InstanceCreator.createNewInstance("TextButton")
CreditsCloseB.Size = [1, 0.12]
CreditsCloseB.Font = "pressstart2p"
CreditsCloseB.TextColor = (255, 255, 255)
CreditsCloseB.Text = "Close"
CreditsCloseB.Parent = CreditsPanel


