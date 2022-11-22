import pyautogui
import time
import cv2
import numpy as np
from pynput import keyboard
from pynput.keyboard import Controller as c_keyboard


# time.sleep(2)

# print('start')
# 方向框

ck = c_keyboard()



def tempmatch(ml,tem,dir):
    movesgary = cv2.cvtColor(ml, cv2.COLOR_BGR2GRAY)
    temgray = cv2.cvtColor(tem, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(movesgary, temgray,	cv2.TM_CCOEFF_NORMED)

    threshold = 0.9
    loc = np.where(result >= threshold)
    pos = []
    for pt in zip(*loc[::-1]): 
        pos.append([dir,pt[0],pt[1]])
    return pos


def main():
    pyautogui.screenshot(r'C:\Users\CloverCho\Desktop\test\nobody\sc.png', region=(500, 780, 900, 75))

    moves = cv2.imread('sc.png')
    d = cv2.imread('d.png')
    l = cv2.imread('l.png')
    u = cv2.imread('u.png')
    r = cv2.imread('r.png')

    buttons = []

    rr = tempmatch(moves,r,'r')
    if len(rr)!=0:
        for x in rr:
            buttons.append(x)

    dd = tempmatch(moves,d,'d')
    if len(dd)!=0:
        for x in dd:
            buttons.append(x)

    ll = tempmatch(moves,l,'l')
    if len(ll)!=0:
        for x in ll:
            buttons.append(x)

    uu = tempmatch(moves,u,'u')
    if len(uu)!=0:
        for x in uu:
            buttons.append(x)


    

    buttons.sort(key=lambda x:x[1])
    tmp = -100
    for i in buttons:
        if (i[1]-tmp)<50: continue
        if i[0]=='d':
            ck.press(keyboard.Key.down)
            ck.release(keyboard.Key.down)
        if i[0]=='l':
            ck.press(keyboard.Key.left)
            ck.release(keyboard.Key.left)
        if i[0]=='u':
            ck.press(keyboard.Key.up)
            ck.release(keyboard.Key.up)
        if i[0]=='r':
            ck.press(keyboard.Key.right)
            ck.release(keyboard.Key.right)
        tmp = i[1]
        time.sleep(0.1)



def on_press(key):
    if key==keyboard.Key.insert:
        main()

if __name__=="__main__":
    with keyboard.Listener(on_press=on_press) as lsn:
        lsn.join()
