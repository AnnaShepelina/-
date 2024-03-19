class Plant:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def plant_description(self):
        print(f"Растение: {self.name}, Вид: {self.species}, Возраст: {self.age}")


plant = Plant("Роза", "Многолетнее", 5)
plant.plant_description()
