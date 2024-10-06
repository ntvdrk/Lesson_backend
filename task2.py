class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}"


class Animal(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = "Животное"

    def __repr__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}, Тип: {self.toy_type}"


class CartoonCharacter(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = "Персонаж мультфильма"

    def __repr__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}, Тип: {self.toy_type}"


class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def purchase_materials(self):
        print(f"Закупка сырья для игрушки {self.name}.")

    def sewing(self):
        print(f"Пошив игрушки {self.name}.")

    def coloring(self):
        print(f"Окраска игрушки в цвет {self.color}.")

    def create_toy(self):
        self.purchase_materials()
        self.sewing()
        self.coloring()

        if self.toy_type == "Животное":
            return Animal(self.name, self.color)
        elif self.toy_type == "Персонаж мультфильма":
            return CartoonCharacter(self.name, self.color)
        else:
            raise ValueError(f"Неизвестный тип игрушки: {self.toy_type}")


factory_animal = Toy("Пингвин", "Белый", "Животное")
animal_toy = factory_animal.create_toy()
print(animal_toy)

factory_cartoon = Toy("Винни пух", "Оранжевый", "Персонаж мультфильма")
cartoon_toy = factory_cartoon.create_toy()
print(cartoon_toy)

