from Modules.Gameloop.UI.Init.LoginPage import LoginScreen, LoginB, UsernameInput, PasswordInput

LoginState = "Login"  # 'Login' or 'Create'




def SetLoginState(state):
    global LoginState
    LoginState = state

    if state == "Login":
        LoginB.Text = "Login"
    elif state == "Create":
        LoginB.Text = "Create Acccount"
    else:
        print(f"Attempted to set invalid login state:{state}")
    #reset textboxes
    UsernameInput.Text = ""
    PasswordInput.Text = "" 

def GetAccountDetails():
    print(f"Creating new account with username:{UsernameInput.Text} & password:{PasswordInput.Text}")
    return UsernameInput.Text, PasswordInput.Text
