class Animal:

    def __init__(
            self, name: str,
            appetite: int,
            is_hungry: bool = True
    ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite
        return 0


class Cat(Animal):

    def __init__(
            self, name: str,
            is_hungry: bool = True,
            appetite: int = 3
    ) -> None:
        super().__init__(name, is_hungry)
        self.appetite = appetite
        self.is_hungry = is_hungry

    def catch_mouse(self) -> None:
        print("The hunt began!")


class Dog(Animal):

    def __init__(
            self, name: str,
            is_hungry: bool = True,
            appetite: int = 7
    ) -> None:
        super().__init__(name, is_hungry)
        self.appetite = appetite

    def bring_slippers(self) -> None:
        print("The slippers delivered!")


def feed_animals(list_animals: list) -> int:
    total_fed = 0
    for animal in list_animals:
        if isinstance(animal, Cat) and animal.is_hungry:
            animal.feed()
            total_fed += 3
        elif isinstance(animal, Dog) and animal.is_hungry:
            animal.feed()
            total_fed += 7
        elif animal.is_hungry:
            animal.feed()
            total_fed += animal.appetite
    return total_fed
