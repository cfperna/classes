



class TextBox:
    def draw(self):
        print("Text Box")


class DropDownList:
    def draw(self):
        print('DropdownList')


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()


draw([ddl, tb])
