import pydirectinput, time, pyautogui

def moveTo(x, y, duration=0):
    pyautogui.moveTo(x, y, duration=duration)

def click(x, y, duration=0):
    moveTo(x, y, duration)
    pydirectinput.click()

def clickPlantacao(x, y, duration=0):
    moveTo(x, y, duration)
    time.sleep(0.3)
    pydirectinput.click(clicks=2, interval=0.01)

def rightClick(x, y, duration=0):
    moveTo(x, y, duration)
    pydirectinput.rightClick()

def dragTo(x1, y1, x2, y2, duration=0):
    moveTo(x1, y1, duration=duration)
    pydirectinput.mouseDown()
    try:
        pydirectinput.moveTo(x2, y2, duration=duration)
    finally:
        pydirectinput.mouseUp()