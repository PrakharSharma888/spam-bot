import pyautogui,time
time.sleep(5)
f = open("hell.txt",'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("Space")
f.close()




