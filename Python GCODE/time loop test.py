import time
import pyautogui

timeout = time.time() + 60*5
while True:
    pixel_color = pyautogui.pixel(x, y)
    if pixel_color == target_color:
        break
    time.sleep(retry_interval)