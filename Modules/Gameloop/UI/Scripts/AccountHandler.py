import Modules.Gameloop.UI.Init.LoginPage as LoginPage
import Modules.Gameloop.UI.Init.MenuPage as MenuPage
import Modules.Core.Data.DataHandler as DataHandler
from Modules.Gameloop.UI.Init.AccountSelectionPage import (
    NewAccountB,
    AccountSelectScreen,
    MakeAccountCard,
)

CurrentAccountId = None
PendingAccountId = None


def Load():
    LoginState = "Login"

    def addAccountCard(account_id, username):
        card = MakeAccountCard(username, account_id)
        selectB = card.FindFirstChild("SelectB")
        deleteB = card.FindFirstChild("DeleteB")

        def selectAccount():
            nonlocal LoginState
            global PendingAccountId

            LoginState = "Login"
            PendingAccountId = account_id
            LoginPage.UsernameInput.Text = username
            LoginPage.PasswordInput.Text = ""
            LoginPage.LoginTitle.Text = "LOGIN"
            LoginPage.LoginB.Text = "Submit"
            AccountSelectScreen.Visible = False
            LoginPage.LoginScreen.Visible = True

        def deleteAccount():
            DataHandler.DeleteAccount(account_id)
            card.Visible = False

        selectB.Button.MouseButton1Up.Connect(selectAccount)
        deleteB.Button.MouseButton1Up.Connect(deleteAccount)

    for account_id in DataHandler.GetAccountIds():
        addAccountCard(account_id, DataHandler.GetUsername(account_id))

    def new():
        nonlocal LoginState
        global PendingAccountId

        LoginState = "Create"
        PendingAccountId = None
        LoginPage.UsernameInput.Text = ""
        LoginPage.PasswordInput.Text = ""
        LoginPage.LoginTitle.Text = "CREATE ACCOUNT"
        LoginPage.LoginB.Text = "Create"
        AccountSelectScreen.Visible = False
        LoginPage.LoginScreen.Visible = True

    def CreateNewAccount():
        username = LoginPage.UsernameInput.Text
        password = LoginPage.PasswordInput.Text

        if not username or not password:
            return

        account_id = DataHandler.CreateAccount(username, password)
        DataHandler.SaveAccount(account_id)

        LoginPage.UsernameInput.Text = ""
        LoginPage.PasswordInput.Text = ""
        LoginPage.LoginScreen.Visible = False
        AccountSelectScreen.Visible = True

        addAccountCard(account_id, username)

    def AttemptLogin():
        global CurrentAccountId, PendingAccountId

        username = LoginPage.UsernameInput.Text
        password = LoginPage.PasswordInput.Text
        account_id = DataHandler.VerifyLogin(username, password)

        if account_id is None:
            return

        if PendingAccountId is not None and account_id != PendingAccountId:
            return

        CurrentAccountId = account_id
        PendingAccountId = None
        LoginPage.UsernameInput.Text = ""
        LoginPage.PasswordInput.Text = ""
        LoginPage.LoginScreen.Visible = False
        MenuPage.MenuFrame.Visible = True

    def OpenAccountPage():
        MenuPage.MenuFrame.Visible = False
        AccountSelectScreen.Visible = True

    def OnLoginPress():
        nonlocal LoginState

        if LoginState == "Login":
            AttemptLogin()
        elif LoginState == "Create":
            CreateNewAccount()

    NewAccountB.Button.MouseButton1Up.Connect(new)
    LoginPage.LoginB.Button.MouseButton1Up.Connect(OnLoginPress)
    MenuPage.PlayB.Button.MouseButton1Up.Connect(OpenAccountPage)


def GetAccountID():
    return CurrentAccountId
