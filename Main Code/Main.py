from movements import *
import time

time.sleep(3)
move_machine(0, 0, 0.1, 9000)
while True:

    move_machine(0, 6, 0, 9000)
    move_machine(0, 0, -0.1, 9000)
    time.sleep(0.2)
    move_machine(0, 0, 0.1, 9000)

    move_machine(9, 0, 0, 9000)
    move_machine(0, 0, -0.1, 9000)
    time.sleep(0.2)
    move_machine(0, 0, 0.1, 9000)

    move_machine(0, -6, 0, 9000)
    move_machine(0, 0, -0.1, 9000)
    time.sleep(0.2)
    move_machine(0, 0, 0.1, 9000)

    move_machine(-9, 0, 0, 9000)
    move_machine(0, 0, -0.1, 9000)
    time.sleep(0.2)
    move_machine(0, 0, 0.1, 9000)