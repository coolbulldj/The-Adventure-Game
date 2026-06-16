# from Modules.Core import InputService
# import Modules.Gameloop.UIHandler as UIHandler
# #UI Handler Modules
import Modules.Gameloop.UI.Scripts.ActHandler as ActHandler
# import Modules.Gameloop.UI.Scripts.CreationHandler as CreationHandler
# import Modules.Gameloop.UI.Scripts.LoginHandler as LoginHandler
# import Modules.Gameloop.UI.Scripts.AccountHandler as AccountHandler
from Modules.Core.Data import DataHandler
from Modules.Gameloop.UI.Init import MenuPage
import Modules.Gameloop.UI.Scripts.MenuHandler as MenuHandler
import Modules.Gameloop.UI.Scripts.AccountHandler as AccountHandler
#load all modules
MenuHandler.Load()
AccountHandler.Load()

currentAct = 0
currentReputation = 0


def run(deltaTime: float):
    global currentAct, currentReputation

    currentAccountId = AccountHandler.GetAccountID()

    if not currentAccountId:
        return

    #print(deltaTime)
    # enteredText = None

    # if MainScreenPage.MainTextbox.Text != "":
    #     if InputService.HeldKeys:
    #         if 13 in InputService.HeldKeys: #the enter key
    #             enteredText = MainScreenPage.MainTextbox.Text
    #             MainScreenPage.MainTextbox.Text = ""

    # stateChanges = ActHandler.Tick(enteredText, currentAct, currentReputation)
    # if stateChanges:
    #     currentAct = stateChanges["act"]
    #     currentReputation = stateChanges["reputation"]
    #     DataHandler.SetDataValue(currentAccountId, "act", currentAct)
    #     DataHandler.SetDataValue(currentAccountId, "reputation", currentReputation)
