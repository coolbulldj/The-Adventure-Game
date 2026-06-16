from Modules.Gameloop.UI.Init.CreationScreen import (
    CreationScreen,
    ConfirmB,
    NameInput,
    AgeInput,
    MaleB,
    FemaleB,
    OtherB,
)
from Modules.Gameloop.UI.Init.MainScreenPage import (
    MainScreen,
    StatNameLabel,
    StatAgeLabel,
    StatGenderLabel,
)

GENDER_BUTTONS = {
    "Male": MaleB,
    "Female": FemaleB,
    "Other": OtherB,
}

SelectedGender = "Unknown"
DEFAULT_GENDER_COLOR = (40, 40, 40)
SELECTED_GENDER_COLOR = (50, 120, 50)


def _getInputText(textbox):
    if textbox.Text == textbox.PlaceholderText:
        return ""
    return textbox.Text.strip()


def _selectGender(gender):
    global SelectedGender
    SelectedGender = gender

    for button in GENDER_BUTTONS.values():
        button.BackgroundColor = DEFAULT_GENDER_COLOR

    GENDER_BUTTONS[gender].BackgroundColor = SELECTED_GENDER_COLOR


def GetCreationDetails():
    return _getInputText(NameInput), _getInputText(AgeInput), SelectedGender


def _applyToMainScreen(name, age, gender):
    StatNameLabel.Text = name or "Traveler"
    StatAgeLabel.Text = age or "25"
    StatGenderLabel.Text = gender


def _confirmCreation():
    name, age, gender = GetCreationDetails()

    if not name:
        print("Character creation requires a name.")
        return

    if not age or not age.isdigit():
        print("Character creation requires a valid age.")
        return

    if gender == "Unknown":
        print("Character creation requires a gender selection.")
        return

    _applyToMainScreen(name, age, gender)
    CreationScreen.Visible = False
    MainScreen.Visible = True


def Load():
    MaleB.Button.MouseButton1Up.Connect(lambda: _selectGender("Male"))
    FemaleB.Button.MouseButton1Up.Connect(lambda: _selectGender("Female"))
    OtherB.Button.MouseButton1Up.Connect(lambda: _selectGender("Other"))
    ConfirmB.Button.MouseButton1Up.Connect(_confirmCreation)
