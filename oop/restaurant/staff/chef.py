from staff import Staff
class Chef(Staff):
    def __init__(self, name, salary, speciality):
        super().__init__(name, salary)
        self.speciality = speciality

    def cook_order(self, order):
        self.energy -= 10
        order.status = "cooking"
        order.status = "ready"

    def work(self):
        self.energy += 15
        print(f"{self.name} is cooking")