from movements import *
import time

time.sleep(10)

for i in range(10):
    move_machine(0, 0, -0.5, 500)
    time.sleep(3)
    move_machine(0, 0, 0.5, 500)
    move_machine(-5.4, 11.625, 0, 9000)
    move_machine(0, 0, -0.5, 500)
    time.sleep(3)
    move_machine(0, 0, 0.5, 500)
    move_machine(5.4 - 0.508, -11.625, 0, 9000)
