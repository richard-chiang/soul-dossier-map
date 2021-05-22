from MapData import MapData
from Map import Map

first_floor_url = "./img/town/first_floor.jpeg"
second_floor_url = "./img/town/second_floor.jpeg"
first_map_y_delta = 100
second_map_y_delta = 100

first_floor_seal_locations = [
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

second_floor_seal_locations = [
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

first_map_data = MapData(first_floor_url, first_map_y_delta, first_floor_seal_locations)
second_map_data = MapData(second_floor_url, second_map_y_delta, second_floor_seal_locations)

map_display = Map(first_map_data, second_map_data)
map_display.draw()
