from util import *
import MapData


class Map:

    def __init__(self, first_map_data: MapData, second_map_data: MapData = None):
        self.width = 1440  # 720
        self.height = 900
        self.first_map_data = first_map_data
        self.second_map_data = second_map_data
        self.util = Util()

    def draw(self):
        root = tk.Tk()
        root.geometry(f"{self.width}x{self.height}")
        root.bind("<Button 1>", self.util.getorigin)

        self.util.get_background(root, self.first_map_data.map_url)

        for x_coord, y_coord in self.first_map_data.seal_locations:
            x = x_coord
            y = y_coord
            self.util.create_option_menu(root, x, y)

        if self.second_map_data is not None:
            self.util.get_background(root, self.second_map_data.map_url)

            for x_coord, y_coord in self.second_map_data.seal_locations:
                x = self.width // 2 + x_coord
                y = y_coord
                self.util.create_option_menu(root, x, y)

        root.mainloop()
