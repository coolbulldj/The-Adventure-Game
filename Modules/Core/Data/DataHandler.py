# Save file
DataFilePath = "Modules\Core\Data\DataSaveFile.txt"

EncryptedData = False  # use this for

# A space represents a new profile, the next line after this space is the user name & password all data below that line is then a an array


def CheckPassword(password):
    return True


def RetriveData(user, password):
    pass


def FindProfileLine(user, password):
    with open(DataFilePath, "r") as file:
        lines = file.readlines()

    profiles = []

    with open(DataFilePath, "w") as file:
        file.writelines(lines)


def WriteProfile(user, password, data):
    pass


FindProfileLine(1, 1)
