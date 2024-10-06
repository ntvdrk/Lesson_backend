class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}, Тип: {self.toy_type}"

class Factory:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def purchase(self):
        print(f"Закупка сырья для игрушки {self.name}.")

    def sewing(self):
        print(f"Пошив игрушки {self.name}.")

    def coloring(self):
        print(f"Окраска игрушки в цвет {self.color}.")

    def create_toy(self):
        self.purchase()
        self.sewing()
        self.coloring()
        return Toy(self.name, self.color, self.toy_type)

factory = Factory("Мики-маус", "Разноцветный", "Персонаж мультфильма")
toy = factory.create_toy()
print(toy)