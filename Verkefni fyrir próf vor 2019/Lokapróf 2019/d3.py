class Order:
    def __init__(self, product_name, quantity, unit_price, order):
        #self.order = order
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price

    def add_quantity(self):
        self.quantity = 0

        pass

    def increase_unit_price(self, price_increase):
        self.price_increase = int()
        self.unit_price *= self.price_increase


    def __gt__(self, other):
        if self.quantity * self.unit_price > other.quantity * other.unit_price:
            return True

    def __eq__(self, other):
        if self.unit_price == other.unit_price:
            return True



def create_order():
    product_name = input("Product name: ")
    quantity = int(input("How many units: "))
    unit_price = float(input("Unit price: "))
    print()

    return Order(product_name, quantity, unit_price)


def main():
    orders = []
    number_of_orders = int(input("How many orders? "))

    for _ in range(number_of_orders):
        order = create_order()
        orders.append(order)

    print("Printing all orders: ")
    for order in orders:
        print(order)
    print()

    print("First order before adding to the quantity")
    print(orders[0])
    orders[0].add_quantity(3)
    print("First order after adding to the quantity")
    print(orders[0])

    for order in orders:
        order.increase_unit_price(0.25)

    for order in orders:
        print(order)

    order1 = create_order()
    order2 = create_order()

    if order1 == order2:
        print("The orders are identical")
    else:
        print("The orders are not identical")

    if order1 > order2:
        print("Order1 is greater than order2")
    else:
        print("Order1 is NOT greater thatn order2")


main()