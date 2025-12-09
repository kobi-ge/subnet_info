class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.energy = 100

    def work(self):
        self.energy -= 10
        print(f"{self.name} is working")

    def rest(self):
        self.energy += 20
        print(f"{self.name} is resting")

    def is_tired(self):
        return self.energy < 30

    def get_info(self):
        return f"employee: {self.name}, salary: {self.salary}, energy: {self.energy}"
