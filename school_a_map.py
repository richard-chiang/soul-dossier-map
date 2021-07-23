from MapData import MapData
from Map import Map

first_floor_url = "./img/school_a/first_floor.jpeg"
second_floor_url = "./img/school_a/second_floor.jpeg"
first_map_y_delta = 0
second_map_y_delta = 0

first_floor_seal_locations = [
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

second_floor_seal_locations = [
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

first_map_data = MapData(first_floor_url, first_map_y_delta, first_floor_seal_locations)
second_map_data = MapData(second_floor_url, second_map_y_delta, second_floor_seal_locations)

map_display = Map(first_map_data, second_map_data)
map_display.draw()
