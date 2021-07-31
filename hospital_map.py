from MapData import MapData
from MapDrawer import Map


class Hospital:

    def map_url(self):
        return "./img/Hospital/hospital.jpg"

    def seal_locations(self):
        return [
            (54, 496),
            (223, 511),
            (127, 212),
            (236, 271),
            (352, 260),
            (639, 42),
            (654, 195),
            (621, 404),
            (739, 499),
            (846, 518),
            (1033, 486),
            (1110, 507),
            (1040, 38),
            (1104, 155),
            (1235, 504),
            (1354, 512),
            (1460, 519),
            (1222, 37),
            (1328, 136),
            (1229, 252),
            (1724, 57),
            (1734, 150),
            (1741, 257),
            (1737, 363),
            (1789, 505),
            (1619, 529),
            ]

    def map(self):
        return MapData(self.map_url(), self.seal_locations())

    def draw(self):
        map_display = Map(self.map())
        map_display.draw()


Hospital().draw()
