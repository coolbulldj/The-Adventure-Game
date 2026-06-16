import Modules.Core.InstanceCreator as InstanceCreator

# THIS MODULE SHOULD ONLY BE USED FOR THE CREATION OF ASSETS, NOT FOR FUNCTIONALITY!

INPUT_SIZE = [0.9, 0.1]
LABEL_SIZE = [0.9, 0.07]
STROKE_SIZE = 0.02
BUTTON_STROKE_SIZE = 0.04
GENDER_BUTTON_SIZE = [0.28, 0.12]

# ---------------------------------------------------------------
# Character creation screen
# ---------------------------------------------------------------

CreationScreen = InstanceCreator.createNewInstance("Frame")
CreationScreen.Size = [1, 1]
CreationScreen.Pos = [0.5, 0.5]
CreationScreen.BackgroundTransparency = 1
CreationScreen.Visible = False
CreationScreen.zIndex = 1

CreationBackground = InstanceCreator.createNewInstance("Image")
CreationBackground.Size = [1, 1]
CreationBackground.ImagePath = (
    "Assets\\Images\\Backgrounds\\RedFrontierGamebackground.png"
)
CreationBackground.zIndex = 2
CreationBackground.Parent = CreationScreen

CreationFormFrame = InstanceCreator.createNewInstance("Frame")
CreationFormFrame.Size = [0.45, 0.72]
CreationFormFrame.Pos = [0.5, 0.5]
CreationFormFrame.BackgroundTransparency = 0
CreationFormFrame.BackgroundColor = (20, 20, 20)
CreationFormFrame.zIndex = 3
CreationFormFrame.Parent = CreationScreen

CreationFormCorner = InstanceCreator.createNewInstance("UICorner")
CreationFormCorner.Parent = CreationFormFrame

CreationFormLayout = InstanceCreator.createNewInstance("UIListLayout")
CreationFormLayout.Padding = 0.035
CreationFormLayout.Parent = CreationFormFrame

# --- Header ---
CreationTitle = InstanceCreator.createNewInstance("TextLabel")
CreationTitle.Size = [1, 0.12]
CreationTitle.Font = "pressstart2p"
CreationTitle.TextColor = (255, 255, 255)
CreationTitle.Text = "CREATE CHARACTER"
CreationTitle.BackgroundTransparency = 1
CreationTitle.zIndex = 4
CreationTitle.Parent = CreationFormFrame

# --- Name ---
NameLabel = InstanceCreator.createNewInstance("TextLabel")
NameLabel.Size = LABEL_SIZE
NameLabel.Font = "pressstart2p"
NameLabel.TextColor = (200, 200, 200)
NameLabel.Text = "Name:"
NameLabel.BackgroundTransparency = 1
NameLabel.zIndex = 4
NameLabel.Parent = CreationFormFrame

NameInput = InstanceCreator.createNewInstance("Textbox")
NameInput.Size = INPUT_SIZE
NameInput.Font = "pressstart2p"
NameInput.BackgroundColor = (40, 40, 40)
NameInput.TextColor = (255, 255, 255)
NameInput.PlaceholderText = "Enter your name"
NameInput.Text = NameInput.PlaceholderText
NameInput.Name = "NameInput"
NameInput.zIndex = 4
NameInput.Parent = CreationFormFrame

NameStroke = InstanceCreator.createNewInstance("UIStroke")
NameStroke.Size = STROKE_SIZE
NameStroke.Parent = NameInput

# --- Age ---
AgeLabel = InstanceCreator.createNewInstance("TextLabel")
AgeLabel.Size = LABEL_SIZE
AgeLabel.Font = "pressstart2p"
AgeLabel.TextColor = (200, 200, 200)
AgeLabel.Text = "Age:"
AgeLabel.BackgroundTransparency = 1
AgeLabel.zIndex = 4
AgeLabel.Parent = CreationFormFrame

