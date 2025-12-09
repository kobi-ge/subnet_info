
class MenuItem:
    def __init__(self, name, price, category, available: bool):
        self.name = name
        self.price = price
        self.category = category
        self.available = available

    def get_info(self):
        print(self.name)
        print(self.price)
        print(self.category)
        print(f"availability: {self.available}")

    def set_available(self):
        if self.available:
            self.available = False
        else:
            self.available = True

    def is_available(self):
        return self.available


class Menu:
    def __init__(self,):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_item_by_name(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def get_items_by_category(self, category):
        current_category = []
        for item in self.items:
            if item.category == category:
                current_category.append(item)
        return current_category

    def display_menu(self):
        return self.items

    def get_total_items(self):
        return len(self.items)
