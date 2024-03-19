class MedicalDevice:
    def __init__(self, name, device_type, functionality):
        self.name = name
        self.device_type = device_type
        self.functionality = functionality

    def device_description(self):
        print(f"Прибор: {self.name}, Тип: {self.device_type}, Функциональность: {self.functionality}")


device = MedicalDevice("ЭКГ", "Диагностический", "Измерение электрической активности сердца")
device.device_description()
