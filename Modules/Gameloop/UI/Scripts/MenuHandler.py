import Modules.Gameloop.UI.Init.MenuPage as MenuPage


def Load():
    MenuPage.CreditsFrame.Visible = False
    MenuPage.SettingsFrame.Visible = False
    def CreditsClicked():
        MenuPage.CreditsFrame.Visible = True

    def SettingsClicked():
        MenuPage.SettingsFrame.Visible = True

    def CloseSettings():
        MenuPage.SettingsFrame.Visible = False

    def CloseCredits():
        MenuPage.CreditsFrame.Visible = False
    

    MenuPage.CreditsB.Button.MouseButton1Up.Connect(CreditsClicked)
    MenuPage.SettingsB.Button.MouseButton1Up.Connect(SettingsClicked)

    MenuPage.CreditsCloseB.Button.MouseButton1Up.Connect(CloseCredits)
    MenuPage.SettingsCloseB.Button.MouseButton1Up.Connect(CloseSettings)