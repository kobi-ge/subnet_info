
class Order:
    def __init__(self, customer, order_number):
        self.costumer = customer
        self.order_number = order_number
        self.status = ""
        self.total_price = 0
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        self.total_price += item.price

    def remove_item(self, item):
        self.items.remove(item)
        self.total_price -= item.price

    def get_total(self):
        return self.total_price

    def set_status(self, new_status):
        self.status = new_status

    def display_order(self):
        print(self.items)

    def is_complete(self):
        return self.status == "delivered"
