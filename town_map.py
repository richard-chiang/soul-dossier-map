from MapData import MapData
from MapDrawer import Map


class Town:

    def first_floor_url(self):
        return "./img/town/first_floor.jpeg"

    def second_floor_url(self):
        return "./img/town/second_floor.jpeg"

    def first_floor_seal_locations(self):
        return [
            (181, 269),
            (63, 510),
            (243, 530),
            (419, 531),
            (569, 551),
            (614, 403),
            (608, 223),
            (404, 259),
            (411, 117)
        ]

    def second_floor_seal_locations(self):
        return [
            (77, 230),
            (64, 482),
            (219, 492),
            (396, 522),
            (617, 378),
            (375, 271),
            (389, 103),
            (562, 170),
            (621, 543)
        ]

    def first_map(self):
        return MapData(self.first_floor_url(), self.first_floor_seal_locations())

    def second_map(self):
        return MapData(self.second_floor_url(), self.second_floor_seal_locations())

    def draw(self):
        map_display = Map(self.first_map(), self.second_map())
        map_display.draw()


Town().draw()
