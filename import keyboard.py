import keyboard

while True:
    if keyboard.read_key() == '`':
        keyboard.press_and_release('backspace')
        keyboard.press_and_release('backspace')
        keyboard.press_and_release('space')
        keyboard.press('shift')
        keyboard.press_and_release('<')
        keyboard.press_and_release('!')
        keyboard.release('shift')
        keyboard.press_and_release('-')
        keyboard.press_and_release('-')
    if keyboard.read_key() == '=':
        break