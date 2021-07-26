from dearpygui import dearpygui as dpg
from .container import Container
from typing import List


class Window(Container):

    def __init__(self, *, width: int, height: int, pos: List[int], no_resize: bool = True, id: int = dpg.generate_uuid(), show: bool = True, no_move: bool = True, no_collapse: bool = True, no_scrollbar: bool = True, no_close: bool = True) -> None:
        super().__init__(width=width, height=height, pos=pos, no_resize=no_resize)
        self.id = id
        self.show = show
        self.no_move = no_move
        self.no_collapse = no_collapse
        self.no_scrollbar = no_scrollbar
        self.no_close = no_close

    def __ref__(self):
        return self.id

    def add_item(self, item):
        pass

    def remove_item(self, item):
        pass

    def update_item(self, item, value):
        pass

    def render(self):  # FIXME return window id
        with dpg.window(**self.__dict__):
            dpg.add_text("asdfasd")
