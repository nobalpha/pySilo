import dearpygui.dearpygui as dpg


def save_callback():
    print("Save Clicked")


def print_height():
    print(dpg.get_viewport_height())


with dpg.window(label="Example Window", no_title_bar=True, pos=(0, 0)) as w:
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.set_viewport_resize_callback(print_height)
dpg.start_dearpygui()
