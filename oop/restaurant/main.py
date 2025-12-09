import customers.customer, items.items, orders.order, restaurant.restaurant, staff.chef, staff.staff, staff.waiter

item1 = items.MenuItem("Margherita Pizza", 42.00, "Main Course", True)
item2 = items.MenuItem("French Fries", 18.50, "Side Dish", True)
item3 = items.MenuItem("Caesar Salad", 28.00, "Starter", False)
item4 = items.MenuItem("Grilled Salmon", 67.00, "Main Course", True)
item5 = items.MenuItem("Chocolate Lava Cake", 24.00, "Dessert", True)

menu_items = [item1, item2, item3, item4, item5]

chef1 = chef.Chef("joe", 500, "italian food")
waiter1 = waiter.Waiter("david", 200)

if __name__ == "__main__":
    def main():
        print("welcome to the restaurants menu")
        restaurant_name = input("enter restaurant's name").lower()
        new_restaurant = restaurant.Restaurant(restaurant_name, menu_items)
        restaurant.Restaurant.hire_staff(chef1)
        restaurant.Restaurant.hire_staff(waiter1)




