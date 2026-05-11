

class Button():
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    def check_mousehit(self, mouseHit):
        #bounds of the button
        lx, hx = 0,0 #low x, high x
        ly, hy = 0,0 #low y, high y

        mx, my = mouseHit

        if mx < lx or hx < mx:
            return False
        elif my < ly or hy < my:
            return False

        return True