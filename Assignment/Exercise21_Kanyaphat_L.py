from tkinter import *
import math

def left_click(event):
    bmi_cal = float(text_box_weight.get())/math.pow(float(text_box_height.get())/100,2)
    if bmi_cal >= 30.0:
        label_result.configure(text = "อ้วนมาก")
    elif bmi_cal >= 25.0 and bmi_cal <= 29.9:
        label_result.configure(text = "อ้วน")
    elif bmi_cal >= 23.0 and bmi_cal <= 24.9:
        label_result.configure(text = "น้ำหนักเกิน")
    elif bmi_cal >= 18.6 and bmi_cal <= 22.9:
        label_result.configure(text = "น้ำหนักปกติ เหมาะสม")
    else:
        label_result.configure(text = "ผอมเกินไป")

main = Tk()

# height
label_height = Label(main, text = "ส่วนสูง (cm)")
label_height.grid(row=0, column=0)
text_box_height = Entry(main)
text_box_height.grid(row=0, column=1)

# weight
label_weight = Label(main, text = "น้ำหนัก (kg)")
label_weight.grid(row = 1, column = 0)
text_box_weight = Entry(main)
text_box_weight.grid(row = 1, column = 1)

# cal button
cal_button = Button(main, text = "คำนวณ")
cal_button.bind("<Button-1>", left_click)
cal_button.grid(row = 2, column = 0)

# result
label_result = Label(main, text = "ผลลัพธ์")
label_result.grid(row = 2, column = 1)

main.mainloop()
