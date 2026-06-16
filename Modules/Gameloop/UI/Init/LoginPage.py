import Modules.Core.InstanceCreator as InstanceCreator

# Login screen
LoginScreen = InstanceCreator.createNewInstance("Frame")
LoginScreen.Size = [1, 1]
LoginScreen.Pos = [0.5, 0.5]
LoginScreen.BackgroundTransparency = 1
LoginScreen.Visible = False
LoginScreen.zIndex = 1

# Background sits behind everything else in the screen
LoginBackground = InstanceCreator.createNewInstance("Image")
LoginBackground.Size = [1, 1]
LoginBackground.ImagePath = "Assets\Images\Backgrounds\RedFrontierGamebackground.png"
LoginBackground.zIndex = 2
LoginBackground.Parent = LoginScreen

# Form container floats above the background
LoginFormFrame = InstanceCreator.createNewInstance("Frame")
LoginFormFrame.Size = [0.4, 0.6]
LoginFormFrame.Pos = [0.5, 0.5]
LoginFormFrame.BackgroundTransparency = 0
LoginFormFrame.BackgroundColor = (20, 20, 20)
LoginFormFrame.zIndex = 3
LoginFormFrame.Parent = LoginScreen

LoginFormCorner = InstanceCreator.createNewInstance("UICorner")
LoginFormCorner.Parent = LoginFormFrame

LoginFormLayout = InstanceCreator.createNewInstance("UIListLayout")
LoginFormLayout.Padding = 0.04
LoginFormLayout.Parent = LoginFormFrame

# --- Header ---
LoginTitle = InstanceCreator.createNewInstance("TextLabel")
LoginTitle.Size = [1, 0.15]
LoginTitle.Font = "pressstart2p"
LoginTitle.TextColor = (255, 255, 255)
LoginTitle.Text = "LOGIN"
LoginTitle.BackgroundTransparency = 1
LoginTitle.zIndex = 4
LoginTitle.Parent = LoginFormFrame

# --- Username ---
UsernameLabel = InstanceCreator.createNewInstance("TextLabel")
UsernameLabel.Size = [0.9, 0.08]
UsernameLabel.Font = "pressstart2p"
UsernameLabel.TextColor = (200, 200, 200)
UsernameLabel.Text = "Username:"
UsernameLabel.BackgroundTransparency = 1
UsernameLabel.zIndex = 4
UsernameLabel.Parent = LoginFormFrame

UsernameInput = InstanceCreator.createNewInstance("Textbox")
UsernameInput.Size = [0.9, 0.12]
UsernameInput.Font = "pressstart2p"
UsernameInput.BackgroundColor = (40, 40, 40)
UsernameInput.TextColor = (255, 255, 255)
UsernameInput.Text = ""
UsernameInput.Name = "UsernameInput"
UsernameInput.zIndex = 4
UsernameInput.Parent = LoginFormFrame

UsernameStroke = InstanceCreator.createNewInstance("UIStroke")
UsernameStroke.Size = 0.02
UsernameStroke.Parent = UsernameInput

# --- Password ---
PasswordLabel = InstanceCreator.createNewInstance("TextLabel")
PasswordLabel.Size = [0.9, 0.08]
PasswordLabel.Font = "pressstart2p"
PasswordLabel.TextColor = (200, 200, 200)
PasswordLabel.Text = "Password:"
PasswordLabel.BackgroundTransparency = 1
PasswordLabel.zIndex = 4
PasswordLabel.Parent = LoginFormFrame

PasswordInput = InstanceCreator.createNewInstance("Textbox")
PasswordInput.Size = [0.9, 0.12]
PasswordInput.Font = "pressstart2p"
PasswordInput.BackgroundColor = (40, 40, 40)
PasswordInput.TextColor = (255, 255, 255)
PasswordInput.Text = ""
PasswordInput.Name = "PasswordInput"
PasswordInput.zIndex = 4
PasswordInput.Parent = LoginFormFrame

PasswordStroke = InstanceCreator.createNewInstance("UIStroke")
PasswordStroke.Size = 0.02
PasswordStroke.Parent = PasswordInput

# --- Submit Button ---
LoginB = InstanceCreator.createNewInstance("TextButton")
LoginB.Size = [0.6, 0.12]
LoginB.Font = "pressstart2p"
LoginB.TextColor = (255, 0, 0)
LoginB.Text = "Submit"
LoginB.Name = "LoginSubmitB"
LoginB.zIndex = 4
LoginB.Parent = LoginFormFrame

LoginSubmitStroke = InstanceCreator.createNewInstance("UIStroke")
LoginSubmitStroke.Size = 0.04
LoginSubmitStroke.Parent = LoginB
