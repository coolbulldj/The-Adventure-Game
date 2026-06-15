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
from Modules.Gameloop.UI.Init.StartMenuPage import MenuFrame, PlayB, SettingsB, CreditsB
from Modules.Gameloop.UI.Init.MainScreenPage import MainScreen
from Modules.Gameloop.UI.Scripts.MainScreenHandler import Load as MainScreenLoad

# Load functions
# from Modules.Gameloop.UI.Scripts.AccountHandler import Load as AHLoad

# AHLoad([])
MainScreenLoad()

MainScreen.Visible = True
