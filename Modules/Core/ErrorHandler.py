import traceback


ErrorStatus = False

def ThrowWarning(WarningString):
    print(" ")
    print(WarningString, traceback.extract_stack())
    print(" ")

def ThrowError(ErrorString):
    global ErrorStatus
    print(" ")
    print(ErrorString, traceback.extract_stack())
    print(" ")
    ErrorStatus = True

def GetErrorStatus():
    return ErrorStatus