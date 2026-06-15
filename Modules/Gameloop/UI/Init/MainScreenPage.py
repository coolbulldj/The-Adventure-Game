# GUI Classes
from Classes.GUIClasses.Frame import Frame
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.Textbox import Textbox
from Classes.GUIClasses.ImageLabel import Image
from Classes.GUIClasses.ScrollingFrame import ScrollingFrame
from Classes.GUIClasses.NonRendered.UIGridLayout import UIGridLayout
from Classes.GUIClasses.NonRendered.UIListLayout import UIListLayout
from Classes.GUIClasses.NonRendered.UIStroke import UIStroke
from Classes.GUIClasses.NonRendered.UICorner import UICorner

# ---------------------------------------------------------------------------
# Shared styling
# ---------------------------------------------------------------------------

PANEL_COLOR = (18, 18, 22)
PANEL_ACCENT = (35, 35, 42)
STAT_TITLE_COLOR = (150, 150, 160)
STAT_VALUE_COLOR = (240, 240, 245)
HEADER_COLOR = (255, 60, 60)
STROKE_SIZE = 0.025
CORNER_SIZE = 0.04

# Column layout (Pos values assume default anchor [0.5, 0.5] unless overridden)
MARGIN = 0.012
SIDE_WIDTH = 0.22
CENTER_WIDTH = 1 - (SIDE_WIDTH * 2) - (MARGIN * 4)
PANEL_HEIGHT = 0.96


def StylePanel(frame, transparency=0):
    frame.BackgroundColor = PANEL_COLOR
    frame.BackgroundTransparency = transparency
    corner = UICorner()
    corner.Size = CORNER_SIZE
    corner.Parent = frame
    stroke = UIStroke()
    stroke.Size = STROKE_SIZE
    stroke.Color = (60, 60, 70)
    stroke.Parent = frame
    return frame


def MakeSectionHeader(text, parent):
    header = TextLabel()
    header.Size = [1, 0.08]
    header.AnchorPoint = [0.5, 0.5]
    header.Font = "pressstart2p"
    header.TextColor = HEADER_COLOR
    header.Text = text
    header.BackgroundTransparency = 1
    header.TextWrapped = False
    header.Parent = parent
    return header


def MakeStatRow(statKey, title, initialValue, parent):
    row = Frame()
    row.Size = [1, 0.085]
    row.AnchorPoint = [0.5, 0.5]
    row.BackgroundColor = PANEL_ACCENT
    row.BackgroundTransparency = 0.15
    row.Parent = parent

    rowCorner = UICorner()
    rowCorner.Size = 0.08
    rowCorner.Parent = row

    titleLabel = TextLabel()
    titleLabel.Size = [0.42, 1]
    titleLabel.AnchorPoint = [0, 0.5]
    titleLabel.Pos = [0.04, 0.5]
    titleLabel.Font = "pressstart2p"
    titleLabel.TextColor = STAT_TITLE_COLOR
    titleLabel.Text = title
    titleLabel.BackgroundTransparency = 1
    titleLabel.TextWrapped = False
    titleLabel.Parent = row

    valueLabel = TextLabel()
    valueLabel.Name = statKey
    valueLabel.Size = [0.5, 1]
    valueLabel.AnchorPoint = [1, 0.5]
    valueLabel.Pos = [0.96, 0.5]
    valueLabel.Font = "pressstart2p"
    valueLabel.TextColor = STAT_VALUE_COLOR
    valueLabel.Text = initialValue
    valueLabel.BackgroundTransparency = 1
    valueLabel.TextWrapped = False
    valueLabel.Parent = row

    return valueLabel


# ---------------------------------------------------------------------------
# Main screen root
# ---------------------------------------------------------------------------

MainScreen = Frame()
MainScreen.Size = [1, 1]
MainScreen.AnchorPoint = [0.5, 0.5]
MainScreen.Pos = [0.5, 0.5]
MainScreen.BackgroundTransparency = 1
MainScreen.Visible = True



# ---------------------------------------------------------------------------
# Left column — player stats + inventory
# ---------------------------------------------------------------------------

