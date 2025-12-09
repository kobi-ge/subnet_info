from staff import Staff
from ..orders import order
class Waiter(Staff):
    order_nums = 1
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.tips = 0

    def take_order(self, customer, menu):
        new_order = order.Order(customer, Waiter.order_nums, "pending")
        Waiter.order_nums += 1
        menu.display_menu()
        flag = True
        while flag:
            user_input = input("what would you like to order? (to finish type: 'finish)")
            if user_input.lower() == "finish":
                flag = False
            item = menu.get_item_by_name(user_input)
            new_order.add_item(item)
        return order

    def serve_order(self, order):
        order.status = "delivered"
        customer_satisfaction = input("enter customer's satisfaction")

    def receive_tip(self, amount):
        self.tips += amount

    def get_total_earning(self):
        return self.salary + self.tips