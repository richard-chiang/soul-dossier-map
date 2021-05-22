import tkinter as tk
from PIL import ImageTk, Image


class Util:

    def __init__(self):
        self.selected_element_list = []

    def get_element_dictionary(self):
        return {
            "unselected": "white",
            "gold": "gold",
            "wood": "green",
            "water": "blue",
            "fire": "red",
            "earth": "saddle brown",
            "none": "DarkOrchid1",
        }


    def element_selection_callback(self, text, option_menu):
        selection_text = text.get()
        elements = self.get_element_dictionary()
        color = elements[selection_text]
        print(f"Clicked {selection_text}, change color to {color}")
        option_menu.config(background=color, foreground=color)
        self.recount_found()

    def recount_found(self):
        count = 0
        for text in self.selected_element_list:
            current_selection = text.get()
            if current_selection != "unselected" and current_selection != "none":
                count += 1

        if count == 5:
            self.set_leftover_to_none()

    def create_option_menu(self, root, coord_x, coord_y):
        element_list = list(self.get_element_dictionary().keys())

        default_text = tk.StringVar(root, value=element_list[0])

        option = tk.OptionMenu(root, default_text, *element_list)
        option.config(background="grey")
        option.config(width=4)
        option.config(borderwidth=10)

        default_text.trace("w", lambda *args: self.element_selection_callback(default_text, option))
        option.place(x=coord_x, y=coord_y)

        self.selected_element_list.append(default_text)

    def getorigin(self, eventorigin):
        global x, y
        x = eventorigin.x
        y = eventorigin.y
        print(f'({x}, {y})')

    def get_background(self, root, image_url):
        background = Image.open(image_url)
        background = ImageTk.PhotoImage(background)
        panel = tk.Label(root, image = background)
        panel.image = background
        panel.pack(side=tk.LEFT)

    def set_leftover_to_none(self):
        for text in self.selected_element_list:
            if text.get() == "unselected":
                text.set("none")

    def create_reset_button(self, root):
        btn = tk.Button(root, text="Reset", command=self.reset)
        btn.place(x=0, y=0)

    def reset(self):
        for text in self.selected_element_list:
            text.set("unselected")