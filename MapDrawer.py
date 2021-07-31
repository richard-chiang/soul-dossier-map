from util import *
import MapData


class Map:

    def __init__(self, first_map_data: MapData, second_map_data: MapData = None):
        self.width = 1440  # 720
        self.height = 900
        self.first_map_data = first_map_data
        self.second_map_data = second_map_data
        self.util = Util()

    def drawFrame(self, root):
        frame = tk.Frame(root)
        # frame.geometry(f"{self.width}x{self.height}")
        # frame.bind("<Button 1>", self.util.getorigin)

        self.util.get_background(frame, self.first_map_data.map_url)

        for x_coord, y_coord in self.first_map_data.seal_locations:
            x = x_coord
            y = y_coord
            self.util.create_option_menu(frame, x, y)

        if self.second_map_data is not None:
            self.util.get_background(frame, self.second_map_data.map_url)

            for x_coord, y_coord in self.second_map_data.seal_locations:
                x = self.width // 2 + x_coord
                y = y_coord
                self.util.create_option_menu(frame, x, y)

        return frame
