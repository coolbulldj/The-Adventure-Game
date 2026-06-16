import Modules.Core.InstanceCreator as InstanceCreator

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
LIST_PADDING = 0.04
LIST_CHILD_WIDTH = 0.96

# Column layout (Pos values assume default anchor [0.5, 0.5] unless overridden)
MARGIN = 0.012
SIDE_WIDTH = 0.22
CENTER_WIDTH = 1 - (SIDE_WIDTH * 2) - (MARGIN * 4)
PANEL_HEIGHT = 0.96


def StylePanel(frame, transparency=0):
    frame.BackgroundColor = PANEL_COLOR
    frame.BackgroundTransparency = transparency
    corner = InstanceCreator.createNewInstance("UICorner")
    corner.Size = CORNER_SIZE
    corner.Parent = frame
    stroke = InstanceCreator.createNewInstance("UIStroke")
    stroke.Size = STROKE_SIZE
    stroke.Color = (60, 60, 70)
    stroke.Parent = frame
    return frame


def MakeSectionHeader(text, parent):
    header = InstanceCreator.createNewInstance("TextLabel")
    header.Size = [LIST_CHILD_WIDTH, 0.07]
    header.AnchorPoint = [0.5, 0.5]
    header.Font = "pressstart2p"
    header.TextColor = HEADER_COLOR
    header.Text = text
    header.BackgroundTransparency = 1
    header.TextWrapped = False
    header.Parent = parent
    return header


def MakeStatRow(statKey, title, initialValue, parent):
    row = InstanceCreator.createNewInstance("Frame")
    row.Size = [LIST_CHILD_WIDTH, 0.078]
    row.AnchorPoint = [0.5, 0.5]
    row.BackgroundColor = PANEL_ACCENT
    row.BackgroundTransparency = 0.15
    row.Parent = parent

    rowCorner = InstanceCreator.createNewInstance("UICorner")
    rowCorner.Size = 0.08
    rowCorner.Parent = row

    titleLabel = InstanceCreator.createNewInstance("TextLabel")
    titleLabel.Size = [0.42, 1]
    titleLabel.AnchorPoint = [0, 0.5]
    titleLabel.Pos = [0.04, 0.5]
    titleLabel.Font = "pressstart2p"
    titleLabel.TextColor = STAT_TITLE_COLOR
    titleLabel.Text = title
    titleLabel.BackgroundTransparency = 1
    titleLabel.TextWrapped = False
    titleLabel.Parent = row

    valueLabel = InstanceCreator.createNewInstance("TextLabel")
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


# Main screen root

MainScreen = InstanceCreator.createNewInstance("Frame")
MainScreen.Size = [1, 1]
MainScreen.AnchorPoint = [0.5, 0.5]
MainScreen.Pos = [0.5, 0.5]
MainScreen.BackgroundTransparency = 1
MainScreen.Visible = True


# player stats & inventory

StatsHolder = InstanceCreator.createNewInstance("Frame")
StatsHolder.Name = "StatsHolder"
StatsHolder.Size = [SIDE_WIDTH, PANEL_HEIGHT]
StatsHolder.AnchorPoint = [0, 0.5]
StatsHolder.Pos = [MARGIN, 0.5]
StatsHolder.Parent = MainScreen
StylePanel(StatsHolder)

StatsHolderLayout = InstanceCreator.createNewInstance("UIListLayout")
StatsHolderLayout.Padding = LIST_PADDING
StatsHolderLayout.Parent = StatsHolder

StatsPanel = InstanceCreator.createNewInstance("Frame")
StatsPanel.Name = "StatsPanel"
StatsPanel.Size = [LIST_CHILD_WIDTH, 0.5]
StatsPanel.AnchorPoint = [0.5, 0.5]
StatsPanel.BackgroundTransparency = 1
StatsPanel.Parent = StatsHolder

StatsLayout = InstanceCreator.createNewInstance("UIListLayout")
StatsLayout.Padding = 0.035
StatsLayout.Parent = StatsPanel

