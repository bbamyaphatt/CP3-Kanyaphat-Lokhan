row_num = int(input("Enter a number: "))
for i in range(row_num):
    space = " " * (row_num - i - 1)
    print(space + ("*" * (2*i+1)) + space)
