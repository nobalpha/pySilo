from dearpygui import dearpygui as dpg
from typing import List


class Container:
    def __init__(self, width: int, height: int, pos: List[int], no_resize: bool = True) -> None:
        self.width = width
        self.height = height
        self.pos = pos
        self.no_resize = no_resize
