class Customer:
    name = ""
    last_name = ""
    age = 0

    def add_cart(self):
        print(f"{self.name} {self.last_name} added a product to cart")

# customer 1
# variable = Class() -> created object
customer1 = Customer()
customer1.name = "Kanyaphat"
customer1.last_name = "L."
customer1.age = 23
# variable.function()
customer1.add_cart()

# customer 2
customer2 = Customer()
customer2.name = "Daisy"
customer2.last_name = "Y."
customer2.age = 23
customer2.add_cart()

# customer 3
customer3 = Customer()
customer3.name = "Jasmine"
customer3.last_name = "J."
customer3.age = 23
customer3.add_cart()

# customer 4
customer4 = Customer()
customer4.name = "Tulip"
customer4.last_name = "M."
customer4.age = 23
customer4.add_cart()
