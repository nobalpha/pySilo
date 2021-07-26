import inspect
from dearpygui.dearpygui import *
from typing import List, Any


class Item:
    def __init__(self, *, type: str, pos: List[int], width: int, height: int, id: int = generate_uuid(), label: str = "", show: bool = True, user_data: Any = "",  parent: int = get_active_window(), margin: List[int] = [10, 10, 10, 10]):
        self.id = id
        self.label = label
        self.width = width
        self.height = height
        self.show = show
        self.pos = pos
        self.user_data = user_data
        self.type = type
        self.parent = parent

    def __ref__(self):
        return self.id

    def render(self):
        try:
            func = eval(f"add_{self.type}")
            args = self.__dict__.copy()
            args.pop("type")
            with window(id=self.parent):
                func(**args)
        except Exception as e:
            print(e)


# item = Item(1, 2, 3, 4, 5, 6, 7, "button", 9)
# item.render()
