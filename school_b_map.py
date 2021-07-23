from MapData import MapData
from Map import Map

first_floor_url = "./img/school_b/first_floor.png"
second_floor_url = "./img/school_b/second_floor.png"
first_map_y_delta = 185
second_map_y_delta = 185

first_floor_seal_locations = [
    (26, 159),
    (129, 139),
    (212, 88),
    (344, 240),
    (167, 400),
    (319, 386),
    (108, 268)
]

second_floor_seal_locations = [
    (41, 169),
    (140, 246),
    (211, 47),
    (281, 271),
    (215, 339),
    (374, 385),
    (113, 59),
    (433, 293)
]

first_map_data = MapData(first_floor_url, first_map_y_delta, first_floor_seal_locations)
second_map_data = MapData(second_floor_url, second_map_y_delta, second_floor_seal_locations)

map_display = Map(first_map_data, second_map_data)
map_display.draw()
