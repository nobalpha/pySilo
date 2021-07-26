from typing import List
from dearpygui import dearpygui as dpg
from typing import Tuple, Any
from .item import Item


class Layout(Item):
    def __init__(self, *, width: int, height: int, pos: Tuple[int], alignment: str = "a", label: str = "", show: bool = True, user_data: Any = "", parent: int) -> None:
        type = "layout"
        super().__init__(id=id, label=label, width=width, height=height,
                         show=show, pos=pos, user_data=user_data, type=type, parent=parent)
        self.lpos = (0, 0)  # local position
        self.alignment = alignment  # [a]uto | [h]orizontal | [v]ertical
        self.items = []

    def add_item(self, *items: Item):
        try:
            for item in items:
                self.items.append(item)
        except Exception as e:
            print(e)
            return False
        return True

    def arrange_layout(self):
        for i in range(1, len(self.items)):  # dearpygui pos manipulation
            item = self.items[i]
            if not i:  # FIXME check if item width/height is more than layout width/height
                lx = self.lpos[0] + item.margin[1]
                ly = self.lpos[1] + item.margin[0]
                item.pos = [lx, ly]
                self.lpos = [(self.lpos[0] + lx + item.width + item.margin[3]) % self.width, (self.lpos[1] +
                             ly + item.height + item.margin[2]) % self.height]  # initial to last local position
                continue

            lx = self.lpos[0] + item.margin[1]
            ly = self.lpos[1] + item.margin[0]
            item.pos = [lx, ly]
            self.lpos = [self.lpos[0] + lx + item.width, self.lpos[1] +
                         ly + item.height]  # initial to last local position

            item.pos = [item.margin]  # [top, left, bottom, right]

    def render(self):
        self.arrange_layout()
        pass
