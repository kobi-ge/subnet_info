from ..orders import order
class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.money = 1000
        self.staff = []
        self.orders = []
        self.orders_count = 0

    def hire_staff(self, staff_member):
        self.staff.append(staff_member)

    def fire_someone(self, staff_name):
        self.staff.remove(staff_name)

    def create_order(self, customer):
        self.orders_count += 1
        new_order = order.Order(customer, self.orders_count)
        self.orders.append(new_order)

    # def process_order(self, new_order):
    #     for i in self.staff:

    def complete_order(self, new_order):
        self.money += new_order.total_price
        self.orders.remove(new_order)

    def pay_salaries(self):
        for worker in self.staff:
            self.money -= worker.salary

    def get_statistics(self):
        stats = {}
        stats["total orders"] = self.orders_count
        stats["total money"] = self.money
        stats["number of workers"] = len(self.staff)

    def display_status(self):
        print(self.get_statistics)

    # def show_menu(self):
    #     print(f"1: create order\n"
    #           f"2: view orders\n"
    #           f"3: manage staff\n"
    #           f"4: view staff\n"
    #           f"5: end day")

    # def run_day(self):













