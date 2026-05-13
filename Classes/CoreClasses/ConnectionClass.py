class Connection:
    def __init__(self, disconnectMethod):
        self._DisconnectMethod = disconnectMethod
        self._Connected = True

    def Disconnect(self):
        if not self._Connected:
            print(
                "WARNING: this Connection has already been disconnected consider deleting held variable to prevent memory leak"
            )
            return
        self._Connected = False
        self._DisconnectMethod()
