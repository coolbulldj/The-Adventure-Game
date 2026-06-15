from Modules.Gameloop.UI.Init.AccountSelectionPage import (
    NewAccountB,
    AccountSelectScreen,
    MakeAccountCard,
)
from Modules.Gameloop.UI.Init.LoginPage import LoginScreen, LoginB
from Modules.Gameloop.UI.Scripts.LoginHandler import SetLoginState, GetAccountDetails


def Load(accountList):
    count = 0

    def new():
        AccountSelectScreen.Visible = False
        SetLoginState("Create")
        LoginScreen.Visible = True

    def AttemptLogin():
        AccountSelectScreen.Visible = False
        SetLoginState("Login")
        LoginScreen.Visible = True
        print("logining?")

    def DeleteAccount():
        pass

    def CreateNewAccount():
        LoginScreen.Visible = False
        AccountSelectScreen.Visible = True
        Username, Password = GetAccountDetails()
        nonlocal count
        count += 1
        card = MakeAccountCard(Username, count)
        SelectB = card.FindFirstChild("SelectB")
        DeleteB = card.FindFirstChild("DeleteB")
        def test():
            print('select button working1')
        SelectB.Button.MouseButton1Up.Connect(test)



    NewAccountB.Button.MouseButton1Up.Connect(new)
    LoginB.Button.MouseButton1Up.Connect(CreateNewAccount)
    
