from Classes.Adventurer import Adventurer
from Modules.Gameloop.UI.Init.MainScreenPage import (
    StatNameLabel,
    StatAgeLabel,
    StatGenderLabel,
    StatHealthLabel,
    StatFoodLabel,
    StatHungerLabel,
    LocationLabel,
    EnvironmentImage,
    NPCNameLabel,
    NPCDescriptionLabel,
    NPCPortrait,
)

Player = Adventurer("Traveler", "Unknown", 25)
CurrentLocation = "Red Frontier — Outpost Gate"
CurrentEnvironmentImage = (
    "Assets\\Images\\Backgrounds\\RedFrontierGamebackground.png"
)

_statTimer = 0


def UpdatePlayerStats():
    StatNameLabel.Text = Player.Name
    StatAgeLabel.Text = str(Player.Age)
    StatGenderLabel.Text = Player.Gender
    StatHealthLabel.Text = str(int(Player.Health))
    StatFoodLabel.Text = str(int(Player.Food))
    StatHungerLabel.Text = str(int(Player.Hunger))


def SetEnvironment(location, imagePath=None):
    global CurrentLocation, CurrentEnvironmentImage

    CurrentLocation = location
    LocationLabel.Text = location

    if imagePath:
        CurrentEnvironmentImage = imagePath
        EnvironmentImage.ImagePath = imagePath


def SetNPCDetails(name="—", description="Approach an NPC to learn more.", imagePath=""):
    NPCNameLabel.Text = name
    NPCDescriptionLabel.Text = description
    NPCPortrait.ImagePath = imagePath


def Tick(deltaTime):
    global _statTimer

    _statTimer += deltaTime
    if _statTimer < 2:
        return

    _statTimer = 0

    Player.Hunger = min(100, Player.Hunger + 1)
    if Player.Hunger > 60:
        Player.Food = max(0, Player.Food - 1)
    if Player.Food < 30:
        Player.Health = max(0, Player.Health - 1)

    UpdatePlayerStats()


def Load():
    SetEnvironment(CurrentLocation, CurrentEnvironmentImage)
    SetNPCDetails()
    UpdatePlayerStats()
