menu_dict = {
    "ข้าวหมกไก่": 45,
    "ข้าวมันไก่": 40,
    "ข้าวมันไก่ผสม": 50,
    "ข้าวมันไก่พิเศษ": 45
}
menu_list = []

def bill():
    print("Food List".center(30, "-"))
    total_price = 0
  
    for num in range(len(menu_list)):
        print(f"{menu_list[num][0]}: {menu_list[num][1]} THB")
        total_price += menu_list[num][1]
      
    print("------------------------------")
    print(f"Total price: {total_price} THB")

while True:
    menu = input("Please select menu: ").lower()
    if menu == "exit".lower():
        break
    else:
        menu_list.append([menu, menu_dict[menu]])

bill()
