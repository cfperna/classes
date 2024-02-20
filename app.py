
from abc import ABC, abstractmethod


class UIcontrol(ABC):

    @abstractmethod
    def draw(self):
        pass


class TextBox(UIcontrol):
    def draw(self):
        print("Text Box")


class DropDownList(UIcontrol):
    def draw(self):
        print('DropdownList')


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()


draw([ddl, tb])
