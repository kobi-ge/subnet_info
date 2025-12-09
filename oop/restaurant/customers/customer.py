
class Customer:
    def __init__(self, name, satisfaction=50):
        self.name = name
        self.satisfaction = satisfaction

    def increase_satisfaction(self, amount):
        if self.satisfaction + amount <= 100:
            self.satisfaction += amount

    def decrease_satisfaction(self, amount):
        if self.satisfaction - amount >= 0:
            self.satisfaction -= amount

    def is_happy(self):
        return self.satisfaction >= 70

    def get_info(self):
        print(f"costumer: {self.name} rated us {self.satisfaction}% satisfaction rating")
