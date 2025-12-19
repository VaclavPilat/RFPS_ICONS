import math


def Arrow(self, W, H, L, C, B, S=False, E=True, F=None):
    degrees = math.degrees(math.atan2(H, W))
    if F is None:
        F = 2*L
    if S:
        for i in (-45, +45):
            radians = math.radians(degrees + i)
            self.line((0, 0), (math.cos(radians)*F, math.sin(radians)*F), rounded=True)
    if E:
        for i in (-45, +45):
            radians = math.radians(degrees + 180 + i)
            self.line((W, H), (W+math.cos(radians)*F, H+math.sin(radians)*F), rounded=True)
    self.line((0, 0), (W, H), rounded=True)