import pyautogui
import time

x_global = 0
y_global = 0
z_global = 0


def home_machine():
    pyautogui.click(687, 968)
    pyautogui.write("$H")
    pyautogui.press("enter")
    while True:
        if pyautogui.pixel(250, 151) == "(0, 201, 0)":
            print("Homing Done!")
            break
        time.sleep(0.5)

    global x_global
    x_global = 0

    global y_global
    y_global = 0

    global z_global
    z_global = 0


def check_completed():
    timer = time
    time.sleep(0.5)
    while True:
        if pyautogui.pixel(250, 151) == (128, 128, 128):
            print("Coordinate Achieved" + str())
            break
        else:
            time.sleep(0.5)


def move_machine(x, y, z, feedrate):
    pyautogui.click(687, 968)
    pyautogui.write("$J=G20G91X" + str(x) + "Y" + str(y) + "Z" + str(z) + "F" + str(feedrate))
    pyautogui.press("enter")
    check_completed()


def go_to_position(x, y, z, feedrate):
    global x_global
    global y_global
    global z_global

    move_x = x - x_global
    move_y = y - y_global
    move_z = z - z_global
    move_feedrate = feedrate
    move_machine(move_x, move_y, move_z, move_feedrate)
    x_global = x
    y_global = y
    z_global = z


def pickup_chip():
    global z_global
    z_drop_position = 0
    z_global = z_drop_position
    go_to_position(0, 0, z_drop_position, 300)


def drop_chip():
    global z_global
    z_drop_position = 0
    z_global = z_drop_position
    go_to_position(0, 0, z_drop_position, 300)
