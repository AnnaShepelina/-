class ElectronicGadget:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year_of_release = year

    def gadget_description(self):
        print(f"Гаджет: {self.brand} {self.model}, Год выпуска: {self.year_of_release}")


gadget = ElectronicGadget("Samsung", "Galaxy S20", 2020)
gadget.gadget_description()
