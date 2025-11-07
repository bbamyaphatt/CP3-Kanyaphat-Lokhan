menu_name = []
menu_price = []

def bill():
    print("Food List".center(30, "-"))
    for num in range(len(menu_name)):
        print(f"{menu_name[num]:6}: {menu_price[num]}")
    total_price = sum(menu_price)
    print("------------------------------")
    print(f"Total Price: {total_price} THB")

while True:
    menu = input("Please select menu: ").lower()
    if menu == "exit".lower():
        break
    else:
        price = int(input("Price: "))
        menu_name.append(menu)
        menu_price.append(price)

bill()
