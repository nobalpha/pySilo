# TODO File Diff fonksiyonu aşağı yukarı bitti, sadece os.replace fonksiyonlarını göç etmemiz ve File Diff'in interaktif ekranını ayarlamamız lazım (silmek).

from genericpath import exists
from os.path import isfile, join, isdir
import re
import os
from typing import Tuple, Dict, List
from dearpygui import dearpygui as dpg
import platform
from functions import *


def init():

    # set_main_window_size(window_width, window_height)
    # set_main_window_title("Program is ongoing!")
    # set_main_window_resizable(True)
    # set_global_font_scale(1.25)
    # set_theme("Light")
    # set_style_window_padding(30, 30)

    dpg.setup_viewport()
    dpg.set_viewport_height(window_height)
    dpg.set_viewport_width(window_width)
    dpg.set_viewport_title("Program is ongoing!")
    dpg.set_viewport_resizable(True)
    # dpg.theme("Light")

    width, height, channels, data = dpg.load_image("./media/logo.png")
    print(channels)

    with dpg.texture_registry():
        image_id = dpg.add_static_texture(width, height, data)

    with dpg.window(label=window_name, id=dpg.generate_uuid(), width=widget_width, height=widget_height, no_resize=True, no_close=True, no_move=True, pos=[(window_width-widget_width) // 2, 0]):
        print("GUI is running.")
        with dpg.drawlist(width=logo["width"], height=logo["height"]):
            dpg.draw_image(image_id, (0, 0), (logo["width"], logo["height"]), uv_min=(0, 0), uv_max=(1, 1))

        dpg.add_same_line()

        with dpg.group(label="Commands", horizontal=False):
            dpg.add_button(label="Directory Selector")  # , callback=directory_picker_callback)
            dpg.add_button(label="Clear")  # , callback=clear_directory_selector)
            dpg.add_button(label="Resimulate")  # , callback=resimulate_organization)
            dpg.add_button(label="Diff")  # , callback=file_diff)

        dpg.add_separator()

        dpg.add_text(label="directory_label", default_value="Selected directory shows here...")
        dpg.add_spacing(count=5)

    with dpg.window(label="File Differ", width=widget_width, height=widget_height, no_resize=True, no_close=True, autosize=True, no_move=False,  pos=[(window_width-widget_width) // 2, widget_height]):
        dpg.add_text(label="diff_label", default_value="File changes will be shown here...")


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
dpg.start_dearpygui()
