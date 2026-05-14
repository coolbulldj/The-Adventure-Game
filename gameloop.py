import Modules.Gameloop.UIHandler as UIHandler


countDown = 0

# def hideFrame():
#     UIHandler.ButtonsFrame.Visible = False

# UIHandler.PlayB.Button.MouseButton1Up.Connect(hideFrame)

def run(deltaTime:float):
    global countDown
    countDown += deltaTime
