from .item import Item
from dearpygui.dearpygui import generate_uuid, set_item_callback
from typing import List, Any


class Button(Item):
    def __init__(self, *, id: int = generate_uuid(), label: str = "", width: int, height: int, show: bool = True, pos: List[int], user_data: Any = "", parent: int, callback, enabled: bool = True):
        type = "button"
        super().__init__(id=id, label=label, width=width, height=height,
                         show=show, pos=pos, user_data=user_data, type=type, parent=parent)
        print(self.type)
        self.callback = callback
        self.enabled = enabled

    def init_callback(self):
        set_item_callback(self.id, self.callback)
        return True
