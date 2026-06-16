import json
import os

DataFilePath = "Modules/Core/Data/DataSaveFile.txt"

EncryptedData = False

PROFILE_SEPARATOR = " "
CREDENTIALS_SEPARATOR = "|"

# account_id -> {"user": str, "password": str, "data": dict}
_accounts: dict[int, dict] = {}
_next_account_id = 1


def _serialize_data(data):
    if EncryptedData:
        raise NotImplementedError("Encrypted saves are not implemented yet.")
    return json.dumps(data, ensure_ascii=False)


def _deserialize_data(rawText):
    if not rawText.strip():
        return {}
    if EncryptedData:
        raise NotImplementedError("Encrypted saves are not implemented yet.")
    return json.loads(rawText)


def _ensure_data_file():
    directory = os.path.dirname(DataFilePath)
    if directory:
        os.makedirs(directory, exist_ok=True)
    if not os.path.exists(DataFilePath):
        with open(DataFilePath, "w", encoding="utf-8"):
            pass


def _read_lines():
    _ensure_data_file()
    with open(DataFilePath, "r", encoding="utf-8") as file:
        return file.read().splitlines()


def _write_lines(lines):
    _ensure_data_file()
    with open(DataFilePath, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
        if lines:
            file.write("\n")


def _parse_profiles(lines):
    profiles = []
    index = 0

    while index < len(lines):
        if lines[index] != PROFILE_SEPARATOR:
            index += 1
            continue

        index += 1
        if index >= len(lines):
            break

        credentials = lines[index].split(CREDENTIALS_SEPARATOR, 1)
        if len(credentials) != 2:
            index += 1
            continue

        username, storedPassword = credentials
        index += 1

        dataLines = []
        while index < len(lines) and lines[index] != PROFILE_SEPARATOR:
            dataLines.append(lines[index])
            index += 1

        profiles.append(
            {
                "user": username,
                "password": storedPassword,
                "data": _deserialize_data("\n".join(dataLines)),
            }
        )

    return profiles


def _format_profile(username, password, data):
    return [
        PROFILE_SEPARATOR,
        f"{username}{CREDENTIALS_SEPARATOR}{password}",
        _serialize_data(data),
    ]


def LoadFromFile():
    global _next_account_id

    _accounts.clear()
    profiles = _parse_profiles(_read_lines())

    for account_id, profile in enumerate(profiles, start=1):
        _accounts[account_id] = profile

    _next_account_id = max(_accounts.keys(), default=0) + 1


def GetAccountIds():
    return list(_accounts.keys())


def GetAccount(account_id):
    return _accounts.get(account_id)


def GetUsername(account_id):
    account = _accounts.get(account_id)
    if account is None:
        return None
    return account["user"]


def GetData(account_id):
    account = _accounts.get(account_id)
    if account is None:
        return None
    return account["data"]


def SetData(account_id, data):
    if account_id not in _accounts:
        raise KeyError(f"Account {account_id} not found.")

    if not isinstance(data, dict):
        raise TypeError("Profile data must be a dictionary.")

    _accounts[account_id]["data"] = data


def SetDataValue(account_id, key, value):
    data = GetData(account_id)
    if data is None:
        raise KeyError(f"Account {account_id} not found.")

    data[key] = value


def CreateAccount(user, password, data=None):
    global _next_account_id

    account_id = _next_account_id
    _next_account_id += 1

    _accounts[account_id] = {
        "user": user,
        "password": password,
        "data": {} if data is None else data,
    }

    return account_id


def VerifyLogin(user, password):
    for account_id, account in _accounts.items():
        if account["user"] == user and account["password"] == password:
            return account_id

    return None


def DeleteAccount(account_id):
    if account_id not in _accounts:
        return False

    del _accounts[account_id]
    return True


def SaveAll():
    lines = []

    for account_id in sorted(_accounts.keys()):
        account = _accounts[account_id]
        lines.extend(
            _format_profile(account["user"], account["password"], account["data"])
        )

    _write_lines(lines)


def SaveAccount(account_id):
    if account_id not in _accounts:
        raise KeyError(f"Account {account_id} not found.")

    SaveAll()


LoadFromFile()
