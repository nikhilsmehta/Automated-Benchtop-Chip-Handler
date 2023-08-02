from movements import *
import time

time.sleep(5)

for i in range(10):
    go_to_position(14.145 - (0.50393701 * i), 1.020, z_idling_position, 13000)
    pickup_chip("tray")
    go_to_position(8.758 - (0.50393701 * i), 12.641, z_idling_position, 13000)
    drop_chip("tray")
