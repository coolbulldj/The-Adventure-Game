from Modules.Core import InstanceCreator
from Modules.Gameloop.UI.Init import MainScreenPage
import Modules.Configs.NPCData as NPCData

SelectedNpcName = None


def DisplayScrollText(text):
    textlabel = InstanceCreator.createNewInstance("TextLabel")
    textlabel.Text = text
    textlabel.Size = [0.9, 0.1]
    textlabel.Font = "pressstart2p"
    textlabel.BackgroundTransparency = 1
    textlabel.Parent = MainScreenPage.MainScroll

    return textlabel


def ClearNpcFocus():
    global SelectedNpcName
    SelectedNpcName = None
    MainScreenPage.NPCNameLabel.Text = "—"
    MainScreenPage.NPCRoleLabel.Text = ""
    MainScreenPage.NPCDescriptionLabel.Text = "No NPC in focus."
    MainScreenPage.NPCPortrait.ImagePath = ""


def DisplayNpc(npcData):
    global SelectedNpcName

    if not npcData:
        ClearNpcFocus()
        return

    SelectedNpcName = npcData.get("DisplayName")
    MainScreenPage.NPCNameLabel.Text = npcData.get("DisplayName", "Unknown")
    MainScreenPage.NPCRoleLabel.Text = npcData.get("Role", "")
    MainScreenPage.NPCDescriptionLabel.Text = npcData.get("Description")
    MainScreenPage.NPCPortrait.ImagePath = npcData.get("ImagePath", "")


def DisplayNpcByName(name):
    DisplayNpc(NPCData.GetNpcByName(name))
