import tkinter as tk
from tkinter import *
from tkinter import ttk

from frames.GKD_map import GKD
from frames.hospital_map import Hospital
from frames.school_a_map import SchoolA
from frames.school_b_map import SchoolB
from frames.town_map import Town


class Controller(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        tab_control = self.createTabControl(parent)
        tab_control.pack(expand=1, fill="both")

    def createTabControl(self, parent):
        tab_control = ttk.Notebook(parent)

        tab_control.add(SchoolA().draw(parent), text='School A')
        tab_control.add(SchoolB().draw(parent), text='School B')
        tab_control.add(Town().draw(parent), text='Town')
        tab_control.add(Hospital().draw(parent), text='Hospital')
        tab_control.add(GKD().draw(parent), text='GKD')
        return tab_control

