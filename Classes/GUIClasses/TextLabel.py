import pygame as py
from pygame import freetype as ft
from Classes.GUIClasses.GuiBase import GuiBase
from Modules.Core.CoreGUI.FontCache import GetFont

SEPARATOR = " "


def GetScaledTextSize(text: str, font: ft.SysFont, abSize) -> int:
    if not text:
        return 1

    base_size = 100
    font.size = base_size
    ts = font.get_rect(text)

    if ts.width == 0 or ts.height == 0:
        return 1

    scale = min(abSize[0] / ts.width, abSize[1] / ts.height)
    return max(1, int(base_size * scale))


def DetermineWrap(text: str, font: ft.SysFont, absoluteSize: tuple) -> list[str]:
    if not text:
        return []

    words = [w for w in text.split(SEPARATOR) if w]
    if len(words) <= 1:
        return [text]

    xs, ys = absoluteSize

    for rows in range(1, len(words) + 1):
        per_row_height = ys / rows
        # Size font to fit one row's height, using "Mg" as a representative glyph
        font.size = GetScaledTextSize("Mg", font, (xs, per_row_height))

        lines = []
        current = []
        too_many = False

        for word in words:
            candidate = SEPARATOR.join(current + [word]) if current else word
            if font.get_rect(candidate).width <= xs:
                current.append(word)
            else:
                if current:
                    lines.append(SEPARATOR.join(current))
                else:
                    lines.append(word)  # single word wider than box; force it
                current = [word]

            if len(lines) > rows:
                too_many = True
                break

        if too_many:
            continue

        if current:
            lines.append(SEPARATOR.join(current))

        if len(lines) <= rows:
            return lines

    return [text]


class TextLabel(GuiBase):
    def __init__(self):
        super().__init__()
        self.TextScaled = True
        self.TextWrapped = True
        self.TextSize = 14
        self.TextColor = (255, 0, 0)
        self.Text = "Hello World"
        self.Font = "monospace"

    def render(self, screen, *args):
        super().render(*args)
        self.renderUIStructures(screen)

        ab_xs, ab_ys = self.AbsoluteSize
        pos_x, pos_y = self.AbsolutePos

        if self.BackgroundTransparency != 1:
            py.draw.rect(screen, self.BackgroundColor, (pos_x, pos_y, ab_xs, ab_ys))

        font = GetFont(self.Font)

        if not self.Text:
            self.renderUIAssets(screen)
            return

        if self.TextScaled:
            wrap_lines = (
                DetermineWrap(self.Text, font, self.AbsoluteSize)
                if self.TextWrapped
                else [self.Text]
            )
            # DetermineWrap returns [] for empty/None text; re-guard here in case
            if not wrap_lines:
                wrap_lines = [self.Text]
            rows = len(wrap_lines)
            per_row_height = ab_ys / rows
            # Pick the smallest size so every line fits both axes
            font.size = max(
                1,
                min(
                    GetScaledTextSize(line, font, (ab_xs, per_row_height))
                    for line in wrap_lines
                ),
            )
        else:
            wrap_lines = [self.Text]
            font.size = self.TextSize

        line_height = font.get_rect("Mg").height
        total_height = line_height * len(wrap_lines)
        start_y = pos_y + (ab_ys - total_height) / 2

        for i, line in enumerate(wrap_lines):
            rect = font.get_rect(line)
            x = pos_x + (ab_xs - rect.width) / 2
            y = start_y + i * line_height
            font.render_to(screen, (x, y), line, fgcolor=self.TextColor, bgcolor=None)
        self.renderUIAssets(screen)
