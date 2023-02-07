import pyautogui
import os
import time
import datetime
import keyboard

app_path = 'nosleep.txt'
os.startfile(app_path)


def click_ui(png_name):
    time.sleep(0.5)  # 等待0.5s
    left, top, width, height = pyautogui.locateOnScreen(png_name, grayscale=True, confidence=0.7)  # 寻找图片
    center = pyautogui.center((left, top, width, height))  # 寻找图片中心位置
    print(center)
    pyautogui.click(center)  # 点击中心
    print("click_ui:点击成功")


click_ui('nosleep.png') # 点击任务栏记事本图标
click_ui('nosleep.png') # 点击任务栏记事本图标

# 100=2min
# 100000=2000min
for i in range(100000):
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if keyboard.is_pressed('esc'):
        print('手动结束')
        break
    elif time_now == '2023-02-07 10:09:00':
        print('定时结束')
        break
    else:
        pyautogui.typewrite(time_now, 0.05)
        pyautogui.press('enter')

print('结束')
