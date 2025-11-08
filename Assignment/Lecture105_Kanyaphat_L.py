# คลาสแม่
class Vehicle:
    license_code = ""
    serial_number = ""
    def turn_on_ac(self):
        print("AC is turned on")

# คลาสลูก
class Car(Vehicle):
    pass
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estate_car(Vehicle):
    pass

car1 = Vehicle()
car1.turn_on_ac()

pickup1 = Vehicle()
pickup1.turn_on_ac()

van1 = Vehicle()
van1.turn_on_ac()

estate1 = Vehicle()
estate1.turn_on_ac()
