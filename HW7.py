


class ItemToPurchase:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def __str__(self):
        total_price = self.__quantity * self.price
        return f"{self.name}: {self.__quantity} @ ${self.price:.2f} = ${total_price:.2f}"


class ShoppingCart:

    def __init__(self, customer_ID):
        self.customer_id = customer_ID
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)
        
    def remove_items(self, item):
        self.cart_items.remove(item)

    def change_quantity(self, name, new_quantity):
        for item in self.cart_items:
            if item.name == name:
                item.set_quantity(new_quantity)

    def print_cart(self):
        total_price = 0
        print(f"Shopping Cart for Customer: {self.customer_id}")
        for item in self.cart_items:
            print(item)
            total_price += item.price * item.get_quantity()
        print(f"TOTAL: ${total_price:.2f}")


def main():
    potato_chips = ItemToPurchase("Potato Chips", 3.49, 1)
    potato_chips.set_quantity(2)
    soda = ItemToPurchase("Soda", 1.50, 1)
##    print(potato_chips)
##    print(soda)

    cart = ShoppingCart("987654")
    cart.add_item(potato_chips)
    cart.add_item(soda)
    cart.print_cart()

    cart.remove_items(potato_chips)
    print()
    cart.print_cart()

    cart.change_quantity("Soda", 3)
    print()
    cart.print_cart()

if __name__ == '__main__':
    main()

    