AgeInput = InstanceCreator.createNewInstance("Textbox")
AgeInput.Size = INPUT_SIZE
AgeInput.Font = "pressstart2p"
AgeInput.BackgroundColor = (40, 40, 40)
AgeInput.TextColor = (255, 255, 255)
AgeInput.PlaceholderText = "Enter your age"
AgeInput.Text = AgeInput.PlaceholderText
AgeInput.Name = "AgeInput"
AgeInput.zIndex = 4
AgeInput.Parent = CreationFormFrame

AgeStroke = InstanceCreator.createNewInstance("UIStroke")
AgeStroke.Size = STROKE_SIZE
AgeStroke.Parent = AgeInput

# --- Gender ---
GenderLabel = InstanceCreator.createNewInstance("TextLabel")
GenderLabel.Size = LABEL_SIZE
GenderLabel.Font = "pressstart2p"
GenderLabel.TextColor = (200, 200, 200)
GenderLabel.Text = "Gender:"
GenderLabel.BackgroundTransparency = 1
GenderLabel.zIndex = 4
GenderLabel.Parent = CreationFormFrame

GenderFrame = InstanceCreator.createNewInstance("Frame")
GenderFrame.Size = [0.9, 0.14]
GenderFrame.BackgroundTransparency = 1
GenderFrame.zIndex = 4
GenderFrame.Parent = CreationFormFrame

GenderGridLayout = InstanceCreator.createNewInstance("UIGridLayout")
GenderGridLayout.X_Padding = 0.04
GenderGridLayout.Y_Padding = 0
GenderGridLayout.Parent = GenderFrame

MaleB = InstanceCreator.createNewInstance("TextButton")
MaleB.Size = GENDER_BUTTON_SIZE
MaleB.Font = "pressstart2p"
MaleB.TextColor = (255, 255, 255)
MaleB.BackgroundColor = (40, 40, 40)
MaleB.Text = "Male"
MaleB.Name = "MaleB"
MaleB.zIndex = 5
MaleB.Parent = GenderFrame

MaleStroke = InstanceCreator.createNewInstance("UIStroke")
MaleStroke.Size = STROKE_SIZE
MaleStroke.Parent = MaleB

FemaleB = InstanceCreator.createNewInstance("TextButton")
FemaleB.Size = GENDER_BUTTON_SIZE
FemaleB.Font = "pressstart2p"
FemaleB.TextColor = (255, 255, 255)
FemaleB.BackgroundColor = (40, 40, 40)
FemaleB.Text = "Female"
FemaleB.Name = "FemaleB"
FemaleB.zIndex = 5
FemaleB.Parent = GenderFrame

FemaleStroke = InstanceCreator.createNewInstance("UIStroke")
FemaleStroke.Size = STROKE_SIZE
FemaleStroke.Parent = FemaleB

OtherB = InstanceCreator.createNewInstance("TextButton")
OtherB.Size = GENDER_BUTTON_SIZE
OtherB.Font = "pressstart2p"
OtherB.TextColor = (255, 255, 255)
OtherB.BackgroundColor = (40, 40, 40)
OtherB.Text = "Other"
OtherB.Name = "OtherB"
OtherB.zIndex = 5
OtherB.Parent = GenderFrame

OtherStroke = InstanceCreator.createNewInstance("UIStroke")
OtherStroke.Size = STROKE_SIZE
OtherStroke.Parent = OtherB

# --- Confirm ---
ConfirmB = InstanceCreator.createNewInstance("TextButton")
ConfirmB.Size = [0.65, 0.12]
ConfirmB.Font = "pressstart2p"
ConfirmB.TextColor = (255, 0, 0)
ConfirmB.Text = "Begin Adventure"
ConfirmB.Name = "ConfirmB"
ConfirmB.zIndex = 4
ConfirmB.Parent = CreationFormFrame

ConfirmStroke = InstanceCreator.createNewInstance("UIStroke")
ConfirmStroke.Size = BUTTON_STROKE_SIZE
ConfirmStroke.Parent = ConfirmB
