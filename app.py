# TODO Typechecking
# TODO Fallback value
# TODO Render UI OOP System
# TODO Simple Hello World Interface
# TODO Manual CSS-like layout
from containers.viewport import Viewport
from containers.window import Window
from items.button import Button
from items.layout import Layout
from dearpygui import dearpygui as dpg

vp = Viewport(width=500, height=500, pos=[100, 100], no_resize=False, title="Hello World!")
vp.render()
window = Window(width=100, height=200, pos=[10, 10])
dpg.set_primary_window(window, True)
window.render()

layout = Layout(width=100, height=100, pos=[50, 50], alignment="a", parent=window.__ref__())

submit_button = Button(label="Submit Button", width=50, height=50, pos=[
                       10, 10], callback=lambda x: print(x), parent=layout.__ref__())
cancel_button = Button(label="Cancel Button", width=50, height=50, pos=[
                       100, 100], callback=lambda x: print("aaa"), parent=layout.__ref__())
layout.add_item(submit_button, cancel_button)
layout.render()
# submit_button.init_callback()

dpg.start_dearpygui()
