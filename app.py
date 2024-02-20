
from abc import ABC, abstractmethod


class RaiseOperationError(Exception):
    pass


class Stream (ABC):
    def __init__(self) -> None:
        self.opened = False

    def open(self):
        if self.opened:
            raise RaiseOperationError('File is already open')
        self.opened = True
        print('open')

    def close(self):
        if not self.open:
            raise RaiseOperationError('File is already closed')
        self.opened = False


    @abstractmethod
    def Read(self):
        print('Reading data from memory stream')


class MemoryStream(Stream):
    def Read(self):
        print("reading data from Memory")


m = MemoryStream()
m.Read()
m.open()

