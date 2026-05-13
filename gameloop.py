import Modules.Gameloop.UIHandler as UIHandler


countDown = 0

def run(deltaTime:float):
    global countDown
    countDown += deltaTime

    if countDown >= 3:
        UIHandler.ButtonsFrame.Visible = False
