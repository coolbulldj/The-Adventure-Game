from Modules.Gameloop.UI.Init.AccountSelectionPage import NewAccountB, AccountScrollFrame, MakeAccountCard


def Load(accountList):
    def new():
        MakeAccountCard("testing!", 1)
    NewAccountB.Button.MouseButton1Up.Connect(new)