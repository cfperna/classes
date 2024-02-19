class Animal:
    def __init__(self) -> None:
        self.age = 1

    def eat(self):
        print("eat")


class Mammel(Animal):
    def walk(self):
        print("walk")


class fish(Animal):
    def swim(self):
        print("Swim)")


m = Mammel()
m.eat()
print(m.age)
print(isinstance(m, object))
print(issubclass(Mammel, Animal))


class RaiseOperationError(Exception):
    pass


class Stream:
    def __init__(self) -> None:
        self.opened = False

    def open(self):
        if self.opened:
            raise RaiseOperationError('File is already open')
        self.open = True

    def close(self):
        if not self.open:
            raise RaiseOperationError('File is already closed')
        self.open = False


class FileStream(Stream):
    def Read(self):
        print('Reading for file')


class NetworkStream(Stream):
    def Read(self):
        print('Reading data for Network')


n = NetworkStream()

n.Read()