MakeSectionHeader("PLAYER", StatsPanel)
StatNameLabel = MakeStatRow("StatName", "Name", "Traveler", StatsPanel)
StatAgeLabel = MakeStatRow("StatAge", "Age", "25", StatsPanel)
StatGenderLabel = MakeStatRow("StatGender", "Gender", "Unknown", StatsPanel)
StatHealthLabel = MakeStatRow("StatHealth", "Health", "100", StatsPanel)
StatFoodLabel = MakeStatRow("StatFood", "Food", "80", StatsPanel)
StatHungerLabel = MakeStatRow("StatHunger", "Hunger", "15", StatsPanel)

InventoryHeader = InstanceCreator.createNewInstance("TextLabel")
InventoryHeader.Size = [LIST_CHILD_WIDTH, 0.045]
InventoryHeader.AnchorPoint = [0.5, 0.5]
InventoryHeader.Font = "pressstart2p"
InventoryHeader.TextColor = HEADER_COLOR
InventoryHeader.Text = "INVENTORY"
InventoryHeader.BackgroundTransparency = 1
InventoryHeader.TextWrapped = False
InventoryHeader.Parent = StatsHolder

InventoryFrame = InstanceCreator.createNewInstance("ScrollingFrame")
InventoryFrame.Name = "InventoryFrame"
InventoryFrame.BackgroundColor = (28, 28, 34)
InventoryFrame.Size = [LIST_CHILD_WIDTH, 0.34]
InventoryFrame.AnchorPoint = [0.5, 0.5]
InventoryFrame.Parent = StatsHolder

InventoryLayout = InstanceCreator.createNewInstance("UIGridLayout")
InventoryLayout.X_Padding = 0.03
InventoryLayout.Y_Padding = 0.03
InventoryLayout.Parent = InventoryFrame

# environment, story log, input

CenterColumn = InstanceCreator.createNewInstance("Frame")
CenterColumn.Name = "CenterColumn"
CenterColumn.Size = [CENTER_WIDTH, PANEL_HEIGHT]
CenterColumn.AnchorPoint = [0.5, 0.5]
CenterColumn.Pos = [0.5, 0.5]
CenterColumn.BackgroundTransparency = 1
CenterColumn.Parent = MainScreen

CenterLayout = InstanceCreator.createNewInstance("UIListLayout")
CenterLayout.Padding = LIST_PADDING
CenterLayout.Parent = CenterColumn

EnvironmentPanel = InstanceCreator.createNewInstance("Frame")
EnvironmentPanel.Name = "EnvironmentPanel"
EnvironmentPanel.Size = [LIST_CHILD_WIDTH, 0.27]
EnvironmentPanel.AnchorPoint = [0.5, 0.5]
EnvironmentPanel.Parent = CenterColumn
StylePanel(EnvironmentPanel)

EnvironmentImage = InstanceCreator.createNewInstance("Image")
EnvironmentImage.Name = "EnvironmentImage"
EnvironmentImage.Size = [1, 0.72]
EnvironmentImage.AnchorPoint = [0.5, 0]
EnvironmentImage.Pos = [0.5, 0]
EnvironmentImage.ImagePath = (
    "Assets\\Images\\Backgrounds\\RedFrontierGamebackground.png"
)
EnvironmentImage.Parent = EnvironmentPanel

LocationLabel = InstanceCreator.createNewInstance("TextLabel")
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

MainScroll = InstanceCreator.createNewInstance("ScrollingFrame")
MainScroll.Name = "MainScroll"
MainScroll.Size = [LIST_CHILD_WIDTH, 0.52]
MainScroll.AnchorPoint = [0.5, 0.5]
MainScroll.BackgroundColor = (22, 22, 28)
MainScroll.zIndex = 2
MainScroll.Parent = CenterColumn
StylePanel(MainScroll, transparency=0.15)

MainScrollListLayout = InstanceCreator.createNewInstance("UIListLayout")
MainScrollListLayout.Padding = LIST_PADDING
MainScrollListLayout.Parent = MainScroll

