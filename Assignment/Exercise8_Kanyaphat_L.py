username = input("Username: ")
password = int(input("Password: "))

# menu dict
menu = {
    "Espresso": 60,
    "Americano": 65,
    "Latte": 65,
    "Honey Lemon": 60,
    "Matcha Latte": 75,
    "Thai Tea": 70
}

# drink name
drink_name_list = list(menu.keys())

if username == "somchai" and password == 1234:
    print("Welcome K. Somchai to Somsri coffee")

    # print menu
    print("MENU:\n"
          "--------------------")
    for drink, price in menu.items():
        print(f"{drink:13} {price} THB")
    print("--------------------")

    # order
    user_order = input("What would you like to order?\n"
                           ":")
    if user_order in drink_name_list:
        user_qty = int(input("How many cups?\n"
                             ":"))
        total_price = menu[user_order] * user_qty
        print(f"Total price for {user_qty} cup(s) of {user_order} is {total_price:.2f} THB")
        print("Thank you for your order!")
    else:
        print("Sorry, the menu is not available. Please try again")
else:
    print("Your username or password is incorrect. Please try again")
