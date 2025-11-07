menu_list = []

def bill():
    print("Food List".center(30, "-"))
    for num in range(len(menu_list)):
        print(f"{menu_list[num][0]}: {menu_list[num][1]} THB")

while True:
    menu = input("Please select menu: ").lower()
    if menu == "exit".lower():
        break
    else:
        price = int(input("Price: "))
        menu_list.append([menu, price])

bill()
