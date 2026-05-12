#GUI Classes
from Classes.GUIClasses.Frame import Frame
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.TextButton import TextButton
from Classes.GUIClasses.ImageLabel import Image


Background = Image()
Background.Size = [1,1]
Background.ImagePath = "Assets\Images\Backgrounds\RedFrontierGamebackground.png"

Title = TextLabel()
Title.Size = [0.5, 0.25]
Title.Pos = [0.5, 0.2]
Title.Font = "pressstart2p"
Title.Text = "Red Frontier"

PlayB = TextButton()
PlayB.Size = [0.1, 0.1]
PlayB.Pos = [0.05,0.5]
PlayB.Font = "pressstart2p"
PlayB.TextColor = (255,0,0)
PlayB.Text = "Play"
