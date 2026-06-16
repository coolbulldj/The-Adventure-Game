from Modules.Gameloop.UI.Scripts import MainScreenHandler
import Modules.Gameloop.UI.Scripts.ChallengeHandler as ChallengeHandler
import Modules.Configs.StoryConfig as StoryConfig

ActComplete = False
DialogOptionsDisplayed = False
OpeningDisplayed = False
CurrentDialogOptions = []


def GetCurrentEvent(currentAct, currentReputation):
    if currentAct >= len(StoryConfig.StoryConfig):
        return None

    actConfig = StoryConfig.StoryConfig[currentAct]
    for event in actConfig:
        if event["RequiredReputation"] == currentReputation:
            return event
    return None


def DisplayOpeningDialog(currentAct, currentReputation):
    event = GetCurrentEvent(currentAct, currentReputation)
    if event is None:
        return

    textlabel = MainScreenHandler.DisplayScrollText(event["DialogueOpening"])
    textlabel.Name = f"OpeningDialog;Act{currentAct};Reputation{currentReputation}"


def DisplayDialogOption(text, optionNum, currentAct, currentReputation):
    textlabel = MainScreenHandler.DisplayScrollText(f"{optionNum}." + text)
    textlabel.Name = f"OpeningDialog;Act{currentAct};Reputation{currentReputation}"


def DisplayDialogOptions(currentAct, currentReputation):
    global CurrentDialogOptions, DialogOptionsDisplayed

    event = GetCurrentEvent(currentAct, currentReputation)
    if event is None:
        return

    CurrentDialogOptions = []
    index = 0

    for dialogOption in event["DialoguePositiveRepOptions"]:
        index += 1
        CurrentDialogOptions.append({
            "RepuationChange": 1,
            "Dialog": dialogOption,
        })
        DisplayDialogOption(dialogOption, index, currentAct, currentReputation)

    for dialogOption in event["DialogueNegativeRepOptions"]:
        index += 1
        CurrentDialogOptions.append({
            "RepuationChange": -1,
            "Dialog": dialogOption,
        })
        DisplayDialogOption(dialogOption, index, currentAct, currentReputation)

    DialogOptionsDisplayed = True


def CompleteAct():
    global ActComplete
    ActComplete = True


def Reset():
    global ActComplete, DialogOptionsDisplayed, OpeningDisplayed, CurrentDialogOptions

    ActComplete = False
    DialogOptionsDisplayed = False
    OpeningDisplayed = False
    CurrentDialogOptions = []
    ChallengeHandler.Reset()


def Tick(enteredText, currentAct, currentReputation):
    global OpeningDisplayed, ActComplete, CurrentDialogOptions, DialogOptionsDisplayed

    if not OpeningDisplayed:
        DisplayOpeningDialog(currentAct, currentReputation)
        OpeningDisplayed = True

    if not ActComplete:
        if ChallengeHandler.Tick(enteredText, currentAct):
            ActComplete = True
        return None

    if not DialogOptionsDisplayed:
        DisplayDialogOptions(currentAct, currentReputation)

    if not enteredText:
        return None

    if not enteredText.isdigit():
        return None

    searchIndex = int(enteredText) - 1
    if searchIndex < 0 or searchIndex >= len(CurrentDialogOptions):
        return None

    currentOption = CurrentDialogOptions[searchIndex]
    textlabel = MainScreenHandler.DisplayScrollText("You: " + currentOption["Dialog"])
    textlabel.Name = f"DialogSpoken;Act{currentAct};Reputation{currentReputation}"

    DialogOptionsDisplayed = False
    OpeningDisplayed = False
    ActComplete = False
    ChallengeHandler.Reset()

    return {
        "act": currentAct + 1,
        "reputation": currentReputation + currentOption["RepuationChange"],
    }
