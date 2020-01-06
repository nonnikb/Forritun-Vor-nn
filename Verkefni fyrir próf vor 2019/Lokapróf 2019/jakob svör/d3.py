class Order:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def add_quantity(self,number):
        self.quantity += number

    def increase_unit_price(self, rise):
        self.price = self.price * (1+rise)


    def __str__(self):
        total_price = self.price * self.quantity
        return"Product: {}\nQuantity: {}\nUnit price: {:.2f}\nTotal: {:.2f}\n".format(self.product, int(self.quantity), self.price, total_price )

    def __eq__(self, other):
        if self.product == other.product:
            if self.quantity == other.quantity:
                if self.price == other.price:
                    return True

    def __gt__(self, other):
        if (self.quantity * self.price) > (other.quantity * other.price):
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
    print("Enter a order")
    order1 = create_order()
    print("Enter a order")
    order2 = create_order()

    if order1 == order2:
        print("The orders are identical")
    else:
        print("The orders are not identical")

    if order1 > order2:
        print("Order1 is greater than order2")
    else:
        print("Order1 is NOT greater than order2")


main()