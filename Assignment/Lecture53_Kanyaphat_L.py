def vat_cal(price):
    result = price + (price*7/100)
    return result

print(vat_cal(int(input())))
