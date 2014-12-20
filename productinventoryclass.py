# Product Inventory Class


class Product(object):

    def __init__(self, price, ID, quantity):
        self.price = price
        self.id = ID
        self.quantity = quantity


class Inventory(object):

    def __init__(self, products):
        self.products = products
        self.value = 0

    def print_inv(self):
        for product in self.products:
            print (product.id)

    def add_to_inv(self, item):
        self.products.append(item)

    def inv_sum(self):
        sum_ = 0
        for product in self.products:
            sum_ += product.price * product.quantity
        print ("$" + str(sum_))

t = Product(245, "Craftsman Toolbox", 1)
s = Product(35, "Screwdriver", 3)
r = Product(103.78, "Rearbelt", 11)
inv = Inventory([])
inv.add_to_inv(t)
inv.add_to_inv(s)
inv.add_to_inv(r)
inv.print_inv()
inv.inv_sum()

