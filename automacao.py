import pandas as pd
import pyautogui
import time

#Iniciar a automação
pyautogui.PAUSE = 0.5


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(4)

pyautogui.write("http://www.sauer.pro.br/python/automacao/index.html")
pyautogui.press("enter")
pyautogui.click(x=-1282, y=917)
pyautogui.write("admin")

#pyautogui.press("enter")
#pyautogui.write("admin")