StatsHolder = Frame()
StatsHolder.Name = "StatsHolder"
StatsHolder.Size = [SIDE_WIDTH, PANEL_HEIGHT]
StatsHolder.AnchorPoint = [0, 0.5]
StatsHolder.Pos = [MARGIN, 0.5]
StatsHolder.Parent = MainScreen
StylePanel(StatsHolder)

StatsHolderLayout = UIListLayout()
StatsHolderLayout.Padding = 0.015
StatsHolderLayout.Parent = StatsHolder

StatsPanel = Frame()
StatsPanel.Name = "StatsPanel"
StatsPanel.Size = [1, 0.54]
StatsPanel.AnchorPoint = [0.5, 0.5]
StatsPanel.BackgroundTransparency = 1
StatsPanel.Parent = StatsHolder

StatsLayout = UIListLayout()
StatsLayout.Padding = 0.02
StatsLayout.Parent = StatsPanel

MakeSectionHeader("PLAYER", StatsPanel)
StatNameLabel = MakeStatRow("StatName", "Name", "Traveler", StatsPanel)
StatAgeLabel = MakeStatRow("StatAge", "Age", "25", StatsPanel)
StatGenderLabel = MakeStatRow("StatGender", "Gender", "Unknown", StatsPanel)
StatHealthLabel = MakeStatRow("StatHealth", "Health", "100", StatsPanel)
StatFoodLabel = MakeStatRow("StatFood", "Food", "80", StatsPanel)
StatHungerLabel = MakeStatRow("StatHunger", "Hunger", "15", StatsPanel)

InventoryHeader = TextLabel()
InventoryHeader.Size = [1, 0.05]
InventoryHeader.AnchorPoint = [0.5, 0.5]
InventoryHeader.Font = "pressstart2p"
InventoryHeader.TextColor = HEADER_COLOR
InventoryHeader.Text = "INVENTORY"
InventoryHeader.BackgroundTransparency = 1
InventoryHeader.TextWrapped = False
InventoryHeader.Parent = StatsHolder

InventoryFrame = ScrollingFrame()
InventoryFrame.Name = "InventoryFrame"
InventoryFrame.BackgroundColor = (28, 28, 34)
InventoryFrame.Size = [1, 0.38]
InventoryFrame.AnchorPoint = [0.5, 0.5]
InventoryFrame.Parent = StatsHolder

InventoryLayout = UIGridLayout()
InventoryLayout.X_Padding = 0.03
InventoryLayout.Y_Padding = 0.03
InventoryLayout.Parent = InventoryFrame

# ---------------------------------------------------------------------------
# Center column — environment, story log, input
# ---------------------------------------------------------------------------

CenterColumn = Frame()
CenterColumn.Name = "CenterColumn"
CenterColumn.Size = [CENTER_WIDTH, PANEL_HEIGHT]
CenterColumn.AnchorPoint = [0.5, 0.5]
CenterColumn.Pos = [0.5, 0.5]
CenterColumn.BackgroundTransparency = 1
CenterColumn.Parent = MainScreen

CenterLayout = UIListLayout()
CenterLayout.Padding = 0.015
CenterLayout.Parent = CenterColumn

EnvironmentPanel = Frame()
EnvironmentPanel.Name = "EnvironmentPanel"
EnvironmentPanel.Size = [1, 0.2]
EnvironmentPanel.AnchorPoint = [0.5, 0.5]
EnvironmentPanel.Parent = CenterColumn
StylePanel(EnvironmentPanel)

EnvironmentImage = Image()
EnvironmentImage.Name = "EnvironmentImage"
EnvironmentImage.Size = [1, 0.72]
EnvironmentImage.AnchorPoint = [0.5, 0]
EnvironmentImage.Pos = [0.5, 0]
EnvironmentImage.ImagePath = (
    "Assets\\Images\\Backgrounds\\RedFrontierGamebackground.png"
)
EnvironmentImage.Parent = EnvironmentPanel

LocationLabel = TextLabel()
LocationLabel.Name = "LocationLabel"
LocationLabel.Size = [1, 0.26]
LocationLabel.AnchorPoint = [0.5, 1]
LocationLabel.Pos = [0.5, 1]
LocationLabel.Font = "pressstart2p"
LocationLabel.TextColor = (255, 220, 180)
LocationLabel.Text = "Red Frontier — Outpost Gate"
LocationLabel.BackgroundColor = (0, 0, 0)
LocationLabel.BackgroundTransparency = 0.45
LocationLabel.TextWrapped = False
LocationLabel.Parent = EnvironmentPanel

