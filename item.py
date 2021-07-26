# TODO Typechecking
# TODO Fallback value
# TODO Render UI OOP System
# TODO Simple Hello World Interface
import inspect
from dearpygui.dearpygui import *
from typing import List


class Item:
    def __init__(self, *, id: int = generate_uuid(), label: str = "", width: int, height: int, show: bool = True, pos: List[int], user_data: Any = "", type: str, parent: int):
        self.id = id
        self.label = label
        self.width = width
        self.height = height
        self.show = show
        self.pos = pos
        self.user_data = user_data
        self.type = type
        self.parent = parent

    def render(self):
        try:
            func = eval(f"add_{self.type}")
            args = self.__dict__.copy()
            args.pop("type")
            print(args)
            print(func(**args))
            # print("add_{0}({1})".format(self.type, self.__dict__.items().__str__()))
            # print(f"{self.__dict__.keys()}\n {self.__dict__.values()}")
            print(f"{[x[0] for x in list(self.__dict__.items())]}")
        except Exception as e:
            print(e)


# item = Item(1, 2, 3, 4, 5, 6, 7, "button", 9)
# item.render()
