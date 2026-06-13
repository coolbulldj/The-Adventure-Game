# GUI Classes
from Classes.GUIClasses.Frame import Frame
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.TextButton import TextButton
from Classes.GUIClasses.ImageLabel import Image
from Classes.GUIClasses.ScrollingFrame import ScrollingFrame
from Classes.GUIClasses.NonRendered.UIListLayout import UIListLayout
from Classes.GUIClasses.NonRendered.UIStroke import UIStroke
from Classes.GUIClasses.NonRendered.UICorner import UICorner

# ---------------------------------------------------------------
# Account Selection Screen
# ---------------------------------------------------------------

AccountSelectScreen = Frame()
AccountSelectScreen.Size = [1, 1]
AccountSelectScreen.Pos = [0.5, 0.5]
AccountSelectScreen.BackgroundTransparency = 1
AccountSelectScreen.Visible = False
AccountSelectScreen.zIndex = 1

AccountSelectBackground = Image()
AccountSelectBackground.Size = [1, 1]
AccountSelectBackground.ImagePath = (
    "Assets\Images\Backgrounds\RedFrontierGamebackground.png"
)
AccountSelectBackground.zIndex = 2
AccountSelectBackground.Parent = AccountSelectScreen

# ---------------------------------------------------------------
# Center panel
# ---------------------------------------------------------------

AccountSelectPanel = Frame()
AccountSelectPanel.Size = [0.5, 0.75]
AccountSelectPanel.Pos = [0.5, 0.5]
AccountSelectPanel.BackgroundTransparency = 0
AccountSelectPanel.BackgroundColor = (20, 20, 20)
AccountSelectPanel.zIndex = 3
AccountSelectPanel.Parent = AccountSelectScreen

AccountSelectPanelCorner = UICorner()
AccountSelectPanelCorner.Parent = AccountSelectPanel

AccountSelectPanelLayout = UIListLayout()
AccountSelectPanelLayout.Padding = 0.03
AccountSelectPanelLayout.Parent = AccountSelectPanel

# ---------------------------------------------------------------
# Header
# ---------------------------------------------------------------

AccountSelectTitle = TextLabel()
AccountSelectTitle.Size = [1, 0.1]
AccountSelectTitle.Font = "pressstart2p"
AccountSelectTitle.TextColor = (255, 255, 255)
AccountSelectTitle.Text = "SELECT ACCOUNT"
AccountSelectTitle.BackgroundTransparency = 1
AccountSelectTitle.zIndex = 4
AccountSelectTitle.Parent = AccountSelectPanel

# ---------------------------------------------------------------
# Scrolling list of account cards
# ---------------------------------------------------------------

AccountScrollFrame = ScrollingFrame()
AccountScrollFrame.Size = [0.95, 0.7]
AccountScrollFrame.BackgroundTransparency = 0
AccountScrollFrame.ScrollingBackgroundColor = (0, 255, 0)
AccountScrollFrame.zIndex = 4
AccountScrollFrame.Parent = AccountSelectPanel

AccountScrollLayout = UIListLayout()
AccountScrollLayout.Padding = 0.1
AccountScrollLayout.Parent = AccountScrollFrame

# ---------------------------------------------------------------
# Account card template (repeated per account at runtime)
# Naming convention: AccountCard_{n}, AccountCardSelectB_{n}, etc.
# ---------------------------------------------------------------


def MakeAccountCard(username: str, index):
    card = Frame()
    card.Size = [1, 0.22]
    card.BackgroundColor = (35, 35, 35)
    card.BackgroundTransparency = 0
    card.Name = f"AccountCard_{index}"
    card.zIndex = 1
    card.Parent = AccountScrollFrame

    cardCorner = UICorner()
    cardCorner.Parent = card

    cardStroke = UIStroke()
    cardStroke.Size = 0.02
    cardStroke.Parent = card

    # Account name label (left-aligned via position offset)
    cardName = TextLabel()
    cardName.Size = [0.55, 0.6]
    cardName.Pos = [0.3, 0.5]
    cardName.Font = "pressstart2p"
    cardName.TextColor = (220, 220, 220)
    cardName.Text = username
    cardName.BackgroundTransparency = 1
    cardName.Name = f"AccountCardName_{index}"
    cardName.zIndex = 6
    cardName.Parent = card

    # Select button
    selectB = TextButton()
    selectB.Size = [0.25, 0.55]
    selectB.Pos = [0.68, 0.5]
    selectB.Font = "pressstart2p"
    selectB.TextColor = (255, 255, 255)
    selectB.BackgroundColor = (50, 120, 50)
    selectB.Text = "Select"
    selectB.Name = "SelectB"
    selectB.zIndex = 6
    selectB.Parent = card

    selectStroke = UIStroke()
    selectStroke.Size = 0.03
    selectStroke.Parent = selectB

    # Delete button
    deleteB = TextButton()
    deleteB.Size = [0.18, 0.55]
    deleteB.Pos = [0.9, 0.5]
    deleteB.Font = "pressstart2p"
    deleteB.TextColor = (255, 60, 60)
    deleteB.BackgroundColor = (60, 20, 20)
    deleteB.Text = "Del"
    deleteB.Name = "DeleteB"
    deleteB.zIndex = 6
    deleteB.Parent = card

    deleteStroke = UIStroke()
    deleteStroke.Size = 0.03
    deleteStroke.Parent = deleteB

    return card


# ---------------------------------------------------------------
# New Account button (bottom of panel, outside scroll)
# ---------------------------------------------------------------

NewAccountB = TextButton()
NewAccountB.Size = [0.6, 0.08]
NewAccountB.Font = "pressstart2p"
NewAccountB.TextColor = (255, 200, 0)
NewAccountB.BackgroundColor = (30, 30, 30)
NewAccountB.Text = "+ New Account"
NewAccountB.Name = "NewAccountB"
NewAccountB.zIndex = 4
NewAccountB.Parent = AccountSelectPanel

NewAccountStroke = UIStroke()
NewAccountStroke.Size = 0.04
NewAccountStroke.Parent = NewAccountB