MainTextbox = InstanceCreator.createNewInstance("Textbox")
MainTextbox.Name = "MainTextbox"
MainTextbox.Font = "pressstart2p"
MainTextbox.Size = [LIST_CHILD_WIDTH, 0.085]
MainTextbox.AnchorPoint = [0.5, 0.5]
MainTextbox.BackgroundColor = (30, 30, 36)
MainTextbox.TextColor = (255, 255, 255)
MainTextbox.Text = ""
MainTextbox.Parent = CenterColumn

MainTextboxStroke = InstanceCreator.createNewInstance("UIStroke")
MainTextboxStroke.Size = 0.03
MainTextboxStroke.Color = (80, 80, 90)
MainTextboxStroke.Parent = MainTextbox

MainTextboxCorner = InstanceCreator.createNewInstance("UICorner")
MainTextboxCorner.Size = 0.06
MainTextboxCorner.Parent = MainTextbox

# Right side NPC details
NPCDetails = InstanceCreator.createNewInstance("Frame")
NPCDetails.Name = "NPCDetails"
NPCDetails.Size = [SIDE_WIDTH, PANEL_HEIGHT]
NPCDetails.AnchorPoint = [1, 0.5]
NPCDetails.Pos = [1 - MARGIN, 0.5]
NPCDetails.Parent = MainScreen
StylePanel(NPCDetails)

NPCDetailsLayout = InstanceCreator.createNewInstance("UIListLayout")
NPCDetailsLayout.Padding = LIST_PADDING
NPCDetailsLayout.Parent = NPCDetails

MakeSectionHeader("NPC DETAILS", NPCDetails)

NPCPortrait = InstanceCreator.createNewInstance("Image")
NPCPortrait.Name = "NPCPortrait"
NPCPortrait.Size = [LIST_CHILD_WIDTH, 0.26]
NPCPortrait.AnchorPoint = [0.5, 0.5]
NPCPortrait.BackgroundColor = (30, 30, 36)
NPCPortrait.ImagePath = ""
NPCPortrait.Parent = NPCDetails

NPCPortraitStroke = InstanceCreator.createNewInstance("UIStroke")
NPCPortraitStroke.Size = 0.03
NPCPortraitStroke.Color = (70, 70, 80)
NPCPortraitStroke.Parent = NPCPortrait

NPCNameLabel = InstanceCreator.createNewInstance("TextLabel")
NPCNameLabel.Name = "NPCNameLabel"
NPCNameLabel.Size = [LIST_CHILD_WIDTH, 0.085]
NPCNameLabel.AnchorPoint = [0.5, 0.5]
NPCNameLabel.Font = "pressstart2p"
NPCNameLabel.TextColor = (255, 200, 120)
NPCNameLabel.Text = "—"
NPCNameLabel.BackgroundTransparency = 1
NPCNameLabel.TextWrapped = False
NPCNameLabel.Parent = NPCDetails

NPCRoleLabel = InstanceCreator.createNewInstance("TextLabel")
NPCRoleLabel.Name = "NPCRoleLabel"
NPCRoleLabel.Size = [LIST_CHILD_WIDTH, 0.06]
NPCRoleLabel.AnchorPoint = [0.5, 0.5]
NPCRoleLabel.Font = "pressstart2p"
NPCRoleLabel.TextColor = STAT_TITLE_COLOR
NPCRoleLabel.Text = ""
NPCRoleLabel.BackgroundTransparency = 1
NPCRoleLabel.TextWrapped = False
NPCRoleLabel.Parent = NPCDetails

NPCDescriptionLabel = InstanceCreator.createNewInstance("TextLabel")
NPCDescriptionLabel.Name = "NPCDescriptionLabel"
NPCDescriptionLabel.Size = [LIST_CHILD_WIDTH, 0.4]
NPCDescriptionLabel.AnchorPoint = [0.5, 0.5]
NPCDescriptionLabel.Font = "pressstart2p"
NPCDescriptionLabel.TextColor = (190, 190, 200)
NPCDescriptionLabel.Text = "No NPC in focus."
NPCDescriptionLabel.BackgroundTransparency = 1
NPCDescriptionLabel.TextWrapped = True
NPCDescriptionLabel.Parent = NPCDetails