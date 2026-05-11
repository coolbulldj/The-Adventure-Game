from .ConnectionClass import Connection
from GeneralFunctions import CreateUniqueKeyForMap


class Event:
    def __init__(self):
        self.cbs = {}

    def _FireEvent(self, *args):
        for cb in self.cbs.values():
            cb(*args)

    def Once(self, cb):
        key = CreateUniqueKeyForMap(self.cbs)

        def DisconnectCB():
            self.cbs[key] = None

        EventConnection = Connection(DisconnectCB)

        def Onevent(*args):
            EventConnection.Disconnect()
            cb(*args)

        self.cbs[key] = Onevent

        return EventConnection

    def Connect(self, cb):
        key = CreateUniqueKeyForMap(self.cbs)

        def DisconnectCB():
            self.cbs[key] = None

        self.cbs[key] = cb

        EventConnection = Connection(DisconnectCB)

        return EventConnection

    def Wait(self, _):
        key = CreateUniqueKeyForMap(self.cbs)

        self.cbs[key] = "Wating..."

        while self.cbs[key]:
            print("wating")
            pass