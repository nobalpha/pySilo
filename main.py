# TODO File Diff fonksiyonu aşağı yukarı bitti, sadece os.replace fonksiyonlarını göç etmemiz ve File Diff'in interaktif ekranını ayarlamamız lazım (silmek).

from genericpath import exists
from os.path import isfile, join, isdir
import re
import os
from typing import Tuple, Dict, List
from dearpygui.core import *
from dearpygui.simple import *
import platform
from functions import *


def init():
    set_main_window_size(window_width, window_height)
    set_main_window_title("Program is ongoing!")
    set_main_window_resizable(True)
    set_global_font_scale(1.25)
    set_theme("Light")
    set_style_window_padding(30, 30)

    with window(window_name, width=widget_width, height=widget_height, no_resize=True, no_close=True, no_move=True, x_pos=(window_width-widget_width) // 2, y_pos=0):
        print("GUI is running.")
        add_image("logo", "media/logo.png", width=logo["width"], height=logo["height"])
        add_same_line()
        add_group("commands")
        add_button("Directory Selector", callback=directory_picker_callback)
        add_button("Clear", callback=clear_directory_selector)
        add_button("Resimulate", callback=resimulate_organization)
        add_button("Diff", callback=file_diff)
        end()
        add_separator()
        add_text(name="directory_label", default_value="Selected directory shows here...")
        add_spacing(count=5)

    with window("File Differ", width=widget_width, height=widget_height, no_resize=True, no_close=True, autosize=True, no_move=False,  x_pos=(window_width-widget_width) // 2, y_pos=widget_height):
        add_text(name="diff_label", default_value="File changes will be shown here...")


window_name = "pySilo : Your best organizer friend"

system = platform.system()

print("{0} system detected...".format(system))


logo = {}
logo["name"] = "logo"
logo["width"] = 90
logo["height"] = 126
logo["dims"] = (logo["width"], logo["height"])
print(logo)

init()

# draw_image("logo", "media/logo.png", (0.0, 0.0), logo["dims"])
start_dearpygui()
