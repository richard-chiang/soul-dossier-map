import tk as tk

from MapData import MapData
from MapDrawer import Map


class SchoolB():

    def first_floor_url(self):
        return "./img/school_b/first_floor.png"

    def second_floor_url(self):
        return "./img/school_b/second_floor.png"

    def first_floor_seal_locations(self):
        return [
            (26, 159),
            (129, 139),
            (212, 88),
            (344, 240),
            (167, 400),
            (319, 386),
            (108, 268)
        ]

    def second_floor_seal_locations(self):
        return [
            (41, 169),
            (140, 246),
            (211, 47),
            (281, 271),
            (215, 339),
            (374, 385),
            (113, 59),
            (433, 293)
        ]

    def first_map(self):
        return MapData(self.first_floor_url(), self.first_floor_seal_locations())

    def second_map(self):
        return MapData(self.second_floor_url(), self.second_floor_seal_locations())

    def draw(self, parent):
        map_display = Map(self.first_map(), self.second_map())
        return map_display.drawFrame(parent)
