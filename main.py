import tkinter as tk
from PIL import ImageTk, Image


def get_element_dictionary():
    return {
        "unselected": "white",
        "gold": "gold",
        "wood": "green",
        "water": "blue",
        "fire": "red",
        "earth": "saddle brown",
        "none": "DarkOrchid1",
    }


def element_selection_callback(text, option_menu):
    selection_text = text.get()
    elements = get_element_dictionary()
    color = elements[selection_text]
    print(f"Clicked {selection_text}, change color to {color}")

    option_menu.config(background=color, foreground=color)


def option_menu(root, coord_x, coord_y):
    element_list = list(get_element_dictionary().keys())

    default_text = tk.StringVar(root, value=element_list[0])

    option = tk.OptionMenu(root, default_text, *element_list)
    option.config(background="grey")
    option.config(width=4)
    option.config(borderwidth=10)

    default_text.trace("w", lambda *args: element_selection_callback(default_text, option))
    option.place(x=coord_x, y=coord_y)


def getorigin(eventorigin):
    global x, y
    x = eventorigin.x
    y = eventorigin.y
    print(x, y)


def get_background(root, image_url):
    background = Image.open(image_url)
    background = ImageTk.PhotoImage(background)
    panel = tk.Label(root, image = background)
    panel.image = background
    panel.pack(side=tk.LEFT)



root = tk.Tk()

# Setting

width = 1440 # 720
height = 900
first_floor_url = "./img/school/first_floor_resized.jpeg"
second_floor_url = "./img/school/second_floor_resized.jpeg"

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
    (548, 738)
]

# Calls

root.geometry(f"{width}x{height}")

root.bind("<Button 1>", getorigin)

get_background(root, first_floor_url)
get_background(root, second_floor_url)

for locations in first_floor_seal_locations:
    option_menu(root, *locations)

for x_coord, y_coord in second_floor_seal_locations:
    x = width // 2 + x_coord
    y = y_coord
    option_menu(root, x, y)

root.mainloop()