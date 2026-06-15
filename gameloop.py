import Modules.Gameloop.UIHandler as UIHandler

UIHandler.MenuFrame.Visible = True
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
    # print(UIHandler.framesList[len(UIHandler.framesList) - 1].Pos)
