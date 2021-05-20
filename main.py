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
    option.configure(background="grey")

    default_text.trace("w", lambda *args: element_selection_callback(default_text, option))
    option.place(x=coord_x, y=coord_y)


def getorigin(eventorigin):
    global x, y
    x = eventorigin.x
    y = eventorigin.y
    print(x, y)


def get_background(root):
    background = Image.open("./img/school/first_floor_crop.png")
    background = ImageTk.PhotoImage(background)
    panel = tk.Label(root, image = background)
    panel.image = background
    panel.grid(row = 2)




root = tk.Tk()
root.bind("<Button 1>", getorigin)

get_background(root)
option_menu(root, 20, 40)



root.mainloop()