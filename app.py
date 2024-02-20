class Text(str):
    def duplicate(self):
        return self + self


class TrackableChanges(list):
    def append(self, object):
        print('Append Called')
        super().append(object)


list = TrackableChanges()
list.append("2")


m = Text("Python")
print(m.duplicate())
