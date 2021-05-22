class MapData:

    def __init__(self, map_url: str, y_delta: int, seal_locations: [(int, int)]):
        self.map_url = map_url
        self.y_delta = y_delta
        self.seal_locations = seal_locations
