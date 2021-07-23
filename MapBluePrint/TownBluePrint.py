from MapBluePrint.IMapBluePrint import IMapBluePrint


class TownMapBluePrint(IMapBluePrint):

    def first_floor_url(self):
        return "./img/town/first_floor.jpeg"

    def second_floor_url(self):
        return "./img/town/second_floor.jpeg"

    def y_delta(self):
        return 100

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


def first_floor_url():
    return None