from MapData import MapData
from MapDrawer import Map


class GKD:

    def map_url(self):
        return "./img/GKD/gkd.jpg"

    def seal_locations(self):
        return [
            (211, 97),
            (313, 91),
            (450, 119),
            (485, 225),
            (427, 373),
            (59, 222),
            (48, 310),
            (61, 457),
            (169, 524),
            (307, 519),
            (381, 578),
            (594, 538),
            (597, 250),
            (752, 96),
            (866, 93),
            (1014, 127),
            (978, 376),
            (1015, 285),
            (901, 537),
            (801, 587),
            (707, 570),
            (947, 41),
            (593, 413)
        ]

    def map_data(self):
        return MapData(self.map_url(), seal_locations = self.seal_locations())

    def draw(self, root):
        map_display = Map(self.map_data())
        return map_display.drawFrame(root)
