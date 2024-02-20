class Text(str):
    def duplicate(self):
        return self + self


m = Text("Python")
print(m.duplicate())
