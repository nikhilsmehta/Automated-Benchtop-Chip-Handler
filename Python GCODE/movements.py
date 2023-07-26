import pyautogui
import time

def home_machine():
    pyautogui.click(687, 968)
    pyautogui.write("$H")
    pyautogui.press("enter")
    while True:
        if pyautogui.pixel(250,151) == "(0, 201, 0)":
            print("Homing Done!")
            break
        time.sleep(0.5)

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



