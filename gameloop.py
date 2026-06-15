import Modules.Gameloop.UIHandler as UIHandler
from Modules.Gameloop.UI.Scripts.MainScreenHandler import Tick as MainScreenTick

UIHandler.MenuFrame.Visible = False
UIHandler.LoginScreen.Visible = False
UIHandler.AccountSelectScreen.Visible = False

countDown = 0


def hideFrame():
    UIHandler.MenuFrame.Visible = False
    UIHandler.AccountSelectScreen.Visible = True


UIHandler.PlayB.Button.MouseButton1Up.Connect(hideFrame)


def run(deltaTime: float):
    global countDown
    countDown += deltaTime
    MainScreenTick(deltaTime)
