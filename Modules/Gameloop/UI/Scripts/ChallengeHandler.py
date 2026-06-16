import glob
import random
from Modules.Configs import NPCData
from Modules.Gameloop.UI.Scripts import MainScreenHandler


currentProgress = 0
currentNpc = None
NPCSafe = None
backgroundNpcList = []

for npc in NPCData.GetBackgroundNpcs().keys():
    backgroundNpcList.append(npc)

def SecurityCheck(enteredText):
    global currentNpc, NPCSafe, currentProgress
    if currentProgress >= 5:
        return True
    if not currentNpc:
        randomInt = random.randint(0, len(backgroundNpcList)-1)
        currentNpc = backgroundNpcList[randomInt]

        NPCSafe = False
        if random.random() > 0.25:
            NPCSafe = True

        MainScreenHandler.DisplayNpcByName(currentNpc)
        idText = ""
        if NPCSafe:
            idText = currentNpc + "-CCD1"
        else:
            idText = "<@?J! <#@!" + "-CCD1"

        MainScreenHandler.DisplayScrollText("Presented Id:" + idText)
        MainScreenHandler.DisplayScrollText("1. To clear")
        MainScreenHandler.DisplayScrollText("2. To Detain")
    if not enteredText:
        return


    if enteredText.isdigit(): #note only works for positive ints but for our case this is fine
        #Advance Act
        choosenAction = int(enteredText)
        if choosenAction != 1 and choosenAction != 2:
            return

        currentNpc = None

        if choosenAction != (NPCSafe and 1 or 2):
            MainScreenHandler.DisplayScrollText("You let a rebel get into the protest!")
            return
        if not NPCSafe:
            MainScreenHandler.DisplayScrollText("You succesfully detained a rebel")
        else:
            MainScreenHandler.DisplayScrollText("You succesfully cleared a protester")
        currentProgress += 1



def Reset():
    global currentProgress, currentNpc, NPCSafe

    currentProgress = 0
    currentNpc = None
    NPCSafe = None


def Tick(enteredText, currentAct):
    if currentAct == 0:
        return SecurityCheck(enteredText)