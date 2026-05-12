import Modules.Gameloop.UIHandler as UIHandler


def run(screen, screenSize):
    UIHandler.Background.render(screen, screenSize)
    UIHandler.Title.render(screen, screenSize)
    UIHandler.PlayB.render(screen, screenSize)