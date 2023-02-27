import pyautogui
import random
import time
import keyboard

# Defina as teclas que deseja usar para gerar os combos
keys = ["w", "a", "s", "d", "alt", "q", "e", "f", "shift", "1", "2"]

# Defina o tempo que deseja manter o combo pressionado
combo_duration = 15

while True:
    # Gere um combo aleatório com até 3 teclas
    combo = random.sample(keys, random.randint(1, 3))

    # Pressione as teclas do combo
    for key in combo:
        keyboard.press(key)

    # Solte as teclas do combo
    for key in combo:
        keyboard.release(key)

    # Espere 5 segundos antes de gerar o próximo combo
    time.sleep(5)
