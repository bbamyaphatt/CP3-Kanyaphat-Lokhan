print("We're going to find the velocity of the car using v = s/t formula.")
print("Please choose the velocity unit first:\n"
      "[1] km/h\n"
      "[2] m/s")

unit = int(input("unit: "))

if unit not in [1, 2]:
    print("Invalid choice. Please try again.")
else:
    s = float(input("Please enter the distance: "))
    t = float(input("Please enter the time = "))
    v = s / t

    if unit == 1:
        print("The velocity is",v, "km/h")
    else:
        print("The velocity is", v, "m/s")