MainScroll = ScrollingFrame()
MainScroll.Name = "MainScroll"
MainScroll.Size = [1, 0.58]
MainScroll.AnchorPoint = [0.5, 0.5]
MainScroll.BackgroundColor = (22, 22, 28)
MainScroll.zIndex = 2
MainScroll.Parent = CenterColumn
StylePanel(MainScroll, transparency=0.15)

MainScrollPlaceholder = TextLabel()
MainScrollPlaceholder.Size = [0.9, 0.15]
MainScrollPlaceholder.AnchorPoint = [0.5, 0]
MainScrollPlaceholder.Pos = [0.5, 0.06]
MainScrollPlaceholder.Font = "pressstart2p"
MainScrollPlaceholder.TextColor = (180, 180, 190)
MainScrollPlaceholder.Text = "Adventure log appears here..."
MainScrollPlaceholder.BackgroundTransparency = 1
MainScrollPlaceholder.TextWrapped = True
MainScrollPlaceholder.Parent = MainScroll

MainTextbox = Textbox()
MainTextbox.Name = "MainTextbox"
MainTextbox.Font = "pressstart2p"
MainTextbox.Size = [1, 0.1]
MainTextbox.AnchorPoint = [0.5, 0.5]
MainTextbox.BackgroundColor = (30, 30, 36)
MainTextbox.TextColor = (255, 255, 255)
MainTextbox.Text = ""
MainTextbox.Parent = CenterColumn

MainTextboxStroke = UIStroke()
MainTextboxStroke.Size = 0.03
MainTextboxStroke.Color = (80, 80, 90)
MainTextboxStroke.Parent = MainTextbox

MainTextboxCorner = UICorner()
MainTextboxCorner.Size = 0.06
MainTextboxCorner.Parent = MainTextbox

# Right side NPC details
NPCDetails = Frame()
NPCDetails.Name = "NPCDetails"
NPCDetails.Size = [SIDE_WIDTH, PANEL_HEIGHT]
NPCDetails.AnchorPoint = [1, 0.5]
NPCDetails.Pos = [1 - MARGIN, 0.5]
NPCDetails.Parent = MainScreen
StylePanel(NPCDetails)

NPCDetailsLayout = UIListLayout()
NPCDetailsLayout.Padding = 0.025
NPCDetailsLayout.Parent = NPCDetails

MakeSectionHeader("NPC DETAILS", NPCDetails)

NPCPortrait = Image()
NPCPortrait.Name = "NPCPortrait"
NPCPortrait.Size = [1, 0.28]
NPCPortrait.AnchorPoint = [0.5, 0.5]
NPCPortrait.BackgroundColor = (30, 30, 36)
NPCPortrait.ImagePath = ""
NPCPortrait.Parent = NPCDetails

NPCPortraitStroke = UIStroke()
NPCPortraitStroke.Size = 0.03
NPCPortraitStroke.Color = (70, 70, 80)
NPCPortraitStroke.Parent = NPCPortrait

NPCNameLabel = TextLabel()
NPCNameLabel.Name = "NPCNameLabel"
NPCNameLabel.Size = [1, 0.1]
NPCNameLabel.AnchorPoint = [0.5, 0.5]
NPCNameLabel.Font = "pressstart2p"
NPCNameLabel.TextColor = (255, 200, 120)
NPCNameLabel.Text = "—"
NPCNameLabel.BackgroundTransparency = 1
NPCNameLabel.TextWrapped = False
NPCNameLabel.Parent = NPCDetails

NPCDescriptionLabel = TextLabel()
NPCDescriptionLabel.Name = "NPCDescriptionLabel"
NPCDescriptionLabel.Size = [1, 0.45]
NPCDescriptionLabel.AnchorPoint = [0.5, 0.5]
NPCDescriptionLabel.Font = "pressstart2p"
NPCDescriptionLabel.TextColor = (190, 190, 200)
NPCDescriptionLabel.Text = "Approach an NPC to learn more."
NPCDescriptionLabel.BackgroundTransparency = 1
NPCDescriptionLabel.TextWrapped = True
NPCDescriptionLabel.Parent = NPCDetails
