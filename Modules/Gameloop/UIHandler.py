# This module acts as a registery for UI assets which can then be asscessed by gameloop
from Modules.Gameloop.UI.Init.LoginPage import (
    LoginScreen,
    LoginB,
    UsernameInput,
    PasswordInput,
)
from Modules.Gameloop.UI.Init.AccountSelectionPage import (
    AccountSelectScreen,
    NewAccountB,
)
from Modules.Gameloop.UI.Init.MenuPage import (
    MenuFrame,
    PlayB,
    SettingsB,
    CreditsB,
    SettingsFrame,
    SettingsBackB,
    CreditsFrame,
    CreditsBackB,
)
from Modules.Gameloop.UI.Init.MainScreenPage import MainScreen
from Modules.Gameloop.UI.Init.CreationScreen import (
    CreationScreen,
    ConfirmB,
    NameInput,
    AgeInput,
    MaleB,
    FemaleB,
    OtherB,
)

MenuFrame.Visible = False
LoginScreen.Visible = False
AccountSelectScreen.Visible = False
CreationScreen.Visible = False

# Load functions
# from Modules.Gameloop.UI.Scripts.AccountHandler import Load as AHLoad
# from Modules.Gameloop.UI.Scripts.CreationHandler import Load as CHLoad

# AHLoad([])
# CHLoad()

MainScreen.Visible = True
