from pygame import freetype as ft
import os

customFonts = {
    "pressstart2p": os.path.join(".", "Assets", "Fonts", "PressStart2P-Regular.ttf")
}
_fontCache = {}


def GetFont(Name) -> ft.SysFont:
    fontPath = None
    if Name in customFonts:
        fontPath = customFonts[Name]

    if Name not in _fontCache.keys():
        # print("creating new font cache instance")
        if fontPath:
            _fontCache[Name] = ft.Font(fontPath, 1)
        else:
            _fontCache[Name] = ft.SysFont(Name, 1)

    return _fontCache[Name]
