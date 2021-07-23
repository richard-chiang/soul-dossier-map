from MapBluePrint.IMapBluePrint import IMapBluePrint


class SchoolBBluePrint(IMapBluePrint):

    def first_floor_url(self):
        return "./img/school_b/first_floor.png"

    def second_floor_url(self):
        return "./img/school_b/second_floor.png"

    def y_delta(self):
        return 185

    def first_floor_seal_locations(self):
        return [
            (26, 159),
            (129, 139),
            (212, 88),
            (344, 240),
            (167, 400),
            (319, 386),
            (117, 266),
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
            (113, 59)
        ]
