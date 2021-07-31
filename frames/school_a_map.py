from MapData import MapData
from MapDrawer import Map


class SchoolA:

    def first_floor_url(self):
        return "./img/school_a/first_floor.jpeg"

    def second_floor_url(self):
        return "./img/school_a/second_floor.jpeg"

    def first_floor_seal_locations(self):
        return [
            (118, 345),
            (138, 588),
            (409, 583),
            (529, 604),
            (598, 703),
            (550, 352),
            (440, 316),
            (80, 138),
            (361, 73),
        ]

    def second_floor_seal_locations(self):
        return [
            (40, 72),
            (43, 312),
            (257, 236),
            (483, 342),
            (138, 634),
            (411, 610),
            (606, 601),
            (548, 738),
            (319, 156)
        ]

    def first_map(self):
        return MapData(self.first_floor_url(), self.first_floor_seal_locations())

    def second_map(self):
        return MapData(self.second_floor_url(), self.second_floor_seal_locations())

    def draw(self, root):
        map_display = Map(self.first_map(), self.second_map())
        return map_display.drawFrame(root)
