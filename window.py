from dearpygui import dearpygui as dpg
from container import Container
from typing import List
from viewport import Viewport


class Window(Container):

    def __init__(self, *, width: int, height: int, pos: List[int], no_resize: bool = True, id: int = dpg.generate_uuid(), show: bool = True, no_move: bool = True, no_collapse: bool = True, no_scrollbar: bool = True, no_close: bool = True) -> None:
        super().__init__(width, height, pos, no_resize)
        self.id = id
        self.show = show
        self.no_move = no_move
        self.no_collapse = no_collapse
        self.no_scrollbar = no_scrollbar
        self.no_close = no_close

    def __ref__(self):
        print(self.id)

    def add_item(self, item):
        pass

    def remove_item(self, item):
        pass

    def update_item(self, item, value):
        pass

    def render(self):
        with dpg.window(**self.__dict__):
            dpg.add_text("asdfasd")


vp = Viewport(width=500, height=500, pos=[100, 100], no_resize=False, title="Hello World!")
vp.render()
window = Window(width=100, height=200, pos=[10, 10])
dpg.set_primary_window(window, True)
window.__ref__()
window.render()
dpg.start_dearpygui()
