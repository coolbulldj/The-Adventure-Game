# GUI Classes
from Classes.GUIClasses.Frame import Frame
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.Textbox import Textbox
from Classes.GUIClasses.ImageLabel import Image
from Classes.GUIClasses.ScrollingFrame import ScrollingFrame
from Classes.GUIClasses.NonRendered.UIGridLayout import UIGridLayout
from Classes.GUIClasses.NonRendered.UIStroke import UIStroke
from Classes.GUIClasses.NonRendered.UICorner import UICorner

MainScreen = Frame()
MainScreen.Size = [1, 1]
MainScreen.Pos = [0.5, 0.5]
MainScreen.BackgroundTransparency = 1

MainScreen.Visible = True

# Menu
Background = Image()
Background.Size = [1, 1]
Background.ImagePath = "Assets\Images\Backgrounds\RedFrontierGamebackground.png"
Background.Parent = MainScreen

MainScroll = ScrollingFrame()
MainScroll.Name = "MainScroll"
MainScroll.BackgroundColor = (255, 255, 255)
MainScroll.zIndex = 2
MainScroll.Pos = [0.5, 0.6]
MainScroll.Parent = MainScreen

MainTextbox = Textbox()
MainTextbox.Name = "MainTextbox"
MainTextbox.Font = "pressstart2p"
MainTextbox.Size = [0.5, 0.1]
MainTextbox.AnchorPoint = [0.5, 1]
MainTextbox.Pos = [0.5, 1]
MainTextbox.Parent = MainScreen

StatsHolder = Frame()
StatsHolder.Name = "StatsHolder"
StatsHolder.Size = [0.25, 1]
StatsHolder.AnchorPoint = [0, 0.5]
StatsHolder.Pos = [0, 0.5]
StatsHolder.BackgroundColor = (0, 0, 0)
StatsHolder.Parent = MainScreen

InventoryFrame = ScrollingFrame()
InventoryFrame.BackgroundColor = (33, 33, 33)
InventoryFrame.Size = [1, 0.5]
InventoryFrame.Parent = StatsHolder

InventoryLayout = UIGridLayout()

InventoryLayout.Parent = InventoryFrame

repeat = 100

for i in range(repeat):
    frame = TextLabel()
    frame.Size = [0.25, 0.25]
    frame.BackgroundColor = (i / repeat * 255, i / repeat * 255, i / repeat * 255)
    frame.Text = f"{i}"
    frame.Parent = InventoryFrame

NPCDetails = Frame()
