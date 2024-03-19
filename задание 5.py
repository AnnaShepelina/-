class OpticalDevice:
    def __init__(self, name, device_type, power):
        self.name = name
        self.device_type = device_type
        self.power = power

    def description(self):
        print(f"Прибор: {self.name}, Тип: {self.device_type}, Мощность: {self.power}")


device = OpticalDevice("Телескоп", "Оптический", "500x")
device.description()
