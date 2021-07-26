from dearpygui import dearpygui as dpg
from .container import Container
from typing import List


class Viewport(Container):
    def __init__(self, *, width: int, height: int, pos: List[int], no_resize: bool = True, title: str, icon: str = "") -> None:
        super().__init__(width=width, height=height, pos=pos, no_resize=no_resize)
        self.title = title
        self.icon = icon

    def render(self):
        try:
            # dpg.setup_viewport()
            # dpg.set_viewport_height(self.height)
            # dpg.set_viewport_maximized_box(False)
            # dpg.set_viewport_width(500)
            # dpg.set_viewport_title(self.title)
            # dpg.set_viewport_resizable(self.no_resize)
            # dpg.set_viewport_pos(self.pos)
            print(self.width)
            dpg.set_viewport_height(300)

            print(dpg.get_viewport_height())
        except Exception as e:
            print(e)
            return False
        return True
