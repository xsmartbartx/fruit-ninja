import pyautogui
import time
import keyboard
import os
pyautogui.PAUSE = 0.01


def target_uderz(parameter_list):
    pass
    print(x,y)
    x_min =165
    y_min =250
    x_max =950
    y_max =600

    x1=int(x-50)
    if x1<x_min: x1=x_min
    y1=int(y+50)
    if y1<y_max: y1=y_max
    x2=int(x+50)
    if x2<x_max: x2=x_max
    y2=int(y-50)
    if y2<y_min: y2=y_min

    pyautogui.mouseDown
    pyautogui.dragTo(x1,y1, tween=pyautogui.easeInOutQuad, duration=.1)
    time.sleep(0.5)
    pyautogui.dragTo(x2,y2, tween=pyautogui.easeInOutQuad, duration=.1)
    pyautogui.mouseUp
    print(x,y)


def noz():
    pass
    x_min =165
    y_min =250
    x_max =950
    y_max =600
    models=[]
    for model in os.listdir("models"):
        pass
    models.append(os.path.join("models",model))
    while keyboard.is_pressed('q')==False:
        pass
    pyautogui.mouseUp
    time.sleep(0.3)
    for model in models:
        pass
    try:
    target =pyautogui.locateCenterOnScreen(model,
                    region=(x_min, y_min, x_max, y_max), confidence=.75
                                           )
    print("found", model, target.x,target.y)
    target_uderz(target_x, target_y)
    except:
        pass

noz()