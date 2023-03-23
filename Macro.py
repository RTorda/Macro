import keyboard
import time
import random

random = random.randint(1,4)

while True:
    ido = time.time()

    while (time.time() - ido) < 12:
        keyboard.press('space')
        keyboard.press('d')
        time.sleep(0.2)  


    keyboard.release('d')
    keyboard.release('space')

    time.sleep(random)