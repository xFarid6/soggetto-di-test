import keyboard
import mouse
import time

a: int = 5

while True:
    if keyboard.is_pressed('d'):
        print('ok')
        time.sleep(0.2)
        mouse.click()
    if keyboard.is_pressed('q'):
        exit()