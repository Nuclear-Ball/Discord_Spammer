import pyautogui
import time
import random
i = int(0)
array = []
temp_array = []
mee6 = str(" ")
spam_text = str(" ")
repeats = str(" ")
pyautogui.FAILSAFE = False


def array_gen():
    global array
    for arr in range(100):
        array.append(int(random.randint(0, 20)))


def mee6_yes():
    global array, i, repeats, temp_array
    repeats = int(repeats)
    while i < repeats:
        array_gen()
        temp_array = str(array)
        pyautogui.write(temp_array)
        pyautogui.press('enter')
        if slow_mode == "да":
            time.sleep(5)
        i += 1
    pyautogui.press('enter')


def mee6_no():
    global i, repeats
    repeats = int(repeats)
    while i < repeats:
        pyautogui.write(spam_text)
        pyautogui.press('enter')
        if slow_mode == "да":
            time.sleep(5)
        i += 1
        time.sleep(0.4)
    pyautogui.press('enter')


if __name__ == '__main__':
    while True:
        repeats = pyautogui.prompt(text='Введите количество отправляемых сообщений!', title='Сколько будем спамить?')
        if repeats != "none":
            break
    while True:
        mee6 = pyautogui.prompt(text='Есть ли бот MEE6?(Да/Нет)', title='Есть ли бот MEE6?')
        if mee6 == "да" or mee6 == "нет":
            break
    while True:
        slow_mode = pyautogui.prompt(text='Есть ли "Медленный режим"?(Да/Нет)', title='Есть ли "Медленный режим"?')
        if slow_mode == "да" or slow_mode == "нет":
            break
    if mee6 == "нет":
        while True:
            spam_text = pyautogui.prompt(text='Какой текст будем спамить?', title='Какой текст будем спамить?')
            if spam_text != "none":
                break
        mee6_no()
    if mee6 == "да":
        mee6_yes()
