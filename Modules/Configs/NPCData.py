#structure
#DisplayName:string
#Description:string
#
#
#
#

from Modules.Configs.NPCS.Primary import (
    Adrien,
    CaptainMarcus,
    Cass,
    Elias,
    Johan,
    Mara,
    Mira,
    Victor,
)
from Modules.Configs.NPCS.Background import (
    Npc1,
    Npc2,
    Npc3,
    Npc4,
    Npc5,
    Npc6,
    Npc7,
    Npc8,
    Npc9,
    Npc10,
    Npc11,
    Npc12,
)

_PRIMARY_MODULES = [
    Johan,
    Cass,
    Mara,
    CaptainMarcus,
    Adrien,
    Victor,
    Mira,
    Elias,
]

_BACKGROUND_MODULES = [
    Npc1,
    Npc2,
    Npc3,
    Npc4,
    Npc5,
    Npc6,
    Npc7,
    Npc8,
    Npc9,
    Npc10,
    Npc11,
    Npc12,
]


def _RegisterNpcs(modules, npcType):
    registered = {}
    for module in modules:
        data = module.Data
        registered[data["DisplayName"]] = {**data, "Type": npcType}
    return registered


NPCS = {
    **_RegisterNpcs(_PRIMARY_MODULES, "Primary"),
    **_RegisterNpcs(_BACKGROUND_MODULES, "Background"),
}


def GetBackgroundNpcs():
    return {
        name: data
        for name, data in NPCS.items()
        if data["Type"] == "Background"
    }


def GetPrimaryNpcs():
    return {
        name: data
        for name, data in NPCS.items()
        if data["Type"] == "Primary"
    }


def GetNpcByName(name):
    return NPCS.get(name)
