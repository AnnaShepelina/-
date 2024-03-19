class Weapon:
    def __init__(self, name, material, price):
        self.name = name
        self.material = material
        self.price = price

    def description(self):
        print(f"Оружие: {self.name}, Материал: {self.material}, Цена: {self.price}")


weapon1 = Weapon("Меч", "Сталь", 1000)
weapon1.description()
