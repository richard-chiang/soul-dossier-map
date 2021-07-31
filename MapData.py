class MapData:

    def __init__(self, map_url: str, seal_locations: [(int, int)] = []):
        self.map_url = map_url
        self.seal_locations = seal_locations
