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
