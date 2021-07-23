from MapBluePrint.IMapBluePrint import IMapBluePrint


class SchoolABluePrint(IMapBluePrint):

    def first_floor_url(self):
        return "./img/school_a/first_floor.jpeg"

    def second_floor_url(self):
        return "./img/school_a/second_floor.jpeg"

    def y_delta(self):
        return 0

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
            (548, 738)
        ]
