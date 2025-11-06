def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Username or Password is incorrect. Please try again.")

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        totalPrice = int(input("Total Price : "))
        print(f"Total price with VAT is {vatCalculator(totalPrice)}")
    elif userSelected == 2:
        return priceCalculator()
    else:
        print("Invalid option. Please try again.")

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    total_price = price1 + price2
    print(f"Total price is {total_price}")
    is_vat_needed = int(input("Do you want to calculate total price with VAT include?\n"
                            "[1] Yes\n"
                            "[2] No\n : "))
    if is_vat_needed == 1:
        outcome = vatCalculator(total_price)
        print(f"Total price with VAT is {outcome}")
    if is_vat_needed == 2:
        print(f"Total price is {total_price}")

login()
